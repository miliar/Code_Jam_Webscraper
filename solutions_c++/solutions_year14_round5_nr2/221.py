#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <string>
#include <cassert>
#include <cstring>

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define forup(i,a,b) for(int i=a; i<b; ++i)
#define fordn(i,a,b) for(int i=a; i>b; --i)
#define rep(i,a) for(int i=0; i<a; ++i)

#define dforup(i,a,b) for(i=a; i<b; ++i)
#define dfordn(i,a,b) for(i=a; i>b; --i)
#define drep(i,a) for(i=0; i<a; ++i)

#define slenn(s,n) for(n=0; s[n]!=13 and s[n]!=0; ++n);s[n]=0

#define gi(x) scanf("%d",&x)
#define gl(x) cin>>x
#define gd(x) scanf("%lf",&x)
#define gs(x) scanf("%s",x)

#define pis(x) printf("%d ",x)
#define pin(x) printf("%d\n",x)
#define pls(x) cout<<x<<" "
#define pln(x) cout<<x<<"\n"
#define pds(x) printf("%.12f ",x)
#define pdn(x) printf("%.12f\n",x)
#define pnl() printf("\n")

#define fs first
#define sc second

#define pb push_back

const int inv=1000000000;
const int minv=-inv;

const int max_n=100+5;
const int max_m=1010;
const int lim=200+5;

int T;
int n;
int p,q;
int h[max_n], g[max_n];
int req[lim+1];
int gain[lim+1];
bool win[lim+1];
int wingain[lim+1];

bool vs[max_n+1][max_m+1];
int dp[max_n+1][max_m+1];
int solve(int i, int m)
{
	//cout<<"@@ "<<i<<" "<<m<<" :: "<<h[i]<<" "<<req[h[i]]<<" "<<gain[h[i]]<<" "<<(req[h[i]]-m)*q+(req[h[i]]-1)*p<<"\n";

	if(i==n)
		return 0;

	if(vs[i][m]) return dp[i][m];
	vs[i][m]=true;

	dp[i][m]=0;

	// take
	if(m>=req[h[i]] or (req[h[i]]-m)*q+(req[h[i]]-1)*p<h[i])
		dp[i][m]=max(dp[i][m],solve(i+1,m-req[h[i]]+gain[h[i]])+g[i]);

	// leave
	dp[i][m]=max(dp[i][m],solve(i+1,m+(h[i]+q-1)/q));

	return dp[i][m];
}

int main()
{
	gi(T);

	rep(z,T)
	{
		printf("Case #%d: ",z+1);

		gi(p); gi(q); gi(n);

		for(int i=1; i<=200; ++i)
		{
			win[i]=false;
			int t=i,gg=0;
			while(t-q>0)
			{
				t-=q;
				++gg;
			}
			if(t<=p)
			{
				win[i]=true;
				wingain[i]=gg;
			}
		}

		for(int i=1; i<=200; ++i)
		{
			req[i]=(i+p-1)/p;
			gain[i]=0;

			int t=i,c=0;
			while(t>0)
			{
				if(win[t])
				{
					req[i]=c+1;
					gain[i]=wingain[t];
					break;
				}
				t-=p;
				++c;
			}
		}

		rep(i,n)
		{
			gi(h[i]);
			gi(g[i]);
		}

		memset(vs,0,sizeof(vs));
		pin(solve(0,1));
	}
	
	return 0;
}