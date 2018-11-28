#include <iostream>
using namespace std;

const int MAXN = 200000;//点数的最大值
const int MAXM = 1000010;//边数的最大值
const int INF = 0x3f3f3f3f;

struct Node
{
	int from, to, next;
	int cap;
}edge[MAXM];
int tol;
int head[MAXN];
int dep[MAXN];
int gap[MAXN];//gap[x]=y :说明残留网络中dep[i]==x的个数为y

int n;//n是总的点的个数，包括源点和汇点

void init()
{
	tol = 0;
	memset(head, -1, sizeof(head));
}

void addedge(int u, int v, int w)
{
	edge[tol].from = u;
	edge[tol].to = v;
	edge[tol].cap = w;
	edge[tol].next = head[u];
	head[u] = tol++;
	edge[tol].from = v;
	edge[tol].to = u;
	edge[tol].cap = 0;
	edge[tol].next = head[v];
	head[v] = tol++;
}
void BFS(int start, int end)
{
	memset(dep, -1, sizeof(dep));
	memset(gap, 0, sizeof(gap));
	gap[0] = 1;
	int que[MAXN];
	int front, rear;
	front = rear = 0;
	dep[end] = 0;
	que[rear++] = end;
	while (front != rear)
	{
		int u = que[front++];
		if (front == MAXN)front = 0;
		for (int i = head[u]; i != -1; i = edge[i].next)
		{
			int v = edge[i].to;
			if (dep[v] != -1)continue;
			que[rear++] = v;
			if (rear == MAXN)rear = 0;
			dep[v] = dep[u] + 1;
			++gap[dep[v]];
		}
	}
}

int cur[MAXN];
int S[MAXN];

int SAP(int start, int end)
{
	int res = 0;
	BFS(start, end);
	int top = 0;
	memcpy(cur, head, sizeof(head));
	int u = start;
	int i;
	while (dep[start]<n)
	{
		if (u == end)
		{
			int temp = INF;
			int inser;
			for (i = 0; i<top; i++)
				if (temp>edge[S[i]].cap)
				{
					temp = edge[S[i]].cap;
					inser = i;
				}
			for (i = 0; i<top; i++)
			{
				edge[S[i]].cap -= temp;
				edge[S[i] ^ 1].cap += temp;
			}
			res += temp;
			top = inser;
			u = edge[S[top]].from;
		}
		if (u != end&&gap[dep[u] - 1] == 0)//出现断层，无增广路
			break;
		for (i = cur[u]; i != -1; i = edge[i].next)
			if (edge[i].cap != 0 && dep[u] == dep[edge[i].to] + 1)
				break;
		if (i != -1)
		{
			cur[u] = i;
			S[top++] = i;
			u = edge[i].to;
		}
		else
		{
			int min = n;
			for (i = head[u]; i != -1; i = edge[i].next)
			{
				if (edge[i].cap == 0)continue;
				if (min>dep[edge[i].to])
				{
					min = dep[edge[i].to];
					cur[u] = i;
				}
			}
			--gap[dep[u]];
			dep[u] = min + 1;
			++gap[dep[u]];
			if (u != start)u = edge[S[--top]].from;
		}
	}
	return res;
}

bool block[500][100];
int source[500][100];
int sink[500][100];

int get_source(int i, int j) {
	if (source[i][j] == -1) {
		source[i][j] = n++;
	}
	return source[i][j];
}

int get_sink(int i, int j) {
	if (sink[i][j] == -1) {
		sink[i][j] = n++;
	}
	return sink[i][j];
}

int dir[4][2] = { 0, 1, 0, -1, 1, 0, -1, 0 };

int main() {
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; cas++) {
		memset(block, true, sizeof(block));
		memset(source, -1, sizeof(source));
		memset(sink, -1, sizeof(sink));
		init();
		int W, H, B;
		cin >> W >> H >> B;
		for (int i = 0; i < B; i++) {
			int x0, x1, y0, y1;
			cin >> x0 >> y0 >> x1 >> y1;
			for (int x = x0; x <= x1; x++) {
				for (int y = y0; y <= y1; y++) {
					block[y][x] = false;
				}
			}
		}
		n = 0;
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (block[i][j] == false) {
					continue;
				}
				int so = get_source(i, j);
				int si = get_sink(i, j);
				addedge(so, si, 1);
				for (int k = 0; k < 4; k++) {
					int newi = i + dir[k][0];
					int newj = j + dir[k][1];
					if (newi < 0 || newi >= H || newj < 0 || newj >= W) {
						continue;
					}
					if (block[newi][newj] == false) continue;
					addedge(get_sink(i, j), get_source(newi, newj), 1);
				}
			}
		}
		int totalsource = n++;
		int totlasink = n++;
		for (int j = 0; j < W; j++) {
			if (block[0][j]) {
				addedge(totalsource, get_source(0, j), 1);
			}
			if (block[H - 1][j]) {
				addedge(get_sink(H - 1, j), totlasink, 1);
			}
		}
		cout << "Case #" << cas << ": " << SAP(totalsource, totlasink) << endl;
	}
}