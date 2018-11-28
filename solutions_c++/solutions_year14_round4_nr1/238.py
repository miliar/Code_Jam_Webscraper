#include <cstdio>
#include <set>
using namespace std;

int t;
int n, x;
multiset <int> S;
int res;

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d", &n, &x);
		S.clear();
		for (int i = 0; i < n; i++) {
			int s; scanf("%d", &s);
			S.insert(s);
		}
		res = 0;
		while (!S.empty()) {
			multiset <int>::iterator it = S.end(); it--;
			int s = *it; S.erase(it);
			it = S.upper_bound(x - s);
			if (it != S.begin()) {
				it--; S.erase(it);
			}
			res++;
		}
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}