#include <algorithm>
#include <bitset>
#include <cctype>
#include <cfloat>
#include <climits>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unistd.h>
#include <utility>
#include <vector>
#include <omp.h>

using namespace std;
typedef long long ll;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getc_str(char str[]) { unsigned int c, n = 0; while ((c = gc()) <= ' '); if (!~c) exit(0); do { str[n++] = c; } while ((c = gc()) > ' ' ); str[n] = '\0'; return n; }

const int TC = 100;        // number of test cases
const int THREAD = 4;      // number of thread

struct Input {
    int n;
    int m;
    vector<string> vs;
    void operator()() {
        int i, j;
        m = getint(), n = getint();
        for (i = 0; i < m; i++) {
            string s; cin >> s;
            vs.push_back(s);
        }
    }
};

struct Result {
    int res, cnt;
    void operator()(int tc) {
        printf("Case #%d: ", tc + 1);
        printf("%d %d\n", res, cnt);
    }
};

struct Case {
    int n, m;
    vector<string> vs;
    int nodes[1 << 8];
    const static int M = 1000000007;

    int solve(int h) {
        set<string> st;
        for (int i = 0; i < m; i++) if (h >> i & 1) {
            int len = vs[i].size();
            for (int j = 1; j <= len; j++) {
                st.insert(vs[i].substr(0, j));
            }
        }
        if (h) st.insert("");
        return st.size();
    }

    int res, cnt;

    void dfs(int pos, vector<int>& to) {

        if (pos == m) {
            // for (int i = 0; i < to.size(); i++) cout << to[i] << ' '; puts("");
            vector<int> vs(n);
            for (int i = 0; i < to.size(); i++) {
                vs[to[i]] += 1 << i;
            }
            int tmp = 0;
            for (int i = 0; i < vs.size(); i++) tmp += nodes[vs[i]];
            if (res < tmp) {
                res = tmp, cnt = 1;
            } else if (res == tmp) cnt++;
            return;
        }

        for (int i = 0; i < n; i++) {
            to[pos] = i;
            dfs(pos + 1, to);
        }
    }


    void main(Input* in, Result *out, int test_case) {
        int i, j;
        n = in->n, m = in->m;
        vs.clear();
        for (i = 0; i < m; i++) vs.push_back(in->vs[i]);

        memset(nodes, ~0, sizeof(nodes));

        for (int h = 0; h < 1 << m; h++) {
            nodes[h] = solve(h);
            // cout << bitset<4>(h) << ' ' << nodes[h] << endl;
        }

        vector<int> to(m);

        res = -1, cnt = 0;

        dfs(0, to);

        out->res = res;
        out->cnt = cnt;

        fprintf(stderr, "-->%d done at %d.\n", test_case, omp_get_thread_num());
    }
};

Input in[TC];
Result out[TC];
Case s[THREAD];

int main () {
    int i, t = getint();
    omp_set_num_threads(THREAD);
    for (i = 0; i < t; i++) in[i]();
#pragma omp parallel for schedule(dynamic, 1)
    for (i = 0; i < t; i++) s[omp_get_thread_num()].main(in + i, out + i, i);
    // for (i = 0; i < t; i++) s[0].main(in + i, out + i, i);
    for (i = 0; i < t; i++) out[i](i);
    return 0;
}
