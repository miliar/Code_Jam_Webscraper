#include <cstdio>
#include <iostream>
using namespace std;
int p[1001];
int main()
{
	int t;
	scanf("%d", &t);
	for (int i=1; i<=t; i++)
	{
		int d;
		scanf("%d", &d);
		int most=0;
		for (int j=1; j<=d; j++)
		{
			scanf("%d", &p[j]);
			most=max(most, p[j]);
		}
		int ans=10000;
		for (int j=1; j<=most; j++)
		{
			int sum=j;
			for (int k=1; k<=d; k++) sum+=(p[k]-1)/j;
			ans=min(ans, sum);
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}