#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<map>
#define X first
#define Y second
using namespace std;
#define fr(i,n) for(int i=0;i<n;i++)
#define fo(i,n) for(int i=1;i<=n;i++)
#define fe(i,n) for(__typeof(n.begin()) i=n.begin();i!=n.end();i++)
typedef long long ll;
typedef pair<ll,ll>LL;
int t,n,m,cc;
long long ans;
map<int,long long>c;
stack<LL>s;
int main()
{
	freopen("c.in","r",stdin);
	freopen("s.out","w",stdout);
	for(scanf("%d",&t);t--;)
	{
		c.clear();
		ans=0;
		cin>>n>>m;
		for(int i=0;i<m;i++)
		{
			long long x,y,z;
			cin>>x>>y>>z;
			ans+=(2*n-(y-x)+1)*(y-x)/2%1000002013*z;
			ans%=1000002013;
			c[x]+=z,c[y]-=z;
		}
		fe(i,c)
		{
			while(i->Y>0)
			{
				s.push(LL(i->X,i->Y));
				i->Y=0;
			}
			while(i->Y<0)
			{
				LL j=s.top();
				s.pop();
				ll dd=min(-i->Y,j.Y);
				j.Y-=dd;
				i->Y+=dd;
				if(j.Y)
					s.push(j);
				ans-=(ll)(2*n-(ll)(i->X-j.X)+1)*(i->X-j.X)/2%1000002013*dd;
				ans%=1000002013;
			}

		}
		printf("Case #%d: %I64d\n",++cc,(ans+1000002013)%1000002013);
	}
	return 0;
}
