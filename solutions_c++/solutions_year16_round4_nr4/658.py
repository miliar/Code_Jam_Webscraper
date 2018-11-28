#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cassert>
#include <map>
#include <string>
#include <iomanip>
#include <set>
#include <queue>
#include <ctime>
#include <vector>
using namespace std;

#define FOR(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define sz(v) (int)(v).size()
#define mp make_pair
#define all(v) (v).begin(), (v).end()
typedef double LD;
//typedef long long LL;

const int N = 4;
int n, G[N][N];
int C[N][N];
char st[N+7];
int a_ptr, a[N];
int b_ptr, b[N];
int perm[N];

bool can(int m) {
    FOR(i, n) FOR(j, n) {
        C[i][j] = (m >> (i * n + j)) & 1;
    }
    FOR(i, n) {
        bool ones = true;
        FOR(j, n) {
            if (C[i][j] == 0) ones=false;
        }
        if (ones) continue;
        a_ptr = 0;
        b_ptr = 0;
        FOR(j, n) {
            if (C[i][j]) a[a_ptr++] = j;
        }
        FOR(j, n) {
            if (i != j) b[b_ptr++] = j;
        }
        FOR(j, n-1) perm[j]=j;
        do {
            bool ok = true;
            FOR(j, a_ptr) {
                int u=b[perm[j]];
                if (C[u][a[j]] == 0) ok = false;
            }
            if (ok) return true;
        } while(next_permutation(perm, perm+n-1));
    }
    return false;
}

void solve() {
    
    int T;
    //scanf("%d", &T);
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cin >> n;
        FOR(i, n) {
            cin >> st;
            FOR(j, n) G[i][j] = st[j] - '0';
        }
        int ans = n * n;
        FOR(mask, 1 << (n * n)) {
            bool ok = true;
            int cnt = 0;
            FOR(i, n) FOR(j, n) {
                int u = i * n + j;
                if (G[i][j] && ((mask >> u) & 1) == 0) ok = false;
                if (!G[i][j] && ((mask >> u) & 1) == 1) ++cnt;
            }
            if (ok && !can(mask)) {
                ans = min(ans, cnt);
            }
        }
        cout << "Case #" << test << ": " << ans << endl;
    }
}

void testgen() {
    FILE *f = fopen("input.txt", "w");
    srand(time(0));
    fclose(f);
}

int  main(int argc, char* argv[]) {
#ifdef harhro94
    //testgen();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    #define task "estimate"
    //freopen(task".in", "r", stdin);
    //freopen(task".out", "w", stdout);
#endif

    solve();

#ifdef harhro94
    cerr << "\ntime = " << clock() / 1000.0 << endl;
#endif
    return 0;
}