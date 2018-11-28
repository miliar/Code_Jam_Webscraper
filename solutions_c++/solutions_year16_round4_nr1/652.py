#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

int u[10000], v[10000];
int win[3]={1,2,0};

void lemon()
{
	int n,p,r,s; scanf("%d%d%d%d",&n,&r,&p,&s);
	//p 0, r 1, s 2
	vector<string> ans;
	rep(last,0,2)
	{
		u[1]=last;
		rep(round,1,n)
		{
			int len=1<<(round-1);
			rep(i,1,len)
			{
				v[i*2-1]=u[i];
				v[i*2]=win[u[i]];
			}
			rep(i,1,len*2) u[i]=v[i];
		}
		int len=1<<n;
		int c[3]; c[0]=0; c[1]=0; c[2]=0;
		rep(i,1,len) c[u[i]]++;
		if (c[0]==p && c[1]==r && c[2]==s)
		{
			string ss;
			rep(i,1,len)
			{
				if (u[i]==0) ss=ss+"P";
				if (u[i]==1) ss=ss+"R";
				if (u[i]==2) ss=ss+"S";
			}
			rep(i,0,n-1)
			{
				int k=1<<i;
				string ns;
				rep(j,0,len/2/k-1)
				{
					string t1,t2;
					t1=ss.substr(j*2*k,k);
					t2=ss.substr((j*2+1)*k,k);
					if (t1>t2) swap(t1,t2);
					ns=ns+t1+t2;
				}
				ss=ns;
			}
			ans.push_back(ss);
		}
	}
	sort(ans.begin(),ans.end());
	if (ans.size()==0)
		printf("IMPOSSIBLE\n");
	else  printf("%s\n",ans[0].c_str());
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("A.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(nowcase,1,tcase)
	{
		printf("Case #%d: ",nowcase);
		lemon();
	}
	return 0;
}

