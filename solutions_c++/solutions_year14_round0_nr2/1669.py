#include <bits/stdc++.h>
using namespace std;

double solve(){
    double c,f,x; cin >> c >> f >> x;
    double cps = 2.0;
    double ans = 0.0;

    while(x/cps > c/cps + x/(cps+f) ){
        ans += c/cps;
        cps += f;
    }

    return ans + x/cps;
}

int main(){
    int t; cin >> t;
    for(int tc = 1; tc <= t; tc++){
        printf("Case #%d: %.9f\n", tc, solve());
    }
}

