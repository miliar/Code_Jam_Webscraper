#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <bitset>
#include <vector>
#include <string>
#include <cstdio>
#include <string>
#include <fstream>
#include <sstream>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define PB push_back
#define SIZE(x) (int)x.size()
#define MP(x, y) make_pair(x, y)
#define ALL(t) (t).begin(),(t).end()
#define CLR(x, y) memset(x, y, sizeof(x))
#define FOR(i, n, m) for (int i = n; i <= m; i++)
#define ROF(i, n, m) for (int i = n; i >= m; i--)

#define RI(x) scanf ("%d", &(x))
#define RII(x, y) RI(x), RI(y)
#define RIII(x, y, z) RI(x), RI(y), RI(z)

typedef long long ll;
typedef unsigned int ui;
typedef unsigned long long ull;

const ll mod = 1e9 + 7;
const int seed = 999731;
const double eps = 1e-8;

/***********************END OF DEFINE******************************/

const int mx = 105;

int t, n, tt, vis[2505];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("data.out", "w", stdout);
    RI(t);
    FOR (i, 0, t - 1) {
        RI(n);
        CLR(vis, 0);
        FOR (j, 0, 2 * n - 2) {
            FOR (k, 0, n - 1) {
                RI(tt);
                vis[tt] ++;
            }
        }
        cout << "Case #" << i + 1 << ":";
        FOR (j, 1, 2500) {
            if(vis[j] % 2)
                cout << " " << j;
        }
        cout << endl;
    }
    return 0;
}


/* A
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("data.out", "w", stdout);
    RI(t);
    FOR (i, 0, t - 1) {
        cin >> s;
        string tmp = "";
        string res = tmp + s[0];
        FOR (i, 1, s.size() - 1) {
            if(s[i] >= res[0])
                res = s[i] + res;
            else
                res = res + s[i];
        }
        cout << "Case #" << i + 1 << ": " << res << endl;
    }
    return 0;
}
*/
