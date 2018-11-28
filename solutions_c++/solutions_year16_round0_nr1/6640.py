#include <iostream>

using namespace std;

void solve(int test) {
    long long x; cin >> x;

    int seen = 0;
    cout << "Case #" << test << ": ";
    for (long long n = 1; n <= 5000; ++n) {
        long long cur = x * n;
        while (cur) {
            seen |= 1 << (cur % 10);
            cur /= 10;
        }
        if (seen == ((1 << 10) - 1)) {
            seen = -1;
            cout << x * n << endl;
            break;
        }
    }

    if (seen != -1)
        cout << "INSOMNIA" << endl;
}

int main() {
    int t; cin >> t;
    for (int e=0; e<t; ++e)
        solve(e + 1);
}
