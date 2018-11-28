/*************************************************************************
	> File Name: a.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com
	> Created Time: 2015年05月30日 星期六 22时00分27秒
 ************************************************************************/

#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <complex>
#include <cassert>
// #pragma comment(linker,"/STACK:102400000,102400000")
using namespace std;
#define LL long long
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define MAXN 105
template <typename T> inline void checkMax(T &a, T b) {a = a>b?a:b;}
template <typename T> inline void checkMin(T &a, T b) {a = a<b?a:b;}
typedef pair<int, int> PII;
typedef vector<int> vi;
const double PI = acos(-1.0);
const double eps = 1e-8;
int T, Cas = 1, R, C;

char str[MAXN];

int a[MAXN][MAXN];

bool vis[MAXN][MAXN];

bool check(int x, int y) {
    int cnt = 0;
    for (int i = 1; i <= R; i ++) {
        if (a[i][y]) {
            cnt ++;
        }
    }
    for (int i = 1; i <= C; i ++) {
        if (a[x][i]) {
            cnt ++;
        }
    }
    if (cnt > 2) {
        return true;
    } else {
        return false;
    }
}

void work() {
    memset(vis, 0, sizeof(vis));
    printf("Case #%d: ", Cas ++);
    scanf("%d %d", &R, &C);
    for (int i = 1; i <= R; i ++) {
        scanf("%s", str + 1);
        for (int j = 1; j <= C; j ++) {
            if (str[j] == '.') {
                a[i][j] = 0;
            }
            if (str[j] == '^') {
                a[i][j] = 1;
            }
            if (str[j] == 'v') {
                a[i][j] = 2;
            }
            if (str[j] == '>') {
                a[i][j] = 3;
            }
            if (str[j] == '<') {
                a[i][j] = 4;
            }
        }
    }
    for (int i = 1; i <= R; i ++) {
        for (int j = 1; j <= C; j ++) {
            if (a[i][j] && !check(i, j)) {
                printf("IMPOSSIBLE\n"); return ;
            }
        }
    }
    for (int j = 1; j <= C; j ++) {
        for (int i = 1; i <= R; i ++) {
            if (a[i][j] == 1) {
                a[i][j] = 2;
                vis[i][j] = true;
                break;
            } else if (a[i][j]) {
                break;
            }
        }
        for (int i = R; i >= 1; i --) {
            if (a[i][j] == 2) {
                a[i][j] = 1;
                vis[i][j] = true;
                break;
            } else if (a[i][j]) {
                break;
            }
        }
    }
    for (int i = 1; i <= R; i ++) {
        for (int j = 1; j <= C; j ++) {
            if (a[i][j] == 4) {
                a[i][j] = 3;
                vis[i][j] = true;
                break;
            } else if (a[i][j]) {
                break;
            }
        }
        for (int j = C; j >= 1; j --) {
            if (a[i][j] == 3) {
                a[i][j] = 4;
                vis[i][j] = true;
                break;
            } else if (a[i][j]) {
                break;
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= R; i ++) {
        for (int j = 1; j <= C; j ++) {
            ans += vis[i][j];
        }
    }
    cout << ans << endl;
}
int main() {
    scanf("%d", &T);
    while (T --) {
        work();
    }
    return 0;
}
