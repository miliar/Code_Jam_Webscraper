#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <algorithm>
using namespace std;

int nodes[111][26];
int calc(const vector <string> &sets) {
    int cnt = 1;
    for (int i = 0; i < 26; i++) {
        nodes[0][i] = -1;
    }
    for (int i = 0; i < (int)sets.size(); i++) {
        string s = sets[i];
        int v = 0;
        for (int j = 0; j < (int)s.size(); j++) {
            int c = s[j] - 'A';
            if (nodes[v][c] == -1) {
                int nv = cnt++;
                for (int j = 0; j < 26; j++) {
                    nodes[nv][j] = -1;
                }
                nodes[v][c] = nv;
            }
            v = nodes[v][c];
        }
    }
    return cnt;
}

char s[111][111];
vector <string> sets[10];
int n, m;
int ans1, ans2;
void go(int pos) {
    if (pos == m) {
        int cur = 0;
        bool ok = true;
        for (int i = 0; i < n; i++) {
            ok &= !sets[i].empty();
            cur += calc(sets[i]);
        }
        if (!ok) {
            return;
        }
        if (cur > ans1) {
            ans1 = cur;
            ans2 = 1;
        } else if (cur == ans1) {
            ans2++;
        }
        return;
    }
    for (int i = 0; i < n; i++) {
        sets[i].push_back(s[pos]);
        go(pos + 1);
        sets[i].pop_back();
    }
}

int main() {
    int nt;
    assert(scanf("%d", &nt) == 1);
    for (int tt = 1; tt <= nt; tt++) {
        assert(scanf("%d%d", &m, &n) == 2);
        for (int i = 0; i < m; i++) {
            assert(scanf("%s", s[i]) == 1);
        }
        ans1 = -1;
        ans2 = 0;
        go(0);
        printf("Case #%d: %d %d\n", tt, ans1, ans2);
    }
    return 0;
}
