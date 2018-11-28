/* Man Mohan Mishra
   IIIT Allahabad
*/
#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.in","w",stdout);
	int t,tc;
	tc = 1;
	scanf("%d",&t);
	while (t --) {
		int k,c,s,i;
		long long d,ans;
		scanf("%d%d%d",&k,&c,&s);
		d = 1;
		for (i = 0; i < c - 1; i++) {
			d = d * k;
		}
		ans = 1;
		printf("Case #%d:",tc);
		for (i = 0; i < s; i++) {
			printf(" %lld",ans);
			ans = ans + d;
		}
		printf("\n");
		tc += 1;
	}
	return 0;
}
