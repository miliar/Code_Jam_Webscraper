#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
using namespace std;

#define rep(i, s, t) for (int i = (s); i <= (t); ++i)
#define REP(i, n) rep(i, 1, n)
#define MOD 1000000007
typedef long long LL;
typedef double LD;

LD C, F, X;

LD calc(int k){
    LD res = 0;
    rep(i, 0, k - 1) res += C / (2 + i * F);
    res += X / (k * F + 2);
    return res;
}

void Excalibur(int ca){
    scanf("%lf%lf%lf", &C, &F, &X);
    int r = X / C, l = 0;
    while (l + 1 < r){
        int mid = (l + r) >> 1;
        if (calc(mid) < calc(mid + 1))
            r = mid;
        else l = mid;
    }
    printf("Case #%d: ", ca);
    printf("%.10f\n", min(calc(0), calc(r)));
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int Ti;
    scanf("%d", &Ti);
    REP(z, Ti) Excalibur(z);
}
