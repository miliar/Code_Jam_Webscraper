#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;

#define PB push_back
#define MP make_pair
#define AA first
#define BB second
#define SZ size()
#define BG begin()
#define OP begin()
#define ED end()
#define SQ(x) ((x)*(x))
#define cmax(x, y) x = max(x, y)
#define cmin(x, y) x = min(x, y)

const double eps = 1e-8;
const LL MOD = 1000000007;
#define N 10004
int n;
int dic;
int g[N];

int main() {
    int i, j;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int Ca = 1; Ca <= T; Ca++) {
        scanf("%d%d", &n, &dic);
        for(i = 0; i < n; i++) scanf("%d", &g[i]);
        sort(g, g + n);
        int ans = 0;
        for(i = 0, j = n -1; i <= j; ) {
            if(g[i] + g[j] <= dic) {
                i++, j--;
            }
            else {
                j--;
            }
            ans++;
        }
        printf("Case #%d: %d\n", Ca, ans);
    }
    return 0;
}
