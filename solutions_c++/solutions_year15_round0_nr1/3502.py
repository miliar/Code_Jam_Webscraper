#include <bits/stdc++.h>
using namespace std;

#define sd(x) scanf("%lld", &x)
#define LL long long

inline void Solve(){
    LL n;
    sd(n);
    string s;
    cin>>s;
    LL till = s[0] - '0', ans = 0;
    for(LL i = 1; i <= n; i++){
        if(till < i){
            ans += (i - till);
            till = i;
        }
        till += (s[i] - '0');
    }
    printf("%lld\n", ans);
    return;
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    LL t, tt = 0;
    sd(t);
    while(t--){
        printf("Case #%lld: ", ++tt);
        Solve();
    }
    return 0;
}
