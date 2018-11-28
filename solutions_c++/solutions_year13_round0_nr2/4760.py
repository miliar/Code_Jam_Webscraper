#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <cctype>
#include <map>
#include <iomanip>
                   
using namespace std;
                   
#define eps 1e-8
#define pi acos(-1.0)
#define inf 1<<30
#define linf 1LL<<60
#define pb push_back
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define fi first
#define se second

int a[150][150];
int r[150], c[150];
int n, m;
bool solve() {
    
    return true;
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.txt", "w", stdout);
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> n >> m;
        memset(r, 0, sizeof(r));
        memset(c, 0, sizeof(c));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> a[i][j];
                r[i] = max(r[i], a[i][j]);
                c[j] = max(c[j], a[i][j]);
            }
        }
        printf("Case #%d: ", Case++);
        bool flag=true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (a[i][j] < r[i] && a[i][j] < c[j]) {
                    flag=false;
                    break;
                }
            }
        }
        puts(flag?"YES":"NO");
    }
    return 0;
}
