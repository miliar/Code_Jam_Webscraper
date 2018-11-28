#include<iostream>
#include<cstdio>
#include<string.h>
#include<string>
#include<math.h>
#include<algorithm>
#include<map>
using namespace std;

typedef long long ll;
map<ll,ll> mp;
int num[200];

int pal(ll x){
    int len = 0;
    while(x){
        num[len++] = x%10;
        x/=10;
    }
    for(int i=0,j=len-1;j>i;i++,j--){
        if(num[i]!=num[j]) return 0;
    }
    return 1;
}

int main(){
    ll cur = 0;
    for(ll i=0;i<=10000000;i++){
        if(pal(i)&&pal(i*i)){
            if(i*i>9&&i*i<=120) cout << "i: " << i << endl;
            mp[i*i] = ++cur;
        }
    }
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        ll l,r;
        scanf("%lld %lld",&l,&r);
        ll x = (mp.upper_bound(l-1)--)->second;
        ll y = (mp.upper_bound(r)--)->second;
        printf("Case #%d: %lld\n",cas,y - x);
    }
    return 0;
}
