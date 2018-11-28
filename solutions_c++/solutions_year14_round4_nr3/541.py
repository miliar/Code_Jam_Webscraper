#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

map<pair<int, int>, int> f;

int w, h, b;
vector<int> g[400000];
bool out[111][555];
bool visited[400000];

int no(int x, int y) {
	return x * 2000 + 2 * y;
}

bool ins(int x, int y) {
	return x >= 0 && y >= 0 && x < w && y < h;
}

bool found_aug;

vector<int> path, aug;

void dfs(int u) {
	//printf("visiting %d\n", u);
	visited[u] = true;
	path.push_back(u);
	if (u == 400000-2) {
		found_aug = true;
		aug = path;
		path.pop_back();
		return;
	}
	for (int i = 0; i < g[u].size(); i++) if (!visited[g[u][i]] && f[make_pair(u, g[u][i])] >= 1) dfs(g[u][i]);
	path.pop_back();
}

void decrease_flow() {
	for(int i=0;i<aug.size()-1;i++) {
		f[make_pair(aug[i], aug[i+1])]--;
		f[make_pair(aug[i+1], aug[i])]++;
	}
}

int MAAA;

bool augmenting_path() {
	//printf("start\n");
	found_aug = false;
	path.clear(); aug.clear();
	fill(visited, visited+MAAA, false);
	visited[400000-1] = visited[400000-2] = false;
	dfs(400000-1);
	if (found_aug) {
		decrease_flow();
		return true;
	}
	return false;
}

void solve(int testcase) {
	scanf("%d%d%d", &w, &h, &b);
	f.clear();
	for (int x = 0; x < w; x++) for (int y = 0; y < h; y++) out[x][y] = false;
	MAAA = 2000*(w+1)+2*(h+1)+10;
	for (int i = 0; i < MAAA; i++) g[i].clear();
	for (int i = 0; i < MAAA; i++) {
		if (i%2 == 0) {
			g[i].push_back(i+1);
			g[i+1].push_back(i);
			f[make_pair(i, i+1)] = 1;
		}
	}
	for (int i = 0; i < w; i++) {
		g[400000-1].push_back(no(i, 0));
		f[make_pair(400000-1, no(i, 0))] = 1;
		g[no(i, h-1)+1].push_back(400000-2);
		f[make_pair(no(i, h-1)+1, 400000-2)] = 1;
	}
	//printf("ok\n");
	for (int i = 1; i <= b; i++) {
		int x1, y1, x2, y2; scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int x = x1; x <= x2; x++) for (int y = y1; y <= y2; y++) out[x][y] = true;
	}
	//printf("ok\n");
	for (int x = 0; x < w; x++) for (int y = 0; y < h; y++) for (int i = -1; i <= 1; i++) for (int j = -1; j <= 1; j++) if (i * j == 0 && i + j != 0) if (ins(x + i, y + j)) {
		int a = x + i, b = y + j;
		if (!out[x][y] && !out[a][b]) {
			g[no(x, y)+1].push_back(no(a, b));
			g[no(a, b)+1].push_back(no(x, y));
			
			g[no(x, y)].push_back(no(a, b)+1);
			g[no(a, b)].push_back(no(x, y)+1);
			f[make_pair(no(x, y)+1, no(a, b))] = f[make_pair(no(a, b)+1, no(x, y))] = 1;
		}
	}
	//printf("ok\n");
	int D = 0;
	while (augmenting_path()) D++;
	printf("Case #%d: %d\n", testcase, D);
}

int main() {
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) solve(i);
	return 0;
}