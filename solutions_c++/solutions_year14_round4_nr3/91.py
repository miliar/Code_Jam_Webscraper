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
int xh[1020],yh[1020],xl[1020],yl[1020],d1[1020],d2[1020];
int dp[1020][1020];
int main()
{
	int t,w,h,b,inf=123456789;
	cin>>t;
	rep(i,t){
		cin>>w>>h>>b;
		rep(j,b){
			cin>>xl[j]>>yl[j]>>xh[j]>>yh[j];
			xh[j]++;yh[j]++;
		}
		rep(j,b+2) dp[j][j]=0;
		rep(j,b) rep(k,b){
			int dx=0,dy=0;
			if(xl[j]>xh[k]) dx=xl[j]-xh[k];if(xl[k]>xh[j]) dx=xl[k]-xh[j];
			if(yl[j]>yh[k]) dy=yl[j]-yh[k];if(yl[k]>yh[j]) dy=yl[k]-yh[j];
			dp[j][k]=max(dx,dy);
		}
		rep(j,b){
			dp[b][j]=dp[j][b]=xl[j];dp[b+1][j]=dp[j][b+1]=w-xh[j];
		}
		dp[b][b+1]=dp[b+1][b]=w;
		rep(j,1020) d1[j]=d2[j]=inf;d1[b]=0;
		rep(j,b+2){
			int n=-1;
			rep(k,b+2){
				if(d2[k]<inf) continue;
				if(n<0) n=k;else if(d1[k]<d1[n]) n=k;
			}
			d2[n]=d1[n];
			rep(k,b+2){
				d1[k]=min(d1[k],d2[n]+dp[n][k]);
			}
		}
		printf("Case #%d: %d\n",i+1,d2[b+1]);
	}
}
