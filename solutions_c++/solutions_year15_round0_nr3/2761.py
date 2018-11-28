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
// i - 2 j - 3 k - 4
int A[5][5] = {
{0, 1, 2, 3, 4},
{1, 1, 2, 3, 4},
{2, 2, -1, 4, -3},
{3, 3, -4, -1, 2},
{4, 4, 3, -2, -1}
};
map<char, int> mp;
const int N = 10000 + 10;
int l, x, n;
char str[N];
string s;
int a[N], b[N];
int get(int x, int y) {
    int xx = fabs(x), yy = fabs(y);
    int t = A[xx][yy];
    if (x < 0) t *= -1;
    if (y < 0) t *= -1;
    return t;
}
void work() {
    mp['i'] = 2, mp['j'] = 3, mp['k'] = 4;
    //mp['i'] = 2, mp['j'] = 3, mp['k'] = 4;
    a[0] = mp[s[0]];
    b[n - 1] = mp[s[n - 1]];
    for (int i = 1; i < n; i++) {
        a[i] = get(a[i - 1], mp[s[i]]);
        b[n - i - 1] = get(mp[s[n - i - 1]], b[n - i]);
    }
}
int main () {
    int T;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("fk.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d%s", &l, &x, str);
        s = str;
        for (int i = 1; i < x; i++) s += str;
        n = l * x;
        printf("Case #%d: ", cas);
        if (n < 3) {
            puts("NO");
            continue;
        }
        work();
        bool flag = false;
        for (int i = 0; i < n - 2; i++) if (a[i] == 2) {
            for (int j = i + 2; j < n; j++) if (b[j] == 4) {
                if (get(a[i], 3) == a[j - 1]) {
                    puts("YES");
                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }
        if (!flag) puts("NO");
    }
    return 0;
}
