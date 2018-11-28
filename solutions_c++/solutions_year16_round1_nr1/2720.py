#include <bits/stdc++.h>
using namespace std;

int main() {
    //freopen("a.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    long long T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        cout << "Case #" << t << ": ";
        string s, c;
        cin >> s;
        c += s[0];
        for (int i=1; i<s.size(); ++i) {
            if (c[0] > s[i])
                c = c + s[i];
            else
                c = s[i] + c;
        }
        cout << c << "\n";
    }
    return 0;
}
