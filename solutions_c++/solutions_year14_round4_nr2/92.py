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
int a[1010],pos[1010];
int dp[1010][1010];
vector<int> b;
int main()
{
	int t,n,inf=12345678;
	cin>>t;
	rep(i,t){
		cin>>n;
		rep(j,n) cin>>a[j];
		b.clear();rep(j,n) b.pb(a[j]);
		sort(All(b));
		rep(j,n) a[j]=(lower_bound(All(b),a[j])-b.begin());
		rep(j,n){
			pos[a[j]]=0;
			rep(k,j){
				if(a[j]<a[k]) pos[a[j]]++;
			}
		}
		rep(j,n+5) rep(k,n+5) dp[j][k]=inf;dp[0][0]=0;
		//rep(j,n) cout<<pos[j]<<endl;
		rep(j,n) rep(k,j+1){
			//int l=j-k,r=n-k-1;
			//cout<<j<<' '<<k<<' '<<dp[j][k]<<endl;
			//cout<<l<<' '<<r<<' '<<abs(pos[j]-l)<<' '<<abs(pos[j]-r)<<endl;
			int len=n-j-1;
			dp[j+1][k]=min(dp[j+1][k],dp[j][k]+pos[j]);
			dp[j+1][k+1]=min(dp[j+1][k+1],dp[j][k]+abs(len-pos[j]));
		}
		int ret=inf;
		rep(j,n+1) ret=min(ret,dp[n][j]);
		printf("Case #%d: %d\n",i+1,ret);
	}
}
