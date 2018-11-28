#include <cstdint>
#include <array>
#include <algorithm>
#include <iostream>

using namespace std;

int solve(int n) {
    if (n == 0) return 0;
    int digitLeft = 10;
    array<bool, 10> digitAppeared;
    digitAppeared.fill(false);

    uint64_t sum = 0;
    while (digitLeft != 0) {
        sum += n;

        auto tmp = sum;
        while (tmp != 0) {
            auto remainder = int(tmp % 10);
            if (!digitAppeared[remainder]) {
                digitAppeared[remainder] = true;
                if (--digitLeft == 0) return sum;
            }

            tmp /= 10;
        }
    }

    return -1;
}

int main() {
    int numberOfCases;

    cin >> numberOfCases;
    for (int i = 1; i <= numberOfCases; ++i) {
        // read input
        int baseNumber;
        cin >> baseNumber;

        // write output
        cout << "Case #" << i << ": ";
        auto solution = solve(baseNumber);
        if (solution > 0) {
            cout << solution;
        } else {
            cout << "INSOMNIA";
        }
        cout << endl;
    }

    return 0;
}
