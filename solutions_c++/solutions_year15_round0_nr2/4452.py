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
#define EPS 1e-10
#define rst(a,b) memset(a, b, sizeof(a))
#define pd(a) cout << "debug:" << a << " ";
#define pp(a) cout << a << " ";
#define pl(a) cout << a << endl;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
void solve() {
    int cases;
    scanf("%d", &cases);
    for(int idx = 1; idx <= cases; idx++) {
        int n;
        scanf("%d", &n);
        int max_t = 0;
        priority_queue<int> Q;
        for(int i = 0; i < n; i++) {
            int tt;
            scanf("%d", &tt);
            Q.push(tt);
            max_t = max(max_t, tt);
        }
        int ans = max_t;
        for(int i = max_t-1; i > 0; i--) {
            int ans_t = 0;
            int tmp;
            priority_queue<int> T = Q;
            while(!T.empty() && (tmp=T.top()) > i) {
                T.pop();
                T.push(tmp-i);
                T.push(i);
                ans_t++;
            }
            ans = min(ans, ans_t+i);
        }
        printf("Case #%d: %d\n", idx, ans);
    }
}
int main() {
    //freopen("D:\\5.in", "r", stdin);
    //freopen("D:\\55.out", "w", stdout);
    solve();
    return 0;
}
