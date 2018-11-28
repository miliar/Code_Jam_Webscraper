#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        bool digit[10];
        long long n;
        int r = 10;
        memset(digit, 0, sizeof digit);
        cin >> n;
        std::cout << "Case #" << i << ": ";
        if (n == 0) {
            std::cout << "INSOMNIA" << std::endl;
            continue;
        }
        long long b;
        for (long long j = 1; r > 0; j++) {
            b = j*n;
            while (b) {
                if (!digit[(b % 10)]) {
                    r--;
                    digit[(b % 10)] = true;
                }
                b /= 10;
            }
            b = j*n;
        }
        cout << b << endl;
    }
}
