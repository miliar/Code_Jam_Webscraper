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


const int N = 207;  
int n, k;
LD p[N];
LD bf_ans[1 << 16];

void go(int ptr, int cnt, int z, int mask, LD prob) {
    if (ptr == n) {
        if (cnt == 0 && z == k) {
            int new_mask = 0;
            FOR(i, n) {
                int r = mask % 3;
                mask /= 3;
                if (r > 0) new_mask |= (1 << i);
            }
            bf_ans[new_mask] += prob;
        } 
        return;
    }
    go(ptr + 1, cnt, z, mask * 3, prob);
    go(ptr + 1, cnt + 1, z + 1, mask * 3 + 1, prob * p[ptr]);
    go(ptr + 1, cnt - 1, z + 1, mask * 3 + 2, prob * (1 - p[ptr]));
}

LD brute_force() {
    FOR(i, 1 << n) bf_ans[i] = 0;
    go(0, 0, 0, 0, 1);
    LD ans = 0;
    FOR(i, 1 << n) {
        ans = max(bf_ans[i], ans);
    }
    return ans;
}

void solve() {
    
    int T;
    //scanf("%d", &T);
    cin >> T;
    for (int test = 1; test <= T; ++test) {

        cerr << test << endl;

        cin >> n >> k;
        FOR(i, n) cin >> p[i];
        cout << "Case #" << test << ": ";

        cout << fixed << setprecision(9) << brute_force() << endl; 
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