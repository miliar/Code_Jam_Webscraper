#include<bits/stdc++.h>
using namespace std;
char str[105];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	int k=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s",str);
		//printf("%s\n",str);
		int n=strlen(str);
		int i,j;
		long long ans=0;
		int flag=0;
		for(i=0;i<n;)
		{
			if(str[i]=='+')
			{
				flag=1;
				for(;i<n;i++)
				{	
					if(str[i]=='+')
					{
						
					}
					else
					{
						break;
					}
				}
			}
			else if(str[i]=='-')
			{
				if(flag==0)
				{
					ans+=1;
				}
				else
				{
					ans+=2;
				}
				for(;i<n;i++)
				{	
					if(str[i]=='-')
					{
						
					}
					else
					{
						break;
					}
				}
			}
		}
		printf("Case #%d: %lld\n",k++,ans);
	}
	return 0;
}
