#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<set>
using namespace std;

#define rep(i, s, t) for (int i = (s); i <= (t); ++i)
#define REP(i, n) rep(i, 1, n)
typedef double LD;
set<LD> S;
int n;
LD a[1111], b[1111];

int solve(){
    int ret = 0;
    S.clear();
    REP(i, n) S.insert(a[i]);
    REP(i, n){
        LD v = b[i];
        set<LD>::iterator tmp = S.lower_bound(v);
        if (tmp != S.end()) ret++, S.erase(tmp);
        else S.erase(S.begin());
    }
    return ret;
}

void Excalibur(int ca){
    scanf("%d", &n);
    REP(i, n) scanf("%lf", &a[i]);
    REP(i, n) scanf("%lf", &b[i]);
    int ans1 = solve();
    REP(i, n) swap(a[i], b[i]);
    int ans2 = solve();
    printf("Case #%d: ", ca);
    printf("%d %d\n", ans1, n - ans2);
}

int main(){
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout); 
    int Ti;
    scanf("%d", &Ti);
    REP(z, Ti) Excalibur(z);
}
