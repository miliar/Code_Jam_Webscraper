#include <iostream>

using namespace std;

long long t, n, s;

int main() {
    cin >> t;
    for (long long i = 0; i ++< t; s = 0) {
        cout << "Case #" << i << ": ";
        cin >> n;
        if (!n) cout << "INSOMNIA\n";
        else for (long long m = n;; m += n) {
            long long x = m;
            while (x) s |= 1 << (x % 10), x /= 10;
            if (s == 1023) {
                cout << m << '\n';
                break;
            }
        }
    }
}

