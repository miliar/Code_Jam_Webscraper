#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0; i<(a);++i)
inline bool EQ(double a, double b) {return fabs(a-b) < 1e-9;}

const int INF = 1<<29;
typedef long long ll;

struct Building {
	Building(int x0_, int y0_, int x1_, int y1_):
		x0(x0_), y0(y0_), x1(x1_), y1(y1_) {}
	int x0, y0, x1, y1;
};

int T, W, H, B;
vector<Building> buildings;

bool* avail;
bool* visited;

vector<pair<int, int>> path;

enum Dir {UP, RIGHT, DOWN, LEFT};

int getDX(Dir d) {
	switch (d) {
		case LEFT: return -1;
		case RIGHT: return +1;
		default: return 0;
	}
}

int getDY(Dir d) {
	switch (d) {
		case UP: return -1;
		case DOWN: return +1;
		default: return 0;
	}
}

bool dfs(int x, int y, Dir d) {
	path.push_back({x, y});
	visited[W*y+x] = true;
	if (y == H - 1) return true;

	for (int dd : {1, 0, 3}) {
		Dir nd = (Dir)(((int)d+dd)%4);
		int dx = getDX(nd);
		int dy = getDY(nd);
		int nx = x+dx;
		int ny = y+dy;
		if (nx < 0 || nx >= W) continue;
		if (ny < 0) continue;
		if (visited[W*ny+nx]) continue;
		if (dfs(nx, ny, nd)) return true;
	}

	path.pop_back();
	return false;
}

void markPath() {
	for (pair<int, int> p : path) {
		int x = p.first;
		int y = p.second;
		//printf("%d %d\n", x, y);
		avail[W*y+x] = false;
	}
}

int main() {
	scanf("%d", &T);
	REP(t,T) {
		buildings.clear();
		scanf("%d%d%d", &W, &H, &B);
		REP(i,B) {
			int x0, y0, x1, y1;
			scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
			buildings.emplace_back(x0, y0, x1+1, y1+1);
		}

		if (B == 0) {
			printf("Case #%d: %d\n", t+1, W);
			continue;
		}

		vector<pair<int, pair<int, bool>>> events;
		{
			int i = 0;
			for (Building& b : buildings) {
				events.push_back({b.y0, {i, true}});
				events.push_back({b.y1, {i, false}});
				++i;
			}
		}

		sort(events.begin(), events.end());

		{
			int at = 0;
			int prev = 0;
			for (auto& e : events) {
				if (e.first - prev < W+2) {
					at += e.first - prev;
				} else {
					at += W+2;
				}
				prev = e.first;
				if (e.second.second) {
					buildings[e.second.first].y0 = at;
				} else {
					buildings[e.second.first].y1 = at;
				}
			}
			H = at;
		}

		avail = new bool[H*W];
		visited = new bool[H*W];

		REP(y,H) REP(x,W) {
			avail[W*y+x] = true;
			visited[W*y+x] = false;
		}

		for (Building& b : buildings) {
			FOR(y, b.y0, b.y1-1) FOR(x, b.x0, b.x1-1) {
				avail[W*y+x] = false;
			}
		}

		int flow = 0;

		while (true) {
			REP(y,H) REP(x,W) {
				visited[W*y+x] = !avail[W*y+x];
			}
			bool improved = false;
			REP(x,W) {
				path.clear();
				if (!visited[x] && dfs(x, 0, DOWN)) {
					markPath();
					++flow;
					improved = true;
				}
			}
			if (!improved) break;
		}

		delete[] avail;
		delete[] visited;

		printf("Case #%d: %d\n", t+1, flow);
	}
	return 0;
}
