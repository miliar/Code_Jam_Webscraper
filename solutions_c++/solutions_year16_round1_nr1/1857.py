#include <iostream>

using namespace std;

string solve(string s) {
    string ret;
    for (auto ch : s) {
        if (ret.empty()) {
            ret = ch;
        }
        else if (ch >= ret[0]) {
            ret = ch + ret;
        }
        else {
            ret += ch;
        }
    }
    return ret;
}

int main() {
    int T;
    cin >> T;
    string S, R;
    for (int c = 1; c <= T; c++) {
        cin >> S;
        R = solve(S);
            cout << "Case #" << c << ": " << R << endl;
    }

    return 0;
}