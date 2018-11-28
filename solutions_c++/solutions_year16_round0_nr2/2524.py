#include <bits/stdc++.h>
using namespace std;
#define sz(v) int(v.size())

int T;

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(NULL); cin.tie(NULL);
    cin >> T;
    string s;
    for(int t = 1;t <= T; ++t) {
        cin >> s;
        int ans = 0;
        for(int i = 0;i < sz(s); ++i) {
            if(i > 0 && s[i] != s[i-1]) ans++;
        }
        if(s[sz(s) - 1] == '-') ans++;
        cout << "Case #" << t << ": " << ans << '\n';
    }
    return 0;
}
