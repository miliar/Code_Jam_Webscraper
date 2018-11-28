#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <time.h>
#include <cassert>
#include <map>
#include <set>
#include <unordered_set>
#include <stack>
#include <time.h>
#include <cstdlib>
#include <cstring>
#include <string.h>

#define llong long long int
#define pb push_back
#define mp make_pair
#define pr pair <int, int>

using namespace std;
const int MAXN = 2e6 + 7;
int T;
int a[1010];
int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    //#define FNAME "sum2"
    //freopen(FNAME".in", "r", stdin);
    //freopen(FNAME".out", "w", stdout);
#endif
    //ios_base::sync_with_stdio(false);cin.tie();
    scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        
        int mx = 0, n;
        scanf("%d", &n);
        for (int i = 1; i <= n; i++) {
            scanf("%d", &a[i]);
            mx = max(a[i], mx);
        }
        int ans = mx;
        for (int i = 1; i <= mx; i++) {
            int res = 0;
            for (int j = 1; j <= n; j++) {
                res += (a[j] - 1) / i;
            }
            ans = min(ans, res + i);
        }
        
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}