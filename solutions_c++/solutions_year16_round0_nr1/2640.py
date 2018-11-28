#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string solve(int N) {
    if (N == 0) {
        return "INSOMNIA";
    }
    bool digits[10] = { false };
    for (int n = N;; n += N) {
        for (char c: to_string(n)) {
            digits[c - '0'] = true;
        }
        if (all_of(digits, digits + 10, [](bool i){ return i; })) {
            return to_string(n);
        }
    }
}

int main() {
    int T = 0;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N = 0;
        cin >> N;
        cout << "Case #" << t << ": " << solve(N) << endl;
    }
    
    return 0;
}
