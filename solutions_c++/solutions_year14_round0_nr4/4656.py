#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;
int main()
{
 	freopen("D-large.in","r", stdin);
 	freopen("D-large.out","w", stdout);
	int T;
	int n;
	double weight1[2000];
	double weight2[2000];
	scanf("%d",&T);
	for (int t = 1; t <= T; ++t)
	{
		scanf("%d",&n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%lf",&weight1[i]);
		}
		for (int i = 0; i < n; ++i)
		{
			scanf("%lf",&weight2[i]);
		}
		sort(weight1,weight1+n);
		sort(weight2,weight2+n);
		int p = 0;
		int score1 = 0;
		int score2 = 0;
		for (int i = 0; i < n; ++i)
		{
			if (weight1[i] > weight2[p])
			{
				p++;
				score1++;
			}
		}
		p = n - 1;
		for (int i = n-1; i >= 0; i--)
		{
			if (weight1[i] > weight2[p])
			{
				score2++;
			}
			else
			{
				p--;
			}
		}
		printf("Case #%d: %d %d\n",t,score1,score2);
	}
	return 0;
}