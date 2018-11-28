#include<bits/stdc++.h>
using namespace std;
int main()
{
	int q,i,t,smax,len,sum[1003],flag,ans;
	char c[1002]={'\0'};
	freopen("in.in","r",stdin);
	freopen("out.in","w",stdout);
	scanf("%d",&t);
	for(q=1;q<=t;q++)
	{
		flag=0;
		ans=0;
		scanf("%d",&smax);
		scanf("%s",&c);
		memset(sum,0,sizeof(sum));
		for(i=0;i<smax+1;i++)
		{
			if(c[i]=='0')
				flag=1;
		}
		if(!flag)
		{
			printf("Case #%d: 0\n",q);
			continue;
		}
		while(1)
		{
			flag=0;
			for(i=1;i<smax+1;i++)
				sum[i]=sum[i-1]+c[i-1]-'0';
			for(i=1;i<smax;i++)
			{
				if(sum[i-1]==sum[i]&&sum[i]!=sum[i+1])
				{
					if(i>sum[i])
					{
						ans+=i-sum[i];
						flag=1;
						break;
					}
				}
			}
			if(i>sum[i]&&!flag)
			{
				ans+=i-sum[i];
				flag=1;
			}
			if(flag)
			{
				for(i;i>0;i--)
				{
					if((c[i-1]-'0')!=0)
						c[i]=char(ans+48);
				}
				if(i==0&&(c[i]-'0'==0))
					c[i]=char(ans+48);
			}
			else
				break;
		}
		printf("Case #%d: %d\n",q,ans);
	}
	return 0;
}
