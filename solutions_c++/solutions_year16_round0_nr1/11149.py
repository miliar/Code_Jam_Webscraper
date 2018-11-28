#include <iostream>
#include <string>
using namespace std;
typedef unsigned int uint;

int solve (uint n) {
    if (!n) return 0;
    uint seen = 0;
    uint t = n;
    while (seen != 0x3ff) {
        uint m = t;
        while (m) {
            seen |= 1 << (m % 10);
            m /= 10;
        }
        t += n;
    }
    return t-n;
}

int main () {
    uint nb_test;
    uint n;
    cin >> nb_test;
    for (uint i = 1; i <= nb_test; i++) {
        cin >> n;
        uint r = solve(n);
        cout << "Case #" << i << ": ";
        if (!r) cout << "INSOMNIA";
        else cout << r;
        cout << "\n";
    }
}
