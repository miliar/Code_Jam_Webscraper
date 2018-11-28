#include <set>
#include <map>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100000;

int T, n, a[N];
char str[N];
bool vis[N];
vector <int> g[N];

int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        int ret = N;
        map <string, int> mp;
        scanf("%d", &n);
        gets(str);
        for (int i = 0; i < n; i++) {
            gets(str);
            int m = strlen(str);
            g[i].clear();
            for (int j = 0; j < m;) {
                int k = j;
                string s = "";
                while (str[k] == ' ')
                    ++k;
                while ('a' <= str[k] && str[k] <= 'z') {
                    s += str[k];
                    ++k;
                }
                j = k;
                if ((int) s.size() > 0) {
                    int len = mp.size();
                    if (mp.count(s) == 0) {
                        mp[s] = len;
                    }
                    g[i].push_back(mp[s]);
                }
            }
        }
        int len = mp.size();
        for (int i = 0, r = n - 2; i < (1 << r); i++) {
            a[0] = 0;
            a[1] = 1;
            for (int j = 0; j < r; j++) {
                a[j + 2] = min(1, i & (1 << j));
            }
            for (int j = 0; j < len; j++) {
                vis[j] = false;
            }
            for (int j = 0; j < n; j++) {
                if (a[j] == 0) {
                    for (int k = 0; k < (int) g[j].size(); k++) {
                        vis[g[j][k]] = true;
                    }
                }
            }
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (a[j] == 1) {
                    for (int k = 0; k < (int) g[j].size(); k++) {
                        if (vis[g[j][k]]) {
                            ++cnt;
                            vis[g[j][k]] = false;
                        }
                    }
                }
            }
            ret = min(ret, cnt);
        }
        printf("Case #%d: %d\n", t, ret);
    }

    return 0;

}
