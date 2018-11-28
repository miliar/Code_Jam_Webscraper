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
#include <unordered_map>
#include <stack>
#include <time.h>
#include <cstdlib>
#include <cstring>
#include <string.h>

#define llong long long int
#define pb push_back
#define mp make_pair
#define pr pair <int, int>
#define rev reverse
using namespace std;
const int MAXN = 2e6 + 7, INF = 1e9;
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
    //ios_base::sync_with_stdio(false);
    //cin.tie();
    scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        int n, m;
        int ans = 0, ans2 = 0;
        double eat = 0;
        scanf("%d", &n, &m);
        for (int i = 1; i <= n; i++) {
            scanf("%d", &a[i]);
            if (i > 1) {
                if (a[i - 1] > a[i]) {
                    ans += a[i - 1] - a[i];
                    eat = max(eat, (a[i - 1] - a[i]) / 10.0);
                }
            }
        }
        //cout << eat << endl;
        for (int i = 1; i < n; i++) {
            ans2 += int(min(1.0 * a[i], eat * 10));
           // cout << min(a[i], eat * 10) << ' ';
        }
        printf("Case #%d: %d %d\n", test, ans, ans2);
    }
    return  0;
}