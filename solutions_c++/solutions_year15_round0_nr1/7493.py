#include <iostream>
#include <cstdio>
#define ll long int
using namespace std;

int main()
{
	int t,smax,i,j,ans;
	bool fg;
	ll cnt;
	char st[1005];
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&smax);
		scanf("%s",st);
		if(smax==0)
		{
			printf("Case #%d: 0\n",i);
			continue;
		}
		fg=0;
		cnt=0;
		ans=0;
		for(j=0;st[j]!='\0';j++)
		{
			if(!fg && st[j]!='0')
				cnt=cnt+st[j]-'0';
			if(st[j]=='0')
				fg=1;
			else if(fg)
			{
				if(j<=cnt)
				{
					cnt=cnt+st[j]-'0';
				}
				else
				{
					ans=ans+(j-cnt);
					cnt=cnt+st[j]-'0'+(j-cnt);
				}		
				fg=0;
			}
		}
		if(!fg && ans==0)
			printf("Case #%d: 0\n",i);
		else
			printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}