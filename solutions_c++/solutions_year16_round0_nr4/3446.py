#include <iostream>

using namespace std;

int t, k, c, s;

int main() {
    cin >> t;
    for (int i = 0; i ++< t;) {
        cin >> k >> c >> s;
        if (k != s) ++*(int *)0;
        long long p = 1;
        for (int i = c; i --> 1;) p *= k;
        cout << "Case #" << i << ": ";
        for (long long q = 0; q < k; ++q) cout << (q * p) + 1 << ' ';
        cout << '\n';
    }
}

