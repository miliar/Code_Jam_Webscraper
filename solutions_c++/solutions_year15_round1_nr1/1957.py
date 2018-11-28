#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cassert>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>

#define DEBUGLEVEL
#ifdef DEBUGLEVEL
#define printf_debug(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define printf_debug(fmt, args...)
#endif

typedef long long llong;

using namespace std;

int a[20000];

int main() {
#ifdef DEBUG
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
#endif
    int T;
    cin >> T;
    for(int test = 1; test <= T; ++test) {
        int n;
        int x = 0;
        int y = 0;
        cin >> n;
        int prev = 0;
        int mx = 0;
        for (int i = 0; i < n; ++i) {
          int cur;
          cin >> cur;
          a[i] = cur;
          if (cur < prev) {
            x += prev - cur;
          }
          mx = max(mx, max(prev - cur, 0));
          prev = cur;
        }
        for (int i = 0; i < n - 1; ++i) {
            if (a[i] > mx) {
                y += mx;
            } else {
                y += a[i];
            }
        }
        printf("Case #%d: ", test);
        printf("%d %d\n", x, y);
    }
    return 0;
}