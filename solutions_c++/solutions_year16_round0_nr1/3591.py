#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++) {
        long long mult;
        cin >> mult;
        long long n = mult;

        if (n == 0) {
            cout << "Case #" << tst + 1 << ": INSOMNIA\n";
            continue;
        }
        int mask = 0;

        while (mask != ((1 << 10) - 1)) {
            long long cp = n;

            while (n > 0) {
                mask |= (1 << (n % 10));
                n /= 10;
            }
            n = cp;
            n += mult;
        }
        cout << "Case #" << tst + 1 << ": " << n - mult << '\n';
    }
}
