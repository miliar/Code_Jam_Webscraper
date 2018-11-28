#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
#define LL long long

int n;
LL rank;

int main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d%lld",&n,&rank);
		rank--;
		LL tr = rank;
		int st = 0;
		LL pow = 2;
		for (int i=0; i<n; i++)
			if (tr < (1LL<<(n-i-1))) {
				//printf("W");
				st = 1;
			}
			else {
				//printf("L");
				if (st == 0) pow *= 2;
				tr -= (1LL<<(n-i-1));
			}
		pow = pow-2;
		if (st == 0) pow = (1LL<<n)-1;
		printf("Case #%d: %lld",t,pow);

		LL mi = pow,mx = (1LL<<n),mid,ret = 0;
		while (mi < mx) {
			mid = (mi+mx)/2;
			tr = rank;
			LL hi = mid,lo = (1LL<<n)-mid-1;

			int ok = 1;
			for (int i=0; i<n; i++) {
				//printf("%lld: %lld %lld %d\n",mid,hi,lo,tr < (1LL<<(n-i-1)));
				if (tr < (1LL<<(n-i-1))) {
					if (lo < 1) {
						ok = 0; break;
					}
					lo--;
					if (hi % 2 == 0) {
						hi /= 2;
					}
					else {
						hi = (hi+1)/2;
						lo--;
					}
					lo /= 2;
				}
				else {
					if (lo > 0) {
						break;
					}
					hi -= (1LL<<(n-i-1));
					if (hi < 0) lo += hi, hi = 0;
					tr -= (1LL<<(n-i-1));
				}
			}
			if (ok) {
				ret = max(ret,mid);
				mi = mid+1;
			}
			else mx = mid;
		}
		printf(" %lld\n",ret);
	}
	return 0;
}
