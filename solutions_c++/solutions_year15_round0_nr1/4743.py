# include <iostream>
# include <cstdio>
using namespace std;
int smax,t;
int main()
{
	//freopen("in.txt","r",stdin);
//freopen("out.txt","w",stdout);
	int i,j,sum;
	int ans;
	char c;
	scanf("%d",&t);
	for (j=1;j<=t;j++)
	{
		scanf("%d\n",&smax);
		sum=ans=0;
		for (i=0;i<=smax;i++)
		{
			if (i-sum>ans)ans=i-sum;
			scanf("%c",&c);
			sum+=c-'0';
		}
		printf("Case #%d: %d\n",j,ans);
	} 
	return 0;
} 
