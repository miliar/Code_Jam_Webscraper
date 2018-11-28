#include <iostream>

using namespace std;

int solve(string s) {
    int ret = 0;
    bool flip = true;
    for(auto it = s.rbegin(); it != s.rend(); it++) {
        if (flip) {
            if (*it=='-') {
                flip = false;
                ++ret;
            }
        }
        else {
            if (*it=='+') {
                flip = true;
                ++ret;
            }
        }
    }
    return ret;
}

int main() {
    int T, R;
    cin >> T;
    string S;
    for (int c = 1; c <= T; c++) {
        cin >> S;
        R = solve(S);
        cout << "Case #" << c << ": " << R << endl;
    }

    return 0;
}