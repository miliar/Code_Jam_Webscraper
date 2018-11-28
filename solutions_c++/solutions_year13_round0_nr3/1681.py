#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;

bool IsPalindrome(LL x) {
    if (x == 0) {
        return true;
    }
    int a[32];
    int cnt = 0;
    while (x != 0) {
        a[cnt++] = x % 10;
        x /= 10;
    }
    for (int i = 0; i < cnt; ++i) {
        if (a[i] != a[cnt - 1 - i]) {
            return false;
        }
    }
    return true;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    vector<LL> a;
    const LL LIM = 10000000;
    for (LL i = 1; i <= LIM; ++i) {
        LL cur = i * i;
        if (IsPalindrome(i) && IsPalindrome(cur)) {
            a.push_back(cur);
        }
    }

    
    int nTests;
    cin >> nTests;
    for (int test = 0; test < nTests; ++test) {
        LL l, r;
        cin >> l >> r;
        int ans = 0;
        for (size_t i = 0; i < a.size(); ++i) {
            if (a[i] >= l && a[i] <= r) {
                ans++;
            }
        }
        cout << "Case #" << test + 1 << ": ";
        cout << ans << '\n';
    }

    return 0;
}