/* ***********************************************
Author        :yby
Created Time  :2016年05月28日 星期六 22时42分04秒
File Name     :aa.cpp
************************************************ */

#include <cstdio>
#include <cstring>
#include <stack>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <sstream>
#include <map>
#include <string>
#include <bitset>
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include <queue>
#include <utility>
using namespace std;
#define repp(i,a,b) for(int i=a;i<=b;i++)
#define rep(i,a) for(int i=0;i<a;i++)
#define REP(i,a) for(int i=1;i<=a;i++)
#define per(i,a,b) for(int i=a-1;i>=b;i--)
#define foreach(i,a) for(int i=head[a];i>=0;i=e[i].next)
#define Foreach(i,a) for(__typeof((a).begin())i=(a).begin();i!=(a).end();i++)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define m0(x) memset(x,0,sizeof(x))
#define mff(x) memset(x,0xff,sizeof(x))
#define fi first
#define se second
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define SZ(x) ((int)(x).size())
#define abs(x) ((x)>0?(x):-(x))
#define sqr(x) ((x)*(x))
#define C1(x) cout<<(x)<<endl
#define C2(x,y) cout<<(x)<<" "<<(y)<<endl
#define C3(x,y,z) cout<<(x)<<" "<<(y)<<" "<<(z)<<endl
typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<int,pair<int,int> > PIII;
typedef vector< pair<int,int> > VPII;
const ll mod=1e9+7;
const ll maxn=1e5+7;
const ll maxe=1e6+7;
const ll INF=1e9+7;
const double eps=1e-8;
int dx[4]={0,0,1,-1};
int dy[4]={-1,1,0,0};
int T;
char s[3]={
	'P','R','S'
};
int ans=0;
bool dfs(int r,int p,int s)
{
	int gg=(r+p+s);
	if(gg%4==1){
		if(r==1)ans=1;
		if(p==1)ans=0;
		if(s==1)ans=2;
		return true;
	}
	if(gg%4==2){
		if(r==2||p==2||s==2)return false;
		if(r==1&&p==1)ans=0;
		if(r==1&&s==1)ans=1;
		if(p==1&&s==1)ans=2;
		return true;
	}
	int zz=gg/4;
	int pp=r-zz;
	int rr=s-zz;
	int ss=p-zz;
	if(pp<0||ss<0||rr<0)return false;
	dfs(rr,pp,ss);
}
string res;
string dp[3][20];
bool oo[3][20];
string sol(int a,int b)
{
	if(oo[a][b])return dp[a][b];
	oo[a][b]=true;
	if(a==0){
		dp[a][b]=min(sol(a,b-1)+sol(1,b-1),sol(1,b-1)+sol(a,b-1));
	}
	if(a==1)
	{
		dp[a][b]=min(sol(a,b-1)+sol(2,b-1),sol(2,b-1)+sol(a,b-1));
	}
	if(a==2)
	{
		dp[a][b]=min(sol(a,b-1)+sol(0,b-1),sol(0,b-1)+sol(a,b-1));
	}
	return dp[a][b];
}
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   	cin>>T;
   	int n,r,p,s;

   	REP(ca,T)
   	{
   		oo[0][0]=true;
   		oo[1][0]=true;
   		oo[2][0]=true;
   		dp[0][0]="P";
   		dp[1][0]="R";
   		dp[2][0]="S";
   		printf("Case #%d: ",ca);
		cin>>n>>r>>p>>s;
		if(!dfs(r,p,s))C1("IMPOSSIBLE");
		else {
			C1(sol(ans,n));
		}

	}
    return 0;
}
