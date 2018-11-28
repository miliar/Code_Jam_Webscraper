//Author: Artem Romanov
#include <bits/stdc++.h>
#define TASK "b"

#define F   first
#define S   second
#define y0  y84678
#define y1  y53021

using namespace std;
typedef long double dbl;

const dbl PI = 3.141592653589793238462643383279502884L;
const dbl E = 2.718281828459045235360287471352662498L;
const dbl EPS = 1e-12L;

int t, n, k;
bool b[200];
string s;

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

    cin >> t;
    for (int i = 0; i < t; ++i) {
        memset(b, 0, 200);
        cin >> s; k = 0;
        n = (int) s.size();
        for (int j = 0; j < n; ++j) {
            b[j] = s[j] == '+';
        }
        for (int j = n - 1; j >= 0; --j) {
            if (!b[j]) {
                for (int l = 0; l <= j; ++l) {
                    b[l] ^= 1;
                }
                k++;
            }
        }
        cout << "Case #" << i + 1 << ": " << k << '\n';
    }
    return 0;
}