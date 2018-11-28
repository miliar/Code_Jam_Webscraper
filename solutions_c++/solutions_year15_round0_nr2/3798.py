#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<cmath>
#include<stdlib.h>
#include<iomanip>
#include<list>
#include<deque>
#include<map>
#include <stdio.h>
#include <queue>
#include <stack>
#define maxn 10000+5
#define ull unsigned long long
#define ll long long
#define reP(i,n) for(i=1;i<=n;i++)
#define rep(i,n) for(i=0;i<n;i++)
#define cle(a) memset(a,0,sizeof(a))
#define mod 90001
#define PI 3.141592657
#define INF 1<<30
const ull inf = 1LL << 61;
const double eps=1e-5;

using namespace std;

bool cmp(int a,int b)
{
    return a>b;
}
//map<int,int>mp;
int n;
int a[maxn];
ll tot[maxn];
int main()
{
    #ifndef ONLINE_JUDGE
    //freopen("B-large.in","r",stdin);
    #endif
    //freopen("out.txt","w",stdout);
    int t,x,y;
    ll ans;
    cin>>t;
    for(int k=1;k<=t;k++){
		//mp.clear();
		cle(a);
		y=-INF;
		ans=INF;
		cle(tot);
		scanf("%d",&n);
		for(int i=1;i<=n;i++){
			scanf("%d",&x);
			a[x]++;
			//mp[x]++;
			y=max(x,y);
		}
		ans=y;
		for(int i=1;i<y;i++){
			if(i==1)continue;
			else{
				for(int j=i+1;j<=y;j++){
					tot[i]+=((j-1)/i*a[j]);
				}
			}
			ans=min(ans,tot[i]+i);
		}
		printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
