#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t, k, c, s, ind=0;
	scanf("%d",&t);
	while(t--)
	{
		ind++;
		scanf("%d%d%d",&k,&c,&s);
		printf("Case #%d: ", ind);
		for(int i=1;i<=k;i++)
		{
			printf("%d ", i);
		}
		printf("\n");
	}
	return 0;
}