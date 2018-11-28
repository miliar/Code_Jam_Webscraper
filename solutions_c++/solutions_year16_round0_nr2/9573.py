#include <iostream>
using namespace std;

void solver(string s) {
    int n = 0;
    if (s[0] == '-') {
        n = 1;
    }
    for (int i = 1; i < s.length(); i++) {
        if (s[i] == '-') {
            if (s[i-1] == '+') {
                n = n + 2;
            }
        }
    }
    cout << n << endl;
}

int main() {
    int t;
    string s;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> s;
        cout << "Case #" << i << ": ";
        solver(s);
    }
}
