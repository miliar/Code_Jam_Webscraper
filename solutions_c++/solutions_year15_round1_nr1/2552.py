#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <string>
#include <iterator>
#include <algorithm>
#include <cstdlib>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <vector>
#include <iterator>
using namespace std;
#define PI acos(-1.0)
#define INF 0x3f3f3f3f
#define inf 0x3f
#define MAXN 400005
#define MAXM 20005
#define MOD 1000000007
#define EPS 1e-6
#define rst(a,b) memset(a, b, sizeof(a))
#define pd(a) cout << "debug:" << a << " "
#define pp(a) cout << a << " "
#define pl(a) cout << a << endl
//#define min(a, b) a < b ? a : b
//#define max(a, b) a > b ? a : b
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
int a[1005];
void solve() {
    int cases;
    scanf("%d", &cases);
    for(int idx = 1; idx <= cases; idx++) {
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) scanf("%d", &a[i]);
        int ans1 = 0;
        for(int i = 1; i < n; i++) {
            if(a[i] < a[i-1]) ans1 += a[i-1]-a[i];
        }
        int ans2 = 0;
        int r = max(0, a[n-2] - a[n-1]);
        for(int i = 0; i < n-1; i++) {
            r = max(r, a[i]-a[i+1]);
        }
        for(int i = 0; i < n-1; i++) {
            ans2 += min(r, a[i]);
        }
        printf("Case #%d: %d %d\n", idx, ans1, ans2);
    }
}
void init() {
    freopen("D:\\1.in", "r", stdin);
    freopen("D:\\1.txt", "w", stdout);
}
int main(void) {
    //init();
    solve();
    return 0;
}
