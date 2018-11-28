#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> P;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int dp[114][1919];
int h[114],g[114];
int main()
{
	int t,n,p,q;
	cin>>t;
	rep(i,t){
		cin>>p>>q>>n;
		rep(j,n) cin>>h[j]>>g[j];
		memset(dp,-1,sizeof(dp));dp[0][1]=0;
		rep(j,n) rep(k,1900){
			if(dp[j][k]<0) continue;
			//cout<<j<<' '<<k<<' '<<dp[j][k]<<endl;
			rep(l,11){
				if(q*l>=h[j]){
					dp[j+1][k+l]=max(dp[j+1][k+l],dp[j][k]);break;
				}
				int lest=h[j]-q*l,ne=(lest+p-1)/p;
				//if(j==2 && l==1) cout<<lest<<' '<<ne<<endl;
				if(k+l-ne>=0) dp[j+1][k+l-ne]=max(dp[j+1][k+l-ne],dp[j][k]+g[j]);
			}
		}
		int ret=0;
		rep(j,1919) ret=max(ret,dp[n][j]);
		printf("Case #%d: %d\n",i+1,ret);
	}
}
