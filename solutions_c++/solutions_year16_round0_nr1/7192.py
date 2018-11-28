#include <stdio.h>
#include <string.h>

int count(int n, int a[])
{
	int res=0;
	if (n==0 && a[n]==0) res++, a[n]=1;
	while (n) {
		if (a[n%10]==0) res++, a[n%10]=1;
		n/=10;
	}
	return res;
}

int main()
{
	int t,n,i;
	int app[10], sum, all;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for (int cas=1; cas<=t; cas++)
	{
		memset(app, 0, sizeof(app));
		scanf("%d", &n);
		if (n==0) {
			printf("Case #%d: INSOMNIA\n", cas);
			continue;
		}
		sum=n;
		all=count(n, app);
		while (all<10) {
			sum+=n;
//			if (sum>1000000000) { printf("too large\n"); break; }
			all+=count(sum, app);
		}
		printf("Case #%d: %d\n", cas, sum);
	}
	return 0;
}

