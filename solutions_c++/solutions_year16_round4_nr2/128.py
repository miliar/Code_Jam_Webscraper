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
//double dp[210][210][210];
double dp[25][25];
double p[210];
int main()
{
	int t,n,K;
	cin>>t;
	rep(i,t){
		cin>>n>>K;
		int retm=0;double ret=-1.0;
		rep(j,n) cin>>p[j];
		sort(p,p+n);
		rep(j,(1<<n)){
			if(__builtin_popcount(j)!=K) continue;
			rep(k,20) rep(l,20) dp[k][l]=0.0;dp[0][0]=1.0;
			rep(k,n){
				if((j&(1<<k))){
					rep(l,20){
						dp[k+1][l+1]+=dp[k][l]*p[k];
						dp[k+1][l]+=dp[k][l]*(1.0-p[k]);
					}
				}
				else{
					rep(l,20) dp[k+1][l]=dp[k][l];
				}
			}
			if(dp[n][K/2]>ret) ret=dp[n][K/2],retm=j;
		}
		printf("Case #%d: %.12f\n",i+1,ret);
		string s="";
		rep(j,n){
			if((retm&(1<<j))) s+='1';else s+='0';
		}
		//cout<<i<<'#'<<s<<endl;
	}
}
