/* ***********************************************
Author        :yby
Created Time  :2016年04月09日 星期六 09时57分08秒
File Name     :c.cpp
************************************************ */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <sstream>
#include <map>
#include <string>
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
#define foreach(i,a) for(int i=head[a];i>=0;i=ee[i].next)
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
#define sqr(x) ((x)*(x))
#define C1(x) cout<<x<<endl
#define C2(x,y) cout<<x<<" "<<y<<endl
#define C3(x,y,z) cout<<x<<" "<<y<<" "<<z<<endl
typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< pair<int,int> > VPII;
const ll mod=1e9+7;
const ll maxn=1e5+7;
const ll maxe=1e6+7;
const ll INF=2e8+7;
const double PI=acos(-1);
int dx[4]={0,0,1,-1};
int dy[4]={-1,1,0,0};
int T;
int n,m;
int isp[INF];
VI v;
ll vv[15][20];
vector<ll> vl;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    m0(isp);
    m0(vv);
    rep(i,15)
    vv[i][0]=1;
    rep(i,15)
    {
    	if(i>=2)
		REP(j,16)
		vv[i][j]=vv[i][j-1]*i;
	}
    for(ll i=2;i<INF;i++)
	{
		if(!isp[i]){
			v.pb(i);
		for(ll j=i*i;j<INF;j+=i)
		{
			isp[j]=1;
		}
		}
	}
    cin>>T;
    REP(ca,T)
    {
    	cin>>n>>m;
    	int nu=0;
		printf("Case #%d:\n",ca);
		for(ll i=0;i<(1LL<<(n-2));i++){
			vl.clear();
			int oo=1;
			for(ll j=2;j<=10;j++)
			{
				ll now=1LL+vv[j][n-1];
				rep(k,n-2)
				{
					if((i>>k)%2==1)now+=vv[j][k+1];
				}
				int ok=0;

				rep(k,SZ(v))
				{
					ll z=v[k];
					if(z*z>now)break;
					if(now%z==0){
						vl.pb(z);
						ok=1;
						break;
					}
				}
				if(!ok){

				oo=0;break;
				}
			}
			if(oo){
				nu++;
				printf("1");
				per(k,n-2,0)
				{
					if((i>>k)%2==1)printf("1");
					else printf("0");
				}
				printf("1");
				rep(i,SZ(vl))
				printf(" %lld",vl[i]);
				printf("\n");
			}
			if(nu==m)break;
		}
	}
    return 0;
}
