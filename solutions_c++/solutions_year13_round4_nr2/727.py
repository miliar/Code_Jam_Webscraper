#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <string.h>
#include <queue>
#include <map>
#include <set>
#include <math.h>
#include <sstream>
using namespace std;

typedef long long ll;
const double pi = acos(-1.0);
const double eps = 1e-8;

const int dx[8]={1,0,-1,0,-1,-1,1,1};
const int dy[8]={0,1,0,-1,1,-1,1,-1};
const int days[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
const int leap[13]={0,31,29,31,30,31,30,31,31,30,31,30,31};

ll n,p;

bool check1(ll small,ll now,int v){
    if (v==n) return now<=p;
    if (!small) return check1(small,now*2LL+0,v+1);
    return check1((small-1)/2,now*2LL+1,v+1);
}

bool check2(ll small,ll now,int v){
    if (v==n) return now<=p;
    if (!small) return check2(small,now*2LL+0,v+1);
    ll l=small;
    ll b=(1LL<<(n-v))-1-l;
    if (!b)return check2(l/2,now*2LL+1,v+1);
    b--;
    return check2((l+1)/2,now*2LL+0,v+1);
}

int main(){
    int _,cas=0;
    scanf("%d",&_);
    while (_--){
        scanf("%lld%lld",&n,&p);
        p--;
        ll ans1,ans2;
        ll l=0,r=1ll<<n;
        while (l<r-1){
            ll mid=(l+r)>>1;
            if (check1(mid,0,0)) l=mid;
            else r=mid;
        }
        ans1=l;
        l=0,r=1ll<<n;
        while (l<r-1){
            ll mid=(l+r)>>1;
            if (check2(mid,0,0)) l=mid;
            else r=mid;
        }
        ans2=l;        
        printf("Case #%d: %lld %lld\n",++cas,ans1,ans2);
    }
    return 0;
}
