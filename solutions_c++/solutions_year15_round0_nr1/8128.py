#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output-large.out", "w", stdout);
    int t, n;
    cin >> t;
    for(int tt = 1; tt <= t; tt++){
        string s;
        int ans = 0;
        cin >> n >> s;
        ans += (s[0] - '0');
        int sum = 0;
        for(int i = 1; i <= n; i++) {
            if(ans < i && s[i] != '0'){
                sum += (i - ans);
                ans += (i - ans);
            }
            ans += (s[i] - '0');
        }
        printf("Case #%d: %d\n", tt, sum);
    }
    return 0;
}
