/* ***********************************************
Author        :yuanzhaolin
Created Time  :2017/4/8 21:42:23
File Name     :a.cpp
************************************************ */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
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
const ll mod=(ll)1e9+7;
const ll maxn=(ll)1e5+7;
const ll maxe=(ll)1e6+7;
const ll INF=(ll)1e9+7;
const double PI=acos(-1);
int dx[4]={0,0,1,-1};
int dy[4]={-1,1,0,0};
string s;
int k,n;
int vis[maxn];
int solve()
{
	memset(vis,0,sizeof(vis));
	n=s.length()-1;
	int sum=0;
	int ans=0;
	for(int i=1;i<=n;i++)
	{
		if(i-k>=1)
		{
			sum^=vis[i-k];
		}
		if(n-i+1<k)
		{
			if(s[i]=='+'&&sum==0||s[i]=='-'&&sum==1)
				continue;
			else return INF;
		}
		if(s[i]=='+'&&sum==0||s[i]=='-'&&sum==1)
			vis[i]=0;
		else vis[i]=1;
		sum^=vis[i];
		ans+=vis[i];
	}
	return ans;
}
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin>>T;
    for(int ca=1;ca<=T;ca++)
	{
		cin>>s>>k;
		s="0"+s;
		int res=solve();
		if(res==INF)
			printf("Case #%d: %s\n",ca,"IMPOSSIBLE");
		else
			printf("Case #%d: %d\n",ca,res);

	}
    return 0;
}
