#include<algorithm>

typedef int FLOW;
const int MaxNode = 100010;
const int MaxEdge = 500000;
const FLOW FLOW_INF = ((FLOW)1 << (sizeof(FLOW)* 8 - 1)) - 1;

struct Edge {
	int t;
	FLOW weight;
	Edge *next;
}edges[MaxEdge * 2];
int edgecnt = 0;

struct Node {
	int d;
	Edge *edge;
}nodes[MaxNode];

void InitGraph(int n) {
	for (int i = 0; i < n; i ++) nodes[i].edge = NULL;
	edgecnt = 0;
}

void _AddEdge(int s, int t, FLOW weight) {
	edges[edgecnt].t = t;
	edges[edgecnt].weight = weight;
	edges[edgecnt].next = nodes[s].edge;
	nodes[s].edge = edges + edgecnt;
	edgecnt++;
}

void AddEdge(int s, int t, FLOW weight) {
	_AddEdge(s, t, weight);
	_AddEdge(t, s, 0);
}

Edge inline *OthEd(Edge *e) { return &edges[(e - edges) ^ 1]; }

bool bfs(int s, int t, int n) {
	Node *queue[MaxNode];
	int head = 0, tail = 0;
	for (int i = 0; i<n; i++) nodes[i].d = MaxNode;
	queue[tail++] = nodes + t;
	nodes[t].d = 0;
	while (head<tail) {
		Node *cur = queue[head++];
		for (Edge *p = cur->edge; p != NULL; p = p->next) {
			if (OthEd(p)->weight>0 && nodes[p->t].d == MaxNode) {
				nodes[p->t].d = cur->d + 1;
				if (p->t == s) return true;
				queue[tail++] = nodes + p->t;
			}
		}
	}
	return false;
}

int trm;
FLOW dfs(Edge *ce, FLOW flow) {
	if (flow>ce->weight) flow = ce->weight;
	FLOW f = 0;
	if (ce->t == trm) f = flow;
	else {
		Node *n = nodes + ce->t;
		int mn = MaxNode;
		Edge *e;
		for (e = n->edge; e != NULL && f<flow; e = e->next) {
			if (e->weight>0 && nodes[e->t].d<n->d)
				f += dfs(e, flow - f);
			if (e->weight>0)
				mn = std::min(mn, nodes[e->t].d);
		}
		for (; e != NULL && mn >= n->d; e = e->next)
		if (e->weight>0)
			mn = std::min(mn, nodes[e->t].d);
		n->d = mn + 1;
	}
	OthEd(ce)->weight += f;
	ce->weight -= f;
	return f;
}

FLOW dinic(int s, int t, int n) {
	FLOW flow = 0;
	trm = t;
	while (bfs(s, t, n))
	for (Edge *e = nodes[s].edge; e != NULL; e = e->next)
	if (e->weight>0 && nodes[e->t].d<nodes[s].d)
		flow += dfs(e, FLOW_INF);
	return flow;
}

int W, H, B;
int inline ndid(int x, int y) {
	return (y * W + x) * 2;
}

int rect[10][4];

bool valid(int x, int y) {
	if (x < 0 || x >= W || y < 0 || y >= H) return false;
	for (int i = 0; i < B; i++) {
		if (x >= rect[i][0] && x <= rect[i][2] && y >= rect[i][1] && y <= rect[i][3]) return false;
	}
	return true;
}

int solve() {
	scanf("%d%d%d", &W, &H, &B);

	for (int i = 0; i < B; i++) {
		scanf("%d%d%d%d", &rect[i][0], &rect[i][1], &rect[i][2], &rect[i][3]);
		if (rect[i][0]>rect[i][2]) std::swap(rect[i][0], rect[i][2]);
		if (rect[i][1]>rect[i][3]) std::swap(rect[i][1], rect[i][3]);
	}
	int s = W * H * 2, t = s + 1, n = t + 1;
	InitGraph(n);
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			if (!valid(j, i)) continue;

			AddEdge(ndid(j, i), ndid(j, i) + 1, 1);
			int dir[][2] = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };
			for (int k = 0; k < 4; k++) {
				int x = j + dir[k][0], y = i + dir[k][1];
				if (!valid(x, y)) continue;
				AddEdge(ndid(j, i)+1, ndid(x, y), 1);
			}
		}
	}
	for (int i = 0; i < W; i++) {
		AddEdge(s, ndid(i, 0), 1);
		AddEdge(ndid(i, H - 1) + 1, t, 1);
	}
	return dinic(s, t, n);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int c = 1; c <= T; c++) {
		printf("Case #%d: %d\n", c, solve());
	}
}