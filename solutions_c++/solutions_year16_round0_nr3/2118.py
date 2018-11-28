//Author: Artem Romanov
#include <bits/stdc++.h>
#define TASK "c"

#define F   first
#define S   second
#define y0  y84678
#define y1  y53021

using namespace std;
typedef long double dbl;

const dbl PI = 3.141592653589793238462643383279502884L;
const dbl E = 2.718281828459045235360287471352662498L;
const dbl EPS = 1e-12L;

int64_t a[11];

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    cout.precision(11); cout.setf(ios::fixed);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#elif defined(TASK)
    //freopen(TASK".in", "r", stdin);
    freopen(TASK".out", "w", stdout);
#endif

    for (int i = 2; i <= 10; ++i) {
        a[i] = i;
        a[i] *= a[i] *= a[i] *= a[i] *= a[i];
        a[i]++;
    }
    cout << "Case #1:";
    for (uint i = 0x8001, k = 0; k < 500; i += 2, ++k) {
        cout << '\n' << bitset<32>((i << 16) | i);
        for (int j = 2; j <= 10; ++j)
            cout << ' ' << a[j];
    }
    return 0;
}