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

const int max_n=1010;

int T;
int n;

int a[max_n];
int qleft[max_n],qright[max_n];
pii Q[max_n];
int dp[max_n+1][max_n];

int main()
{
	gi(T);

	rep(z,T)
	{
		printf("Case #%d: ",z+1);

		gi(n);
		rep(i,n)
		{
			gi(a[i]);
			Q[i]=pii(a[i],i);
		}
		sort(Q,Q+n,greater<pii>());
		rep(i,n)
		{
			qleft[i]=0;
			rep(j,i)
				qleft[i]+=(a[j]>a[i]);
			qright[i]=0;
			forup(j,i+1,n)
				qright[i]+=(a[j]>a[i]);
		}

		rep(i,n+1)
			rep(j,n)
				dp[i][j]=inv;
		rep(j,n)
			dp[1][j]=0;
		forup(i,1,n)
			for(int j=0; j+i-1<n; ++j)
			{
				int x=Q[i].sc;

				// place x to the left
				if(j-1>=0) dp[i+1][j-1]=min(dp[i+1][j-1],dp[i][j]+qleft[x]);

				// place x to the right
				if(j+i-1+1<n) dp[i+1][j]=min(dp[i+1][j],dp[i][j]+qright[x]);
			}
		pin(dp[n][0]);
	}
	
	return 0;
}