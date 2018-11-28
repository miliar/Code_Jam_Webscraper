/*
 Created by Saidolda Bayan.
 Copyright (c) 2015 Bayan. All rights reserved.
 LANG: C++
 */
#include <bits/stdc++.h>

#define _USE_MATH_DEFINES
#define y1 lalka
#define right napravo
#define left nalevo
#define pb push_back
#define mp make_pair
#define f first
#define s second

using namespace std;
using pii = pair<int, int>;
using ll = long long;

const int INF = (int)1e9+7, mod = (int)1e9+9, pw = 31, N = (int)1e5+123, M = (int)1e6+123;
const double eps = 1e-11;
const long long inf = 1e18;

inline bool have(ll &mask, ll id){
    return mask & (1ll<<(id));
}
inline ll least(ll &mask, ll &k){
    ll res = 0, t = 1;
    for(ll i=15; i>=0; i--){
        res += have(mask, i) * t;
        t *= k;
    }
    for(ll i=2; i*i <= res; i++){
        if(res % i == 0) return i;
    }
    return 0;
}
inline bool check(ll &mask){
    vector<ll> temp;
    for(ll i=2, x; i<=10; i++){
        if(x = least(mask, i)) temp.pb(x);
        else return 0;
    }
    for(ll i=0; i<16; i++) printf("%d", have(mask, i));
    printf(" ");
    for(auto i : temp) printf("%lld ", i);
    printf("\n");
    return 1;
}
int main ()
{
    ios_base::sync_with_stdio(0);cin.tie(NULL);
    freopen("ans.txt","w",stdout);
    int cnt = 50;
    printf("Case #1:\n");
    for(ll mask = 0; cnt && mask < (1 << 16); mask++){
        if(have(mask, 0) && have(mask, 15)){
            if(check(mask)){
                cnt--;
            }
        }
    }
    
    
    
    
    return 0;
}
