#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

const int MAX = 10000;

void print(int i, int mask) {
    while (i >= 0) {
        if (mask & (1 << i)) {
            cout << 1;
        } else {
            cout << 0;
        }
        --i;
    }
}

int main() {
    int t;
    cin >> t;
    cout << "Case #1:\n";
    int n, amo;
    cin >> n >> amo;
    for (int mask = (1 << (n - 1)) + 1; mask < (1 << n); mask += 2) {
        vector<int> divs;
        for (int s = 2; s <= 10; s++) {
            for (int divisor = 2; divisor < (1 << (n - 1)); divisor++) {
                int deg = 1, ost = 0;
                for (int i = 0; i < n; i++) {
                    if (mask & (1 << i)) {
                        ost += deg;
                        if (ost >= divisor) {
                            ost -= divisor;
                        }
                    }
                    deg = (deg * s) % divisor;
                }
                if (ost == 0) {
                    divs.push_back(divisor);
                    break;
                }
            }
        }
        if (divs.size() == 9) {
            print(n-1, mask);
            cout << " ";
            for (int x : divs) {
                cout << x << " ";
            }
            cout << '\n';
            amo--;
            if (amo == 0) {
                break;
            }
        }
    }
    return 0;
}
