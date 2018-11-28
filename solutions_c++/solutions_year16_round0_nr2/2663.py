#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

inline char Flip(char c) {
    return c == '+' ? '-' : '+';
}

inline void Flip(string& s, int until) {
    for (int i = 0; i < until; i++) {
        s[i] = Flip(s[i]);
    }
    reverse(s.begin(), s.begin() + until);
}

static int CountFlips(string& s) {
    int n = s.size();
    int r = n - 1, flips = 0;
    while (r >= 0) {
        while (r >= 0 && s[r] == '+') r--;
        if (r < 0) break;

        int l = 0;
        while (l < r && s[l] == '+') l++;
        if (l > 0) {
            Flip(s, l);
            flips++;
        }
        Flip(s, r + 1);
        flips++;
    }
    return flips;
}

int main() {
    int num_tests;
    cin >> num_tests;
    string s;
    for (int test = 1; test <= num_tests; test++) {
        cin >> s;
        cout << "Case #" << test << ": " << CountFlips(s) << "\n";
    }
    return 0;
}
