#include<stdio.h>
#include<string.h>
int main()
{
	int t, cs = 1;
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d", &t);
	while(t--) {
		int n, m, i, j, k = 0, l, ans = 0;
		scanf("%d", &n);
		char str[2005];
		scanf("%s", str);
		k = (int)(str[0]-'0');
		for(i = 1; i <= n; i++) {
			if(k >= i) {
				k += (int)(str[i]-'0');
			} else {
				ans += (i-k);
				k += ((i-k)+(int)(str[i]-'0'));
			}
		}
		printf("Case #%d: %d\n",cs++, ans);
	}
	return 0;
}
