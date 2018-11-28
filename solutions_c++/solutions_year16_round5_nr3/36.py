#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long double ld;
typedef pair <ld, int> ldi;

const ld Inf = 1e30l;
const int Maxn = 1005;
const int Maxd = 3;

int t;
int n, s;
int C[Maxn][Maxd];
int S[Maxn][Maxd];
ld dist[Maxn];

ld Dist(ld ax, ld ay, ld az) { return sqrt(ax * ax + ay * ay + az * az); }

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d", &n, &s);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < Maxd; j++)
				scanf("%d", &C[i][j]);
			for (int j = 0; j < Maxd; j++)
				scanf("%d", &S[i][j]);
		}
		fill(dist, dist + Maxn, Inf); dist[0] = 0;
		priority_queue <ldi> Q; Q.push(ldi(-dist[0], 0));
		while (!Q.empty()) {
			int v = Q.top().second; ld d = -Q.top().first; Q.pop();
			if (dist[v] != d) continue;
			for (int i = 0; i < n; i++) {
				ld newdist = max(d, Dist(C[v][0] - C[i][0], C[v][1] - C[i][1], C[v][2] - C[i][2]));
				if (newdist < dist[i]) {
					dist[i] = newdist;
					Q.push(ldi(-dist[i], i));
				}
			}
		}
		printf("Case #%d: %.10lf\n", tc, double(dist[1]));
	}
	return 0;
}