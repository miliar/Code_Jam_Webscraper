#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<cmath>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl
#define sqr(x) ((x)*(x))

int tests,n,m,ans;
int a[100100];

int main()
{
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		scanf("%d %d",&n,&m);
		for (int i=0;i<n;i++) scanf("%d",a+i);
		sort(a,a+n);
		int p=0, q=n-1;
		ans = 0;
		while (1)
		{
			if (a[p]+a[q] <= m)
				ans++,
				p++,
				q--;
			else
				q--,
				ans++;
			//printf("%d %d\n",p,q);
			if (p==q)
			{
				ans++;
				break;
			}
			if (p>q) break;
		}
		printf("Case #%d: %d\n", test, ans);
	}
	
	return 0;
}
