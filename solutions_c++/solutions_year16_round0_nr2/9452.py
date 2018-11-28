#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int flip(const string& s, int pos, char c) {
    if (pos == 0) return s[0] == c ? 0 : 1;
    if (s[pos] == c) return flip(s, pos-1, c);
    return 1 + flip(s, pos-1, c == '+' ? '-' : '+');
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        string s;
        cin >> s;
        cout << "Case #" << i << ": " << flip(s, s.length()-1, '+') << endl;
    }
}
