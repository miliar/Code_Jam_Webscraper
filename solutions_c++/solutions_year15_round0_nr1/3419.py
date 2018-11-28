#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++)
	{
		int smax;
		scanf("%d",&smax);
		char str[smax+1];
		getchar();
		scanf("%s",str);
		//printf("%d\n",t );
		int ans=0,sum=0;
		for(int i=0;i<=smax;i++)
		{
			if(sum<i) 
			{
				int p=i-sum;
				sum+=p;
				ans+=p;
				
			}
			sum+=str[i]-'0';
		}
		printf("Case #%d: %d\n",tt,ans);
		
	}
	return 0;
}