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

const int N = 205;
const int mo = 1000000000 + 7;

char a[N][N], b[N][N];
int n, ans, imp;
int match[N], v[N];

bool find(int j) {
    if (v[j]) return false;
    v[j] = true;
    for (int i = 0; i < n; ++i) if (i != imp && b[i][j] == '1') {
        if (match[i] == -1 || find(match[i])) {
            match[i] = j;
            return true;
        }
    }
    return false;
}

bool cal() {
    for (int i = 0; i < n; ++i) {
        memset(match, -1, sizeof match);
        bool flag = true;
        imp = i;
        for (int j = 0; j < n; ++j)
            if (b[i][j] == '1') {
                memset(v, 0, sizeof v);
                if (!find(j)) {
                    flag = false;
                    break;
                }
            }
        if (flag) return false;
    }
    return true;
}

void dfs(int i, int j) {
    if (j == n) {
        dfs(i + 1, 0);
        return;
    }
    if (i == n) {
        if (cal()) {
            int t = 0;
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < n; ++j)
                    if (a[i][j] != b[i][j])
                        ++t;
            ans = min(ans, t);
        }
        return;
    }
    if (a[i][j] == '0') {
        b[i][j] = '0';
        dfs(i, j + 1);
    }
    b[i][j] = '1';
    dfs(i, j + 1);
}

void work()
{
    cin >> n;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> a[i][j];
    ans = inf;
    dfs(0, 0);
    cout << ans << endl;
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
