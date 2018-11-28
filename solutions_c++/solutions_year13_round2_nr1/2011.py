#include <stdio.h>
#include <algorithm>

using namespace std;
int s[200000];
int ask(int x,int y)
{
	if(x==1)return 1e9;
	int it=0;
	while(x<=y)x+=x-1,it++;
	return it;
}
#define forn(i,n) for(int i=0;i<(int)n;i++)
void solve()
{
	int a;
	int n;
	scanf("%d%d",&a,&n);
	forn(i,n)
		scanf("%d",&s[i]);
	sort(s,s+n);
	int used=0;
	int ans=1e9;
	forn(i,n)
	{
		if(a>s[i])
			a+=s[i];
		else
		{
			ans=min(ans,n-i+used);//6
			used+=ask(a,s[i]);
			if(used>ans)
				break;
			while(a<=s[i])a+=a-1;
			a+=s[i];
		}
	}
	ans=min(ans,used);
	printf("%d",ans);//
	return;
}
int main()
{
	int t;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	forn(i,t)
	{
		printf("Case #%d: ",i+1);
		solve();
		puts("");
	}
	return 0;
}	