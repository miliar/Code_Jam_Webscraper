#include<stdio.h>
#include<algorithm>
int dat[1001];
int min(int a, int b)
{
	return a>b?b:a;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, TT;
	scanf("%d", &TT);
	for(T=1; T<=TT; T++)
	{
		int n, i, ans = 0, j, x;
		scanf("%d", &n);
		for(i=1; i<=n; i++)scanf("%d", &dat[i]);
		for(i=0; i<n; i++)
		{
			x = 1;
			for(j=2; j<=n-i; j++) if(dat[x] > dat[j]) x = j;
			for(j=x; j<n-i; j++)dat[j] = dat[j+1];
			ans += min(x-1, n-i-x);
		}
		printf("Case #%d: %d\n", T, ans);
	}
	return 0;
}