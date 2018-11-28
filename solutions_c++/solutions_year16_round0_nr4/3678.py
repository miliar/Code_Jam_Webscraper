#include <bits/stdc++.h>
using namespace std;
int main()
{
	int i,t;
	cin>>t;
	int k,c,s;
	int c1=0;
	while(t--)
	{
		cin>>k>>c>>s;
		printf("Case #%d: ",++c1);
		if(k==1)
		{
			printf("1\n");
		}
		else if(c==1)
		{
			if(s==k)
			{
				for(i=1;i<=k;i++)
					printf("%d ",i);
				printf("\n");
			}
			else
				printf("IMPOSSIBLE\n");
		}
		else
		{
			if(s<k-1)
			{
				printf("IMPOSSIBLE\n");
			}
			else
			{
				for(i=2;i<=k;i++)
					printf("%d ",i);
				printf("\n");
			}
		}
	}
	return 0;
}
