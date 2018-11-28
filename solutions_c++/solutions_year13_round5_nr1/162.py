#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

constexpr long long size = 37;

void solve()
{
    long long b, n;
    long long x[size], y[size];
    for (long long i = 0; i < size; ++i) {
        x[i] = 0;
        y[i] = 0;
    }
    cin >> b >> n;
    for (long long i = 0; i < n; ++i) cin >> x[i];
    sort(x, x + size);
    long double maximum = 0;
    long long i;
    for (i = 0; i < size; ++i) {
        if (i < size - 1 && x[i] == x[i + 1]) continue;
        long long t = 0;
        for (long long j = 0; j <= i; ++j) {
            y[j] = x[i] - x[j];
            t += y[j];
        }
        if (t > b) break;
        maximum = max(maximum, (36 * t) / static_cast<long double>(i + 1) - t);
        long long tt = t;
        for (long long j = i; j >= 1; --j) {
            tt -= y[j];
            ++y[j];
            ++t;
            if (t > b) break;
            maximum = max(maximum, (36 * tt) / static_cast<long double>(j) - t);
        }
        if (t > b) break;
    }
    if (i == size) {
        cout << maximum;
        return;
    }
    //cerr << maximum << endl;
    long long o = x[i];
    long long d = 0; for (long long j = 0; j < i; ++j) if (x[j] != x[i]) d = x[j];
    while (i && x[i] == x[i - 1]) --i;
    --i;
    while (o > d + 1) {
        long long m = (o + d) / 2;
        long long t = 0;
        for (long long j = 0; j <= i; ++j) {
            y[j] = m - x[j];
            t += y[j];
        }
        if (t > b) {
            o = m;
            continue;
        }
        maximum = max(maximum, (36 * t) / static_cast<long double>(i + 1) - t);
        long long tt = t;
        for (long long j = i; j >= 1; --j) {
            tt -= y[j];
            ++y[j];
            ++t;
            if (t > b) break;
            maximum = max(maximum, (36 * tt) / static_cast<long double>(j) - t);
        }
        if (t > b) {
            o = m;
            continue;
        }
        d = m;
    }
    cout << setprecision(50) << maximum;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
