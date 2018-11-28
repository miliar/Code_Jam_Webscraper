/* ***********************************************
Author        :yby
Created Time  :2016年05月28日 星期六 22时14分41秒
File Name     :b.cpp
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
double p[205];
int zz[16];
int gg[16];
double dp[17][18][18];
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
   	cin>>T;
   	REP(ca,T)
   	{
   		printf("Case #%d: ",ca);
		int n,k;
		cin>>n>>k;
		rep(i,n)scanf("%lf",&p[i]);
		m0(zz);
		for(int i=n-k;i<n;i++)zz[i]=1;
		double ans=0;
		do{
			m0(dp);
			dp[0][0][9]=1;
			int tol=0;
			rep(i,n)if(zz[i])gg[tol++]=i;
			rep(i,k)		
			{
				rep(j,i+1)
				{
					rep(t,18)
					{
						if(dp[i][j][t]!=-1)
						{
							if(t+1<18)
							dp[i+1][j+1][t+1]+=dp[i][j][t]*p[gg[i]];
							if(t-1>=0)
							dp[i+1][j][t-1]+=dp[i][j][t]*(1.0-p[gg[i]]);
						}
					}
				}
			}
			ans=max(ans,dp[k][k/2][9]);
		}
		while(next_permutation(zz,zz+n));
		printf("%.9lf\n",ans);
	}
    return 0;
}
