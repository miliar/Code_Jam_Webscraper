#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll t, i, n, ans, cnt, j, k;
string s;
int main() {
    cin>>t;
    for(ll _t = 1; _t <= t; _t++) {
        cin>>s>>k;
        n = s.length();
        ans = 1;
        cnt = 0;
        for(i = 0; i < n-k+1; i++) {
            if(s[i] == '+') continue;
            cnt++;
            for(j = i; j < i+k; j++) {
                if(s[j] == '-') s[j] = '+';
                else s[j] = '-';
            }
        }
        for(; i < n; i++) {
            if(s[i] == '-') ans = 0;
        }
        if(!ans) {
            printf("Case #%lld: IMPOSSIBLE\n", _t);
        }
        else {
            printf("Case #%lld: %lld\n", _t, cnt);
        }

    }

    return 0;
}
