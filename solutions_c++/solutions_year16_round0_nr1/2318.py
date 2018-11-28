#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int iTest = 0; iTest < t; ++iTest) {
        static const int kAllMask = (1 << 10) - 1;
        uint64_t n;
        cin >> n;
        cout << "Case #" << iTest + 1 << ": ";
        if (0 == n) {
            cout << "INSOMNIA";
        } else {
            int mask = 0;
            uint64_t now = 0;
            do {
                now += n;
                uint64_t clone = now;
                while (clone) {
                    mask |= 1 << (clone % 10);
                    clone /= 10;
                }
            } while (mask != kAllMask);
            cout << now;
        }
        cout << endl;
    }

    return 0;
}
