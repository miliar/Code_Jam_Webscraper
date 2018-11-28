#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int n(0);
        cin >> n;
        vector<int> m(n);
        int diff = 0;

        for (int i = 0; i < n; ++i)
            cin >> m[i];

        for (int i = 0; i < n - 1; ++i) {
            int buf = m[i] - m[i + 1];
            if (buf > diff)
                diff = buf;
        }

        int ate_max(0);
        int ate_const(0);
        for (int i = 0; i < n - 1; ++i) {
            int b = m[i] - m[i + 1];
            if (b > 0)
                ate_max += b;

            if (m[i] - diff > 0) {
                ate_const += diff;
            }
            else ate_const += m[i];
        }

        cout << "Case #" << test << ": " << ate_max << " " << ate_const << endl;
    }

    return 0;
}