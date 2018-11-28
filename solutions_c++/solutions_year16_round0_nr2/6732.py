#include <iostream>
#include <algorithm>

using namespace std;

void solve(int test) {
    cout << "Case #" << test << ": ";
    string s; cin >> s;

    cerr << "s: " << s << endl;

    int ans = 0;
    for (int i = int(s.size()) - 1; i>=0; --i) {
        if (s[i] == '-') {
            if (i == 0) {
                s[0] = '+';
                ++ans;
            } else {
                int frontlen = 0;
                for (int u=0; u<int(s.size()); ++u) {
                    if (s[u] == '-')
                        break;
                    ++frontlen;
                }

                cerr << "frontlen: " << frontlen << endl;
                if (frontlen) {
                    ++ans;
                    for (int u=0; u<frontlen; ++u)
                        s[u] = '-';
                }

                cerr << "after front: " << s << endl;

                if (s[i] == '-') {
                    ++ans;
                    reverse(s.begin(), s.begin() + i + 1);
                    for (int u=0; u<=i; ++u) {
                        if (s[u] == '-') s[u] = '+';
                        else s[u] = '-';
                    }
                }
            }
        }
        cerr << "iter " << i << ": " << s << endl;
    }

    cout << ans << endl;
}

int main() {
    int t; cin >> t;
    for (int e=0; e<t; ++e)
        solve(e + 1);
}
