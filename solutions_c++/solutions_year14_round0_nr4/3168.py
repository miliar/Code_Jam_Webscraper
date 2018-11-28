#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define N 1005
using namespace std;

double a[N], b[N];

int main()
{
	int t, c, n, i, j, ans1, ans2, p, q, k;
	scanf("%d",&t);
	for (c = 1; c <= t ;c++)
	{
		scanf("%d",&n);
		for (i = 0; i < n; i++)
		  scanf("%lf",&a[i]);
		for (i = 0; i < n; i++)
		  scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		ans1 = ans2 = 0;
		p = 0;
		q = k = n-1;
		while(p <= q)
		{
			if(a[q] > b[k])
			{
				ans1++;
				q--,k--;
			}
			else
				p++,k--;
		}
		p = q = n-1;
		k = 0;
		while(k <= q)
		{
			if(b[q] > a[p])
			{
				ans2++;
				p--,q--;
			}
			else
				k++,p--;
		}
		ans2 = n - ans2;
		printf("Case #%d: %d %d\n",c,ans1,ans2);
	}
	return 0;
}
