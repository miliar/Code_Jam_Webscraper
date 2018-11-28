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
char s[1100];
int main () {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, n;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int tot = 0, ans = 0;
        scanf("%d%s", &n, s);
        for (int i = 0; i <= n; i++) {
            if (tot >= i) tot += s[i] - '0';
            else {
                ans += i - tot;
                tot = i + s[i] - '0';
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
