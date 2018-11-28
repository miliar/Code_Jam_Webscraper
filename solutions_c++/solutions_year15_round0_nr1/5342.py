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
int fun(char *str, int Smax) {
    int len = strlen(str);
    int pre = str[0] - '0';
    int ans = 0;
    for(int i = 1; i < len; i++) {
        if(i <= pre) {
            pre += str[i] - '0';
            continue;
        }
        ans += i-pre;
        pre = i + str[i]-'0';
        //printf("(%d %d %d\n", i, ans, pre);
    }
    return ans;
}
void solve() {
    int cases;
    scanf("%d", &cases);
    for(int idx = 1; idx <= cases; idx++) {
        int Smax;
        scanf("%d", &Smax);
        char str[1005];
        scanf("%s", str);
        int ans = fun(str, Smax);
        printf("Case #%d: %d\n", idx, ans);
    }
}
int main() {
    solve();
    return 0;
}
