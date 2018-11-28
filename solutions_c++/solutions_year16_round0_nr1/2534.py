//Author: Artem Romanov
#include <bits/stdc++.h>
#define TASK "a"

#define F   first
#define S   second
#define y0  y84678
#define y1  y53021

using namespace std;
typedef long double dbl;

const dbl PI = 3.141592653589793238462643383279502884L;
const dbl E = 2.718281828459045235360287471352662498L;
const dbl EPS = 1e-12L;

int n, t, v, a[1000000];

int f(int v, int r = 0) {
    while (r |= 1 << v % 10, v /= 10);
    return r;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    cout.precision(11); cout.setf(ios::fixed);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#elif defined(TASK)
    freopen(TASK".in", "r", stdin);
    freopen(TASK".out", "w", stdout);
#endif

    for (int i = 1; i <= 1000000; ++i) {
        for (int j = 1, b = 0; b != 1023; ++j)
            b |= f(v = i * j);
        a[i - 1] = v;
    }

    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> n;
        cout << "Case #" << i + 1 << ": " << (n ? to_string(a[n - 1]) : "INSOMNIA") << '\n';
    }
    return 0;
}