#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int nmax = 150005;
const long double PI = acos(-1.0);
const ll mod = 1e9 + 7;
const long double eps = 1e-6;
set<int> s;
void er(ll n){
    while(n){
        int md = n % 10;
        s.erase(md);
        n /= 10;
    }
}
int main(){
    //ios_base::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ll t;
    scanf("%I64d", &t);
    for(int q = 1; q <= t; ++q){
        ll n;
        s.clear();
        scanf("%I64d", &n);
        if (!n){
            printf("Case #%d: INSOMNIA\n", q);
            continue;
        }
        for(int i = 0; i < 10; ++i) s.insert(i);
        er(n);
        ll cnt = n;
        while(!s.empty()){
            n += cnt;
            er(n);
        }
        printf("Case #%d: %I64d\n", q, n);
    }
    return 0;
}
