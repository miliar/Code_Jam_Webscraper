#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("aa1.out","w",stdout);
	int t,ans;
	char s[1009];
	int n;
	scanf("%d",&t);
	for (int j = 1; j <= t; j++) {
		scanf("%d %s",&n,s);
		int len = n + 1;
		int sum = s[0] - 48;
		ans = 0;
		for (int i = 1; i < len; i++) {
			if (sum >= i) {
				sum += (s[i]) - 48;
			} else {
				ans += i - sum;
				sum += (i-sum)+s[i]-48;
			}
		}
		printf("Case #%d: %d\n",j,ans);
	}
	
	return 0;
}
