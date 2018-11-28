#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <climits>
#include <sstream>
#include <cstring>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#include <map>
#include <set>

#define INF (INT_MAX/3)
#define MAXM 1000
#define MAXS MAXM
#define MAXE MAXM

typedef long long lint;
typedef long double ldouble;

using namespace std;

const lint MOD = 1000002013LL;

lint caps[1+MAXS+MAXE+1][1+MAXS+MAXE+1];
ldouble cost[1+MAXS+MAXE+1][1+MAXS+MAXE+1];
ldouble origcost[1+MAXS+MAXE+1][1+MAXS+MAXE+1];

int prev[1+MAXS+MAXE+1], mark[1+MAXS+MAXE+1];
ldouble mindist[1+MAXS+MAXE+1];

lint calc_dist_cost(lint n, lint diff)
{
	return n*diff - diff*(diff-1)/2;
}

int get(lint v, const vector <lint>& ve)
{
	return lower_bound(ve.begin(), ve.end(), v)-ve.begin();
}

lint min_cost(int n)
{
	lint result = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			origcost[i][j] = cost[i][j];
		}
	}

	while(1) {
		for (int i = 0; i < n; i++) {
			mindist[i] = 1e200;
			prev[i] = -1;
			mark[i] = 0;
		}
		prev[0] = -2;
		mindist[0] = 0;



		int curr = 0;
		while (curr != -1) {
			mark[curr] = 1;

			for (int i = 0; i < n; i++) {
				if (caps[curr][i] > 0 && mindist[i] > mindist[curr] + cost[curr][i]) {
					mindist[i] = mindist[curr] + cost[curr][i];
					prev[i] = curr;
				}
			}
			
			curr = -1;
			for (int i = 0; i < n; i++)
				if (!mark[i] && prev[i] != -1 && (curr == -1 || mindist[i] < mindist[curr]))
					curr = i;
		}

		if (prev[n-1] == -1) break;

		lint amount = 4000000000000000000LL;
		int u = prev[n-1], v = n-1;
		while (u != -2) {
			amount = min(amount, caps[u][v]);
//			printf("%d -> %d, cost = %lf\n", u, v, (double)origcost[u][v]);
			v = prev[v];
			u = prev[u];

		}

		u = prev[n-1], v = n-1;
		while (u != -2) {
			result += amount*origcost[u][v];
			caps[u][v] -= amount;
			caps[v][u] += amount;
			v = prev[v];
			u = prev[u];
		}

//		printf("Amount: %lld\n", amount);

		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				cost[i][j] += mindist[i] - mindist[j];
	}

	return result;
}

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);
	
	for (int test = 0; test < ntest; test++) {
		fprintf(stderr, "Test = %d\n", test);

		int n, m;
		vector <lint> starts, ends;
		vector <pair <lint, pair <lint, lint> > > edges;
		lint honest_cost = 0;

		scanf("%d %d", &n, &m);
		
		for (int i = 0; i < m; i++) {
			int s, t, w;
			scanf("%d %d %d", &s, &t, &w);
			edges.push_back(make_pair(s, make_pair(t, w)));

			starts.push_back(s);
			ends.push_back(t);

			

			honest_cost += calc_dist_cost(n, abs(s-t))*(lint)w;
//			printf("HC: %lld\n", honest_cost);
		}

		sort(starts.begin(), starts.end());
		sort(ends.begin(), ends.end());
		starts.resize(unique(starts.begin(), starts.end())-starts.begin());
		ends.resize(unique(ends.begin(), ends.end())-ends.begin());

		int nstart = starts.size(), nend = ends.size();

		int n2 = 1+nstart+nend+1;

		for (int i = 0; i < n2; i++) {
			for (int j = 0; j < n2; j++) {
				caps[i][j] = 0;
				cost[i][j] = 0;
			}
		}

//		printf("Nstart = %d, nend = %d\n", nstart, nend);

		sort(edges.begin(), edges.end());
		for (int i = 0; i < m; i++) {
			lint ss = edges[i].first;
			lint reach = edges[i].second.first;

			caps[0][1+get(edges[i].first, starts)] += edges[i].second.second;
			caps[1+nstart+get(edges[i].second.first, ends)][1+nstart+nend] += edges[i].second.second;
			for (int j = 0; j < m; j++) {
				lint s = edges[j].first, t = edges[j].second.first;
				if (t < ss) continue;
				if (s > reach) continue;
				reach = max(reach, t);

				caps[1+get(ss, starts)][1+nstart+get(t, ends)] += edges[i].second.second;
				cost[1+get(ss, starts)][1+nstart+get(t, ends)] = calc_dist_cost(n, abs(ss-t));
//				printf("%d -> %d, origcost = %lld\n", 1+get(ss, starts), 1+nstart+get(t, ends),  calc_dist_cost(n, abs(ss-t)));
			}
		}

		lint mc = min_cost(1+nstart+nend+1);

		printf("Case #%d: %lld\n", test+1, honest_cost-mc);
//		printf("Hoenst cost: %lld\n", honest_cost);
//		printf("Mincost: %lld\n", mc);
	}

	return 0;
}
