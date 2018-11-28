#include<bits/stdc++.h>
using namespace std;
int x[1020][1020],e[2000];
main()
{
	freopen("B-large.in","r",stdin);
	freopen("Out-B-large.txt","w",stdout);
	int a,b,c,d,f,g,ans,num;
	for(a=2;a<=1000;a++)
	{
		for(b=1;b<a;b++)
		{
			for(c=b;a-c>=0;c++)
			{
				if(c==b)x[a][b]=x[a-c][b]+x[c][b]+1;
				else x[a][b]=min(x[a][b],x[a-c][b]+x[c][b]+1);
			}
		}
	}
	//printf("[%d]",x[3][2]);
	scanf("%d",&a);
	for(b=0;b<a;b++)
	{
		scanf("%d",&c);
		for(d=0;d<c;d++)
		{
			scanf("%d",&e[d]);
		}
		ans=1000;
		for(f=1;f<=1000;f++)
		{
			num=0;
			for(g=0;g<c;g++)
			{
				if(e[g]>f)num+=x[e[g]][f];
			}
			ans=min(ans,num+f);
			//printf("[%d %d %d]",f,ans,num);
		}
		printf("Case #%d: %d\n",b+1,ans);
	}
}
