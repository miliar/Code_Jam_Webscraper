#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int t, n;
double a[2010], b[2010];

int main()
{
	scanf("%d",&t);
	int cas = 0;
	while (t--)
	{
		scanf("%d",&n);
		for (int i = 0; i < n; i++) 
			scanf("%lf",&a[i]);
		for (int i = 0; i < n; i++) 
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		int ans1 = 0 , ans2 = n ;
		for (int i = 0; i < n; i++) 
			if (a[i] > b[ans1]) ++ans1;
		for (int i = 0; i < n; i++) 
			if (a[n-ans2] < b[i]) --ans2;
		printf("Case #%d: ",++cas);
		printf("%d %d\n",ans1,ans2);
	}
	return 0;
}

