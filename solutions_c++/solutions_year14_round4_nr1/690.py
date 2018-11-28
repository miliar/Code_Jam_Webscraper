#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <vector>
#include <string>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;
#define bitAt(x, k) (((x) >> (k)) & 1)
typedef long long LL;
typedef long double LD;
const int MOD = 1000000000 + 7;
const int INF = 1000000000;
const double EPS = 1e-9;
const double PI = acos(-1.0);

const int N = 10005;

int n, m, a[N];

void solve() {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; ++i) {
        scanf("%d", &a[i]);
    }
    sort(a + 1, a + n + 1);
    int ans = 0;
    for (int i = 1, j = n; i <= j; ) {
        if (i == j) {
            ++ans;
            ++i;
            continue;
        }
        if (a[i] + a[j] <= m) {
            ++ans;
            ++i;
            --j;
        } else {
            ++ans;
            --j;
        }
    }
    printf("%d\n", ans);
}

int main() {
    int test;
    scanf("%d", &test);
    for (int kase = 1; kase <= test; ++kase) {
        printf("Case #%d: ", kase);
        solve();
    }
    return 0;
}
