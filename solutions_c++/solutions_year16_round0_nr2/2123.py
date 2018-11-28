#include <iostream>

using namespace std;

string s;

int main () {
    int T;
    cin >> T;
    for (int _t = 0; _t < T; ++_t) {
        cin >> s;
        int n = s.length();
        int b = 0;
        for (int i = 1; i < n; ++i) {
            if (s[i] == '+' && s[i - 1] == '-') ++b;
            if (s[i] == '-' && s[i - 1] == '+') ++b;
        }
        if (s[n - 1] == '-') ++b;

        cout << "Case #" << _t + 1 << ": " << b << endl;
    }
    return 0;
}
