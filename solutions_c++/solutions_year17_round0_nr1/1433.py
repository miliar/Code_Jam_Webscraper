#include <iostream>
#include <string>
using namespace std;

void flip(string& s, int i, int k) {
    for (int j = i; j < i+k; j++)
        s[j] = s[j] == '-' ? '+' : '-';
}

int main() {
    int t, k;
    cin >> t;
    string s;
    for (int c = 1; c <= t; c++) {
        cin >> s;
        cin >> k;

        int res = 0;
        for (int i = 0; i+k <= s.length(); i++) {
            if (s[i] == '-') {
                flip(s, i, k);
                res++;
            }
        }

        for (char ch : s) {
            if (ch != '+') {
                res = -1;
                break;
            }
        }

        cout << "Case #" << c << ": ";
        if (res == -1) cout << "IMPOSSIBLE";
        else cout << res;
        cout << endl;
    }
}
