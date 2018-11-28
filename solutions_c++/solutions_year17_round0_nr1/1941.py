#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for(int I = 1; I <= t; I++){
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        int i;
        for(i = 0; i + k - 1 < s.size(); i++) {
            if(s[i] == '-') {
                ans++;
                for(int j = i; j < i+k; j++) {
                    if(s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
            }
        }
        for(i; i < s.size(); i++) {
            if(s[i] == '-') {
                ans = -1;
                break;
            }
        }
        printf("Case #%d: ", I);
        if(ans == -1) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << "\n";
        }
    }
    return 0;
}
