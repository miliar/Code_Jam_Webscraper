#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int tt, n, m;
int par[155];
vector<int> ch[155];
string s[5];
char buf[155];
int q[155], qc;
double prob[155];
int sz[155];
string a;

mt19937 mt(123);
uniform_real_distribution<double> uniReal(0.0, 1.0);

int pre[333];

bool kmp(string s, int need) {
    int n = (int)s.length();
    for (int i = 1; i < n; ++i) {
        int j = pre[i - 1];
        while (j && s[i] != s[j]) {
            j = pre[j - 1];
        }
        if (s[i] == s[j]) {
            ++j;
        }
        if (j == need) {
            return true;
        }
        pre[i] = j;
    }
    return false;
}

void dfs(int v) {
    sz[v] = 1;
    for (int to : ch[v]) {
        dfs(to);
        sz[v] += sz[to];
    }
}

double c[105][105];

int main() {
    REP(i, 105) c[0][i] = 0;
    c[0][0] = 1;
    for (int i = 1; i < 105; ++i) {
        c[i][0] = 1;
        for (int j = 1; j < 105; ++j) {
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
        }
    }
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tt);
    for (int test = 1; test <= tt; ++test) {
        printf("Case #%d:", test);
        scanf("%d", &n);
        REP(i, n) par[i] = -1;
        REP(i, n) ch[i].clear();
        REP(i, n) {
            int p;
            scanf("%d", &p), --p;
            par[i] = p;
            if (p >= 0) {
                ch[p].pb(i);
            }
        }
        REP(i, n) sz[i] = 0;
        REP(i, n) if (sz[i] == 0) {
            dfs(i);
        }
        scanf("%s", buf);
        a = string(buf);
        scanf("%d", &m);
        REP(i, m) {
            scanf("%s", buf);
            s[i] = string(buf);
            cerr << s[i] << ' ';
        }
        cerr << endl;
        int all = 0, ok[m];
        REP(i, m) ok[i] = 0;
        string res;
        while (clock() <= 1000 * test) {
            REP(times, 1000) {
                res.clear();
                qc = 0;
                REP(i, n) if (par[i] == -1) {
                    q[qc++] = i;
                }
                while (qc) {
                    int tot = 0;
                    REP(i, qc) tot += sz[q[i]];
                    REP(i, qc) {
                        int v = q[i];
                        double num = 1, denom = c[tot][sz[v]];
                        int rem = tot - sz[v];
                        int chtot = 0;
                        for (int x : ch[v]) {
                            chtot += sz[x];
                            if (chtot != sz[x]) {
                                denom *= c[chtot][sz[x]];
                            }
                            num *= c[rem + chtot][sz[x]];
                        }
                        prob[i] = num / denom;
                    }
                    double sumProb = 0;
                    REP(i, qc) sumProb += prob[i];
                    REP(i, qc) prob[i] /= sumProb;
                    double re = uniReal(mt);
                    int cur = 0;
                    while (cur < qc && re >= prob[cur]) {
                        re -= prob[cur];
                        ++cur;
                    }
                    res += a[q[cur]];
                    --qc;
                    int rem = q[cur];
                    for (int i = cur; i < qc; ++i) {
                        q[i] = q[i + 1];
                    }
                    for (int x : ch[rem]) {
                        q[qc++] = x;
                    }
                }
                REP(i, m) {
                    if (kmp(s[i] + string(1, '#') + res, (int)s[i].length())) {
                        ++ok[i];
                    }
                }
                ++all;
            }
        }
        REP(i, m) printf(" %.12f", (double)ok[i] / all);
        printf("\n");
        cerr << "done " << test << ", iters = " << all << endl;
    }
    return 0;
}
