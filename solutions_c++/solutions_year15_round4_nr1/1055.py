#include<bits/stdc++.h>
using namespace std;
int c,d;
char s[110][110];
int check(int e,int f)
{
	int num=4,g;
	g=f+1;while(g<d&&s[e][g]=='.')g++;if(g==d)num--;
	g=e+1;while(g<c&&s[g][f]=='.')g++;if(g==c)num--;
	g=f-1;while(g>=0&&s[e][g]=='.')g--;if(g==-1)num--;
	g=e-1;while(g>=0&&s[g][f]=='.')g--;if(g==-1)num--;
	return num;
}
main()
{
	freopen("A-large.in","r",stdin);
	freopen("out-A-large.txt","w",stdout);
	int a,b,e,f,g,ans;
	scanf("%d",&a);
	for(b=0;b<a;b++)
	{
		ans=0;
		scanf("%d %d",&c,&d);
		for(e=0;e<c;e++)
		{
			scanf("%s",s[e]);
		}
		for(e=0;e<c;e++)
		{
			for(f=0;f<d;f++)
			{
				if(s[e][f]=='>')
				{
					g=f+1;
					while(g<d&&s[e][g]=='.')g++;
					if(g==d)
					{
						g=check(e,f);
						if(g)ans++;
						else ans=-1;
					}
				}
				else if(s[e][f]=='v')
				{
					g=e+1;
					while(g<c&&s[g][f]=='.')g++;
					if(g==c)
					{
						g=check(e,f);
						if(g)ans++;
						else ans=-1;
					}
				}
				else if(s[e][f]=='<')
				{
					g=f-1;
					while(g>=0&&s[e][g]=='.')g--;
					if(g==-1)
					{
						g=check(e,f);
						if(g)ans++;
						else ans=-1;
					}
				}
				else if(s[e][f]=='^')
				{
					g=e-1;
					while(g>=0&&s[g][f]=='.')g--;
					if(g==-1)
					{
						g=check(e,f);
						if(g)ans++;
						else ans=-1;
					}	
				}
				if(ans==-1)break;
			}
			if(ans==-1)break;
		}
		if(ans==-1)printf("Case #%d: IMPOSSIBLE\n",b+1);
		else printf("Case #%d: %d\n",b+1,ans);
	}
}
