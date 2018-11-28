#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool complete(vector<bool> digits) {
    for (auto it = digits.begin(); it != digits.end(); ++it) {
        if (*it == false) {
            return false;
        }
    }
    return true;
}

int solve(int N) {
    if (N == 0) {
        return -1;
    }

    vector<bool> digits(10, false);

    int lastN;
    int i = 1;
    do {
        int n = i * N;
        lastN = n;

        do {
            int digit = n % 10;
            digits[digit] = true;
            n /= 10;
        } while (n > 0);
        ++i;
    } while (!complete(digits));

    return lastN;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int N;
        cin >> N;

        int solution = solve(N);

        cout << "Case #" << t + 1 << ": " << (solution >= 0 ? to_string(solution) : "INSOMNIA") << endl;
    }
}
