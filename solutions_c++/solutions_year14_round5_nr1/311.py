#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>

using namespace std;

int T;
long long n, p, q, r, s;
long long a[2000001];
long long sum[2000001];
long long resum[2000001];

inline long long max(long long  a, long long b)
{
    return a > b ? a : b;
}
inline long long min(long long  a, long long b)
{
    return a < b ? a : b;
}

long double solve()
{
    long long tot = 0;
    for (int i=0; i<n; ++i) tot+=a[i];
    long long in_range = 0;
    long long left_range;
    long long right_range;
    long long my_best = 0;
    // l = 0;
    //while (out_range > in_range) {
    for (int i=0; i<=n; ++i) {
        left_range = sum[i-1];
        for (int j=i; j<=n; ++j) {
            // [l,r]
            in_range = sum[j]-sum[i-1];
            right_range = tot - sum[j];
            if (in_range >= left_range && in_range >= right_range) {
                my_best = max(my_best, (tot - in_range));
            } else if (left_range >= in_range && left_range >= right_range) {
                my_best = max(my_best, (tot - left_range));
            } else if (right_range >= in_range && right_range >= left_range) {
                my_best = max(my_best, (tot - right_range));
            }

        }
    }
    return my_best * 1.0 / tot;
}

int main()
{
    cin >> T;
    for (int t=1; t<=T; ++t) {
        cin >> n >> p >> q >> r >> s;
        sum[0] = 0;
        for (int i=0; i<n; ++i) {
            a[i] = ((i) * p % r + q) % r + s;
            //cout << a[i] << endl;
            sum[i+1] = sum[i] + a[i];
        }
        printf("Case #%d: %.10llf\n", t, solve());
    }

    return 0;
}
