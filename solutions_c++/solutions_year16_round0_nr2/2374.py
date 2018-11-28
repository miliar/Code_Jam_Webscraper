// Google Code Jam 2016
// Qualification Round
// B. Revenge of the Pancakes
// patsp

#include <iostream>
#include <stdexcept>

using namespace std;

static int solve(const string &sOrg) {
    string s = sOrg;
    int n = static_cast<int>(s.size());
    int ans = 0;
    for (int i = n - 1; i >= 0; --i) {
        if ('-' == s.at(i)) {
            ans += 1;
            for (int j = 0; j <= i; ++j) {
                if ('-' == s.at(j)) {
                    s.at(j) = '+';
                } else if ('+' == s.at(j)) {
                    s.at(j) = '-';
                } else {
                    throw runtime_error("unexpected character");
                }
            }
        }
    }
    return ans;
}

int main() {
    int nTests = 0;
    cin >> nTests;
    for (int test = 1; test <= nTests; ++test) {
        string s;
        cin >> s;
        cout << "Case #" << test << ": " << solve(s) << "\n";
    }

    return 0;
}

