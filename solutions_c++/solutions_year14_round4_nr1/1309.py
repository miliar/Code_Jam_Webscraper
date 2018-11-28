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

#define DEBUGLEVEL
#ifdef DEBUGLEVEL
#define printf_debug(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define printf_debug(fmt, args...)
#endif

typedef long long llong;

using namespace std;

const int MAXN = 100000;

int a[MAXN];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        int n, x;
        cin >> n >> x;
        for(int i = 0; i < n; ++i) {
            cin >> a[i];            
        }
        sort(a, a + n);
        int pe = n - 1, ps = 0;
        int ans = 0;
        while(ps <= pe) {
            if(ps != pe && a[ps] + a[pe] <= x) {
                pe--;
                ps++;
            } else {
                pe--;
            }
            ans++;
        }
        printf("Case #%d: %d\n", t, ans);
    }    
    return 0;
}