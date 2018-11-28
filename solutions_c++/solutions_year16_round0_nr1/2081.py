#include <iostream>
#include <cstdio>

using namespace std;

bool d[10];

int main () {
    int T, a;
    cin >> T;
    for (int _t = 0; _t < T; ++_t) {
        for (int i = 0; i < 10; ++i) d[i] = false;
        cin >> a;
        if (a == 0) {
            cout << "Case #" << _t + 1 << ": INSOMNIA" << endl;
            continue;
        }
        int n = 0;
        int found = 0;
        while (found < 10) {
            n += a;
            int t = n;
            while (t != 0) {
                int dig = t % 10;
                if (!d[dig]) {
                    ++found;
                    d[dig] = true;
                }
                t /= 10;
            }
        }

        cout << "Case #" << _t + 1 << ": " << n << endl;
    }
    return 0;
}
