#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cmath>
using namespace std;
void solve()
{
    int Case;
    cin >> Case;
    for (int ca = 1; ca <= Case; ca++) {
        printf("Case #%d: ", ca);
        unsigned long long r, t;
        cin >> r >> t;
        unsigned long long n, sum, ll = 1ULL, rr = 707106780ULL;
        while (ll <= rr) {
            n = (ll+rr)/2ULL;
            //if (2*r+2*n-1 > 1000000000ULL) rr = n-1;
            //else {
                sum = n*(2*r+2*n-1);
                if (sum <= t) ll=n+1;
                else rr=n-1;
            //}
        }
        cout << rr << endl;
    }
}
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("test.out", "w", stdout);
    solve();
    return 0;
}
