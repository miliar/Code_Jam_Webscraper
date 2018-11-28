#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>
#include <deque>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define fn(n,i) for(int i = 0; i < (n); i++)
#define fv(v,i) for(int i = 0; i < ((int) (v).size()); i++)
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define sqrt(x) sqrt(abs(x))
#define fill(x,y) memset(x,y,sizeof(x))

#define PROBLEM "A-large"

namespace a_small {

    typedef vector<int> vi;
    typedef long long ll;
    typedef long double ld;
    typedef pair<int, int> ii;
    typedef vector<ii> vii;
    typedef vector<string> vs;
    typedef vector<vi> vvi;

    template<class T> T abs(T x) { return x > 0 ? x : -x; }

    char m[128][128];
    bool L[128][128], R[128][128], U[128][128], D[128][128];

    void solve() {
        int r, c;
        fill(m, 0);
        cin >> r >> c;
        string s;
        fn(r,i) {
            cin >> s;
            fv(s,j) {
                m[i][j] = s[j];
            }
        }
        fn(r,i) {
            bool right = true, left = true;
            fn(c,j) {
                L[i][j] = left;
                R[i][c-j-1] = right;
                left = left && (m[i][j] == '.');
                right = right && (m[i][c-j-1] == '.');
            }
        }
        fn(c,j) {
            bool up = true, down = true;
            fn(r,i) {
                U[i][j] = up;
                D[r-i-1][j] = down;
                up = up && (m[i][j] == '.');
                down = down && (m[r-i-1][j] == '.');
            }
        }

        int ans = 0;
        fn(r,i) fn(c,j) {
            if (L[i][j] && R[i][j] && U[i][j] && D[i][j] && (m[i][j] != '.')) {
                cout << "IMPOSSIBLE";
                return;
            }
            if (L[i][j] && (m[i][j] == '<') ||
                R[i][j] && (m[i][j] == '>') ||
                U[i][j] && (m[i][j] == '^') ||
                D[i][j] && (m[i][j] == 'v'))
                ++ans;
        }
        cout << ans;
    }

    int main() {
        freopen(PROBLEM ".in", "r", stdin);
        freopen(PROBLEM ".out", "w", stdout);

        int T;
        cin >> T;
        for (int t = 1; t <= T; ++t) {
            double start = (double)clock() / CLOCKS_PER_SEC;

            cout << "Case #" << t << ": ";
            solve();
            cout << endl;

            double end = (double)clock() / CLOCKS_PER_SEC;
            fprintf(stderr, "Solved %d / %d.\t Time: %.2f\t Total: %.2f\t Avg: %.2f\n", t, T, end-start, end, end / t);
        }

        return 0;
    }

};

int main() {
    return a_small::main();
}
