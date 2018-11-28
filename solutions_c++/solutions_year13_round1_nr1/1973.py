#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

int num = 0;

void solve() {
     long long a, b;
     cin >> a >> b;
     a = a + a + 1;
     long long l = 0, r = 1000000000;
     while (l != r) {
           long long mid = (l + r >> 1) + 1;
           if (a * mid + mid * 2 * (mid - 1) <= b) l = mid;
           else r = mid - 1;
     }
     num++; cout << "Case #" << num << ": " << l << endl;
}

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t; cin >> t; while (t--) solve();
}
