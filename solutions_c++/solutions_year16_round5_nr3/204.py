#include <bits/stdc++.h>
using namespace std;

int p[1005][3];
int v[1005][3];
bool done[1005];
int cost[1005];
int dist(int i, int j) {
	int d[3];
	for (int x = 0; x < 3; x++)
		d[x] = p[i][x] - p[j][x];
	return d[0] * d[0] + d[1] * d[1] + d[2] * d[2];
}

int main() {
	ios::sync_with_stdio(false);
	freopen("/home/ahmed/Desktop/Round 3/C/C-small-attempt0.in", "r", stdin);
	freopen("/home/ahmed/Desktop/Round 3/C/C-small-attempt0.out", "w", stdout);

	int t; cin >> t;
	int id = 1;
	while (t--) {
		int n, s; cin >> n >> s;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < 3; j++)
				cin >> p[i][j];
			for (int j = 0; j < 3; j++)
				cin >> v[i][j];
			done[i] = false;
			cost[i] = 1e9;
		}

		priority_queue<pair<int, int> > pq;
		cost[0] = 0;
		pq.push(make_pair(0, 0));
		while (!pq.empty()) {
			int node = pq.top().second; pq.pop();
			if (done[node])
				continue;
			done[node] = true;
			for (int child = 0; child < n; child++)
				if (!done[child]) {
					int ncost = max(cost[node], dist(node, child));
					if (ncost < cost[child])
						cost[child] = ncost, pq.push(make_pair(-ncost, child));
				}
		}
		printf("Case #%d: %.13lf\n", id++, sqrt(cost[1]));

	}


	return 0;
}
