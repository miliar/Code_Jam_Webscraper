#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    long long T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        cout << "Case #" << t << ": ";
        string s;
        cin >> s;
        vector<int> V(s.size());
        for (int i=0; i<s.size(); ++i)
            V[s.size()-i-1] = (s[i] == '+') ? 1 : 0;
        int ans=0;
        for (int i=0; i<s.size(); ++i) {
            if (!V[i]) {
                ans++;
                for (int j=i; j<s.size(); ++j)
                    V[j] ^= 1;
            }
        }
        cout << ans << "\n";
    }

    return 0;
}
