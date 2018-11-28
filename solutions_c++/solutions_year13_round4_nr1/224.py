#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;
const int M=1000002013;
struct event
{
	int x,f,p;
	event() {}
	event(int a,int b,int c): x(a),f(b),p(c) {}
	bool operator < (const event &b) const
	{
		if(x!=b.x)return x<b.x;
		return f>b.f;
	}
}gao[10000];
int n,m;
int cal(int a,int b)
{
	int x=b-a;
	int ans=(1LL*n*x%M-1LL*x*(x-1)/2)%M;
	if(ans<0)ans+=M;
	return ans;
}
int X[10000],Y[10000],top;
void solve()
{
	scanf("%d %d",&n,&m);
	int cost=0;
	for(int i=1;i<=m;i++)
	{
		int a,b,c;
		scanf("%d %d %d",&a,&b,&c);
		cost=(cost+1LL*cal(a,b)*c)%M;
		gao[2*i-1]=event(a,1,c);
		gao[2*i]=event(b,-1,c);
	}
	sort(gao+1,gao+2*m+1);
	top=0;
	int ans=0;
	for(int i=1;i<=2*m;i++)
	{
		if(gao[i].f==1)
		{
			top++;
			X[top]=gao[i].x;
			Y[top]=gao[i].p;
		}
		else
		{
			int need=gao[i].p;
			while(need)
			{
				int cut=min(need,Y[top]);
				ans=(ans+1LL*cal(X[top],gao[i].x)*cut)%M;
				need-=cut;
				Y[top]-=cut;
				if(Y[top]==0)top--;
			}
		}
	}
	ans=(cost-ans)%M;
	ans=(ans+M)%M;
	printf("%d\n",ans);
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++cas);
		solve();
	}
}
