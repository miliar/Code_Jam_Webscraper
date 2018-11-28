/*
ID: wuqi9395@126.com
PROG:
LANG: C++
*/
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<fstream>
#include<cstring>
#include<ctype.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define INF (1 << 30)
#define LINF (1LL << 60)
#define PI acos(-1.0)
#define mem(a, b) memset(a, b, sizeof(a))
#define rep(i, a, n) for (int i = a; i < n; i++)
#define per(i, a, n) for (int i = n - 1; i >= a; i--)
#define eps 1e-6
#define debug puts("===============")
#define pb push_back
#define mkp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
#define POSIN(x,y) (0 <= (x) && (x) < n && 0 <= (y) && (y) < m)
typedef long long ll;
typedef unsigned long long ULL;
int a[5][5][5];
void init() {
    for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++) {
            a[1][i][j] = 1;
            if ((i * j) % 2 == 0) a[2][i][j] = 1;
        }
    a[3][2][3] = a[3][3][2] = a[3][3][3] = a[3][4][3] = a[3][3][4] = 1;
    a[4][3][4] = a[4][4][3] = a[4][4][4] = 1;
}
int main () {
    init();
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("d.out", "w", stdout);
    int T, x, r, c;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d%d", &x, &r, &c);
        printf("Case #%d: %s\n", cas, a[x][r][c] == 1 ? "GABRIEL" : "RICHARD");
    }
    return 0;
}
