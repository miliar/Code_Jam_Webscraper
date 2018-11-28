/* Man Mohan Mishra
   IIIT Allahabad
*/
#include <bits/stdc++.h>

using namespace std;

char s[105];

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.in","w",stdout);
	int t,tc;
	tc = 1;
	scanf("%d",&t);
	while (t --) {
		int n,i,ans;
		scanf("%s",s);
		n = strlen(s);
		ans = 1;
		for (i = 1; i < n; i++) {
			if (s[i] != s[i - 1]) ans += 1;
		}
		if (s[n - 1] == '+') ans -= 1;
		printf("Case #%d: %d\n",tc,ans);
		tc += 1;
	}
	return 0;
}
