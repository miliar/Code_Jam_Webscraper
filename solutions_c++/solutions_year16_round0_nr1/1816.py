/* Man Mohan Mishra
   IIIT Allahabad
*/
#include <bits/stdc++.h>

using namespace std;

int a[10];

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.in","w",stdout);
	int t,tc;
	tc = 1;
	scanf("%d",&t);
	while (t --) {
		int n,i,cnt;
		long long val,ans;
		scanf("%d",&n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n",tc);
			tc += 1;
			continue;
		}
		memset(a,0,sizeof(a));
		cnt = 0;
		for (i = 1; cnt < 10; i++) {
			val = n * 1LL * i;
			ans = val;
			while (val > 0) {
				if (a[val % 10] == 0) {
					a[val % 10] = 1;
					cnt += 1;
				}
				val = val / 10;
			}
		}
		printf("Case #%d: %lld\n",tc,ans);
		tc += 1;
	}
	return 0;
}
