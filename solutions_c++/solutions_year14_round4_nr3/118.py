#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <iostream>
#include <utility>
#include <cctype>
using namespace std;

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define PRINT(x...) TRACE(printf(x))

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

#define FU(i, a, b) for(decltype(b) i = (a); i < (b); ++i)
#define fu(i, n) FU(i, 0, n)

#define mset(c, v) memset(c, v, sizeof(c))
#define mod(a, b) ((((a)%(b))+(b))%(b))
#define pb push_back
#define SZ(c) int((c).size())

const int INF = 0x3F3F3F3F; const int NEGINF = 0xC0C0C0C0;
const double EPS = 1e-8;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;


int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int main() {
	int _42;
	scanf("%d", &_42);
	fu(_41, _42) {
		printf("Case #%d: ", _41+1);
		ll W, H;
		int N;
		scanf("%lld %lld %d", &W, &H, &N);
		vll x1(N), y1(N), x2(N), y2(N);
		fu(i, N) {
			scanf("%lld %lld %lld %lld", &x1[i], &y1[i], &x2[i], &y2[i]);
		}

		vector<vector<pair<int, ll>>> graph(N+2);
		// N = left side
		// N+1 = right side
		// do it from borders to each bulding:
		graph[N].emplace_back(N+1, W);
		graph[N+1].emplace_back(N, W);
		fu(i, N) {
			graph[N].emplace_back(i, x1[i]);
			graph[i].emplace_back(N, x1[i]);
			graph[N+1].emplace_back(i, W-1-x2[i]);
			graph[i].emplace_back(N+1, W-1-x2[i]);
		}

		// between buildings:
		fu(i, N) fu(j, i) {
			ll distx = max(x1[i] - x2[j], x1[j] - x2[i]) - 1ll;
			ll disty = max(y1[i] - y2[j], y1[j] - y2[i]) - 1ll;
			ll dist = max(distx, disty);
			graph[i].emplace_back(j, dist);
			graph[j].emplace_back(i, dist);
		}

		// perform dijkstra

		priority_queue<pair<ll, int>> heap;
		vll dist(N+2, -1ll);
		vi mark(N+2, 0);
		dist[N] = 0;
		heap.push(make_pair(0ll, N));
		while (!heap.empty()) {
			int k = heap.top().second; heap.pop();
			if (mark[k] == 1) continue;
			mark[k] = 1;
			for (auto &x : graph[k]) {
				if (mark[x.first]) continue;
				if (dist[x.first] != -1ll && dist[x.first] <= dist[k] + x.second) continue;
				dist[x.first] = dist[k] + x.second;
				heap.push(make_pair(-dist[x.first], x.first));
			}
		}
		printf("%lld\n", dist[N+1]);
	}
	return 0;
}

