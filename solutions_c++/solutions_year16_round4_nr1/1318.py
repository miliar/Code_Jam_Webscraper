/*
 * Author:heroming
 * File:heroming.cpp
 * Time:2016/5/28 21:34:56
 */
#include <vector>
#include <list>
#include <set>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
using namespace std;

#define px first
#define py second
#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(), (v).end()
#define clr(v, e) memset(v, e, sizeof(v))
#define rep(it, v) for (auto it : v)
#define forn(i, n) for (int i = 0; i < (n); ++ i)
#define rforn(i, n) for (int i = (n) - 1; i >= 0; -- i)
#define form(i, a, b) for (int i = (a); i <= (b); ++ i)
#define rform(i, a, b) for (int i = (b); i >= (a); -- i)
#define forv(i, v) for (int i = 0; i < sz(v); ++ i)
#define iter(it, v) for (auto it = v.begin(); it != v.end(); ++ it)

typedef long long lint;
typedef vector<int> vint;
typedef vector<string> vstring;
typedef pair<int, int> pint;
typedef vector<lint> vlint;
typedef vector<pint> vpint;

const int maxm = 256;
const int maxn = 10000;

int T, N, R, P, S;
int cnt[maxm];
char op[maxm];
char s[maxn], t[maxn];
string ans;

string dfs(const int l, const int r) {
    if (l == r) {
        string ret = "0";
        ret[0] = t[l];
        return ret;
    }
    int m = (l + r) >> 1;
    string a = dfs(l, m);
    string b = dfs(m + 1, r);
    string ab = a + b;
    string ba = b + a;
    return min(ab, ba);
}

int main() {
    freopen("heroming.out", "w", stdout);
    scanf("%d", &T);
    op['R'] = 'S', op['P'] = 'R', op['S'] = 'P';
    form (cas, 1, T) {
        printf("Case #%d: ", cas);
        scanf("%d%d%d%d", &N, &R, &P, &S);
        vint v{R, P, S};
        sort(all(v));
        clr(cnt, 0);

        char c[3] = {'R', 'P', 'S'};
        bool finish = 0;
        ans = "";
        forn (x, 3) {
            cnt['R'] = R;
            cnt['P'] = P;
            cnt['S'] = S;
            if (cnt[c[x]] == 0) continue;
            clr(t, 0);
            t[0] = c[x];
            -- cnt[t[0]];

            bool flag = 1;
            for (int bit = 0; bit < N && flag; ++ bit) {
                for (int i = 0; i < (1 << bit); ++ i) {
                    s[i] = t[i];
                }
                for (int i = 0; i < (1 << bit); ++ i) {
                    t[i << 1] = min(s[i], op[s[i]]);
                    t[i << 1 | 1] = max(s[i], op[s[i]]);
                    if (-- cnt[op[s[i]]] < 0) {
                        flag = 0;
                        break;
                    }
                }
            }
            if (flag) {
                finish = 1;
                if (sz(ans) == 0) {
                    ans = dfs(0, (1 << N) - 1);
                } else {
                    ans = min(ans, dfs(0, (1 << N) - 1));
                }
            }

        }
        if (finish) {
            printf("%s\n", ans.c_str());
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
