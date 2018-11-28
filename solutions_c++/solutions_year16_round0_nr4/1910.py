#include <bits/stdc++.h>

using namespace std;

int t,k,c,s;
int main(void)
{
	scanf("%d",&t);
	for (int cases = 1; cases <= t; ++cases)
	{
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d:",cases);
		for (int i = 0; i < s; ++i)
		{
			printf(" %d", i + 1);
		}
		printf("\n");
	}
	return 0;
}