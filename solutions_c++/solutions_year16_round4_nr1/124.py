#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())
#define all(v) v.begin(), v.end()
#define pb push_back

void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;
    int r, p, s, n;
    cin >> n >> r >> p >> s;
    forn(w, 3) {
        vector<int> a = {w};
        forn(it, n) {
            vector<int> na;
            forv(i, a) {
                na.pb(a[i]);
                na.pb((a[i] + 1) % 3);
            }
            a = na;
        }
        vector<int> cnt(3);
        string str = "RSP";
        forv(i, a) cnt[a[i]]++;
        if (r == cnt[0] && s == cnt[1] && p == cnt[2]) {
            string res = "";
            forv(i, a) res += str[a[i]];
            
            for (int len = 1; len <= res.size() / 2; len *= 2) {
                for (int i = 0; i < res.size(); i += 2 * len) {
                    string s1 = res.substr(i, len);
                    string s2 = res.substr(i + len, len);
                    if (s1 > s2) {
                        forn(j, len) {
                            swap(res[i + j], res[i + len + j]);
                        }
                    }
                }
            }
            
            cout << res << endl;
            return;
        }
    }
    cout << "IMPOSSIBLE" << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
