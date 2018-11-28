#include <iostream>
#include <sstream>
#include <vector>
#include <windows.h>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <map>
#include <set>
#include <cmath>

using namespace std;

#define pb push_back
#define mp make_pair
#define INF 1000000000
#define y1 tratatatatatatata

const int MOD = 1000000007;


void solve(){
    double C, F, X, ans, now, ret;
    cin >> C >> F >> X;
    now = 2;
    ans = X / 2.0;
    ret = 0;
    for (int i = 1; i <= 10000000; ++i) {
        ret += C / now;
        now = now + F;
        if (ret + X / now < ans) ans = ret + X / now;
    }
    printf("%.9f\n", ans);
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
