#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
int d[1005];
int max(int a,int b)
{
	if (a > b ) return a ;
	return b;
}
int main()
{
	int caseTest;
	int flag = 0;
	scanf("%d",&caseTest);
	int ansans = 1000;
	for (int _ = 1 ; _ <= caseTest ; _ ++)
	{
		int n;
		int maxD;
		scanf("%d",&n);
		for (int i = 1; i <= n ; i ++)
		{
			scanf("%d",&d[i]);
			maxD = max ( maxD , d[i] );
		}
		int ans = 0;
		int ansans = 1000;
		for (int i = 0 ; i <= maxD ; i ++)
		{
			for (int j = 1; j<= n ; j ++)
			{
				if (d[j] > i && i == 0) 
				{
					flag = 1;
					break;
				}

				if (d[j] > i) 
				{
					ans += (d[j] - 1) / i;
				}
			}
			if (flag == 1) 
			{
				flag = 0;
				continue ;
			}
			ans += i;
			if (ans < ansans) ansans = ans;
			ans = 0;
		}
		printf("Case #%d: %d\n",_ , ansans);
	}
}
