#include <bits/stdc++.h>
#define msg(x) cout << #x << " = " << x << endl
using namespace std;

const int maxN = 224;

int t, n;
string str[maxN];

int main() {
    freopen("a-small.txt", "w", stdout);
    cin.sync_with_stdio(0); cin.tie(0);
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> str[i];
        }
        vector<pair<int, char> > cmp[maxN];
        bool poss = true;
        int ans = 0, sz;
        for (int i = 0; i < n; i++) {
            str[i].push_back('*');
            int cnt = 1;
            for (int j = 1; j < str[i].size(); j++) {
                if (str[i][j] != str[i][j - 1]) {
                    cmp[i].push_back(make_pair(cnt, str[i][j - 1]));
                    cnt = 1;
                } else ++cnt;
            }
            if (cmp[i].size() != cmp[0].size()) {
                poss = false;
                break;
            }
            for (int j = 0; j < cmp[i].size(); j++) {
                if (cmp[i][j].second != cmp[0][j].second) {
                    poss = false;
                    break;
                }
            }
        }
        for (int i = 0; i < cmp[0].size(); i++) {
            int sum = 0;
            for (int j = 0; j < n; j++) {
                sum += cmp[j][i].first;
            }
            sum /= n;
            for (int j = 0; j < n; j++) {
                ans += abs(sum - cmp[j][i].first);
            }
        }
        cout << "Case #" << tc << ": ";
        if (!poss) cout << "Fegla Won\n";
        else cout << ans << "\n";
    }
    return 0;
}
