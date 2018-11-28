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

int pow_of_2(int n) {
    int ans = 0;
    while(n > 1) {
        n >>= 1;
        ans++;
    }
    return ans;
}

int main() {
#ifdef DEBUG
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
#endif
    int t;
    cin >> t;
    int T = 1;
    while(t--) {
        int n, p;
        cin >> n >> p;
        int a1 = -1, a2 = -1;
        // int ap1 = -1, ap2 = -1;
        for(int i = 0; i < (1 << n); ++i) {
            int p1 = (1 << n) - ((1 << (n - pow_of_2(i + 1))) - 1);
            if (p1 <= p && i > a1) a1 = i;
            // int p2 = ((1 << n) - 1) ^ ((1 << (n - pow_of_2(n - i))) - 1)
            int p2 = (1 << n) - (((1 << n) - 1) ^ ((1 << (n - pow_of_2((1 << n) - i))) - 1));
            if (p2 <= p && i > a2) a2 = i;
            // printf_debug("i = %d, p1 = %d, p2 = %d, pow = %d\n", i, p1, p2, pow_of_2(i + 1));
        }
        cout << "Case #" << T++ << ": " << a1 << " " << a2 << endl;
    }
    return 0;
}