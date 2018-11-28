#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

#define f first
#define s second

int t, cases, n, best, worst;
pair<double,int> val[2020];

int main() {
	scanf("%d", &t);
	cases = 1;
	while(t--) {
		scanf("%d", &n);
		
		for (int i = 0; i < n; ++i) {
			scanf("%lf", &val[i].f);
			val[i].s = 1;
		}
		
		for (int i = 0; i < n; ++i) {
			scanf("%lf", &val[i+n].f);
			val[i+n].s = 0;
		}
		n <<= 1;
		sort(val, val+n);
		
		best = 0;
		worst = 0;

		for (int i = 0, j = 0; i < n; ++i) {
			if (val[i].s) {
				j++;
			} else if (j == 0) {
				worst++;
			} else {
				j--;
			}
		}
		
		for (int i = 0, j = n-1, k; i < j; ++i) {
			if (val[i].s == 1) {
				while(j > i && val[j].s != 0) {
					--j;
				}
				val[j].s = -1;
				val[i].s = -1;
			} else if (val[i].s == 0) {
				k = i;
				while(k < n && val[k].s != 1) {
					++k;
				}
				val[k].s = -1;
				val[i].s = -1;
				best++;
			}
		}
		printf("Case #%d: %d %d\n", cases++, best, worst);
	}
	return 0;
}
