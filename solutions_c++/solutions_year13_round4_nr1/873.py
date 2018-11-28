#include <cstdio>
#include <algorithm>
#include <map>

#define SMALL
//#define LARGE

using namespace std;

long long cost;
map <pair<int, int>, int> mm;

int main()
{
#ifdef SMALL
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int T, n, m, b, e, p;
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++Case) {
		scanf("%d %d", &n, &m);
		mm.clear();
		cost = 0;
		for (int i = 0; i < m; ++i) {
			scanf("%d %d %d", &b, &e, &p);
			cost += (1LL * (n + n - e + b + 1) * (e - b) * p) >> 1;
			mm[make_pair(b, e)] += p;
		}
		map <pair<int, int>, int>::iterator iter1, iter2;
/*		for (iter1 = mm.begin(); iter1 != mm.end(); ++iter1)
			printf("%d %d %d\n", iter1->first.first, iter1->first.second, iter1->second);
		printf("\n");*/
		for (iter1 = mm.begin(); iter1 != mm.end(); ++iter1) {
			if (iter1->second == 0)
				continue;
			int b0 = iter1->first.first;
			int e0 = iter1->first.second;
			iter2 = iter1;
			iter2++;
			for (; iter2 != mm.end(); ++iter2) {
				if (iter2->second == 0)
					continue;
				int b1 = iter2->first.first;
				int e1 = iter2->first.second;
				if (e0 >= b1 && e0 < e1) {
					int temp = min(iter1->second, iter2->second);
					iter1->second -= temp, iter2->second -= temp;
					mm[make_pair(b0, e1)] += temp;
					mm[make_pair(b1, e0)] += temp;
				}
			}
		}
/*		for (iter1 = mm.begin(); iter1 != mm.end(); ++iter1)
			printf("%d %d %d\n", iter1->first.first, iter1->first.second, iter1->second);
		printf("\n");*/
		long long min_cost = 0;
		for (iter1 = mm.begin(); iter1 != mm.end(); ++iter1) {
			if (iter1->second == 0)
				continue;
			b = iter1->first.first, e = iter1->first.second, p = iter1->second;
			min_cost += (1LL * (n + n - e + b + 1) * (e - b) * p) >> 1;
		}
//		printf("%lld %lld %lld\n", cost, min_cost, cost - min_cost);
    printf("Case #%d: %lld\n", Case, cost - min_cost);
	}
	return 0;
}
