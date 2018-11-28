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
typedef pair<double,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
double dp[1919];
bool sumi[1919];
double d[1919][1919];
int x[1919],y[1919],z[1919];
priority_queue<pint> q;
double sq(double a){return a*a;}
void aedge(double x,int y){
	if(dp[y]-1e-8>x){
		dp[y]=x;q.push(mp(-x,y));
	}
}
int main()
{
	int t,n,s;
	double inf=1e9;
	cin>>t;
	rep(i,t){
		cin>>n>>s;
		rep(j,n) cin>>x[j]>>y[j]>>z[j]>>s>>s>>s;
		rep(j,n) rep(k,n) d[j][k]=sqrt(sq(x[j]-x[k])+sq(y[j]-y[k])+sq(z[j]-z[k]));
		rep(j,1919) dp[j]=inf;memset(sumi,false,sizeof(sumi));
		aedge(0,0);
		while(!q.empty()){
			pint p=q.top();q.pop();
			double x=-p.fi;int y=p.se;
			if(sumi[y]) continue;sumi[y]=true;
			rep(j,n) aedge(max(x,d[y][j]),j);
		}
		printf("Case #%d: %.12f\n",i+1,dp[1]);
	}
}
