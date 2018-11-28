#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <cassert>
#include <map>
#include <set>
#include <ctime>
#include <unordered_map>
#include <iomanip>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const double eps = 1e-10;
const int inf = 1000000000;

const int N = 1000005;
const int M = 4097;
const int mo = 1000000000 + 7;

int f[13][M][M], g[13][M][M];

int dp(int n, int a, int b, int c) {
    if (n == 0) return true;
    int &ans = f[n][a][b];
    if (ans != 0) return ans;
    int x = (a + b - c) / 2;
    if (x < 0 || x > a || x > b) return ans = -1;
    int aa = a - x;
    int bb = x;
    int cc = b - x;
    if (dp(n - 1, aa, bb, cc) == 1) {
        g[n][a][b] = x;
        return ans = 1;
    }
    else return ans = -1;
}

void work()
{
    int n, a, b, c;
    cin >> n >> a >> b >> c;
    if (dp(n, a, b, c) == -1) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    queue<string> q[3];
    for (int i = 0; i < a; ++i) q[0].push("R");
    for (int i = 0; i < b; ++i) q[1].push("P");
    for (int i = 0; i < c; ++i) q[2].push("S");
    while (1) {
        if (n == 0) {
            for (int i = 0; i < 3; ++i)
                if (q[i].size() > 0) {
                    cout << q[i].front() << endl;
                }
            return;
        }
        int x = g[n][a][b];
        for (int i = 0; i < x; ++i) {
            string s = min(q[1].front() + q[0].front(), q[0].front() + q[1].front());
            q[0].pop(), q[1].pop();
            q[1].push(s);
        }
        for (int i = 0; i < a - x; ++i) {
            string s = min(q[0].front() + q[2].front(), q[2].front() + q[0].front());
            q[0].pop(), q[2].pop();
            q[0].push(s);
        }
        for (int i = 0; i < b - x; ++i) {
            string s = min(q[1].front() + q[2].front(), q[2].front() + q[1].front());
            q[1].pop(), q[2].pop();
            q[2].push(s);
        }
        int aa = a - x;
        int bb = x;
        int cc = b - x;
        --n;
        a = aa;
        b = bb;
        c = cc;
    }
}

int main()
{
    #ifdef LOCAL_TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
