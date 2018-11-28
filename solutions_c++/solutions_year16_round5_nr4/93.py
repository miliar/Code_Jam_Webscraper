#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int tt, n, len;
string g[100];
string b;
char buf[55];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (int test = 1; test <= tt; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d", &n, &len);
        bool ok = true;
        REP(i, n) {
            scanf("%s", buf);
            g[i] = string(buf);
            bool all = true;
            REP(j, len) if (g[i][j] != '1') {
                all = false;
            }
            if (all) ok = false;
        }
        scanf("%s", buf);
        b = string(buf);
        //REP(i, len) assert(b[i] == '1');
        if (!ok) {
            printf("IMPOSSIBLE\n");
            cerr << "done " << test << endl;
            continue;
        }
        string ans;
        ans += '0';
        REP(i, len - 1) ans += '?';
        printf("%s ", ans.c_str());
        ans.clear();
        REP(i, 28) {
            ans += '1';
            ans += '0';
        }
        ans += '?';
        REP(i, 28) {
            ans += '1';
            ans += '0';
        }
        printf("%s\n", ans.c_str());
        cerr << "done " << test << endl;
    }
    return 0;
}
