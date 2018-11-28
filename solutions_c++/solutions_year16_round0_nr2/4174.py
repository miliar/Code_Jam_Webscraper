#include <iostream>
#include <string>

using namespace std;

int t;
string s;

int main() {
    cin >> t;
    for (int _ = 1; _ <= t; _++) {
        cin >> s;
        int last_pos = s.size() - 1;
        while (last_pos >= 0 && s[last_pos] == '+') {
            last_pos--;
        }
        if (last_pos == -1) {
            cout << "Case #" << _ << ": " << 0 << endl;
        } else if (last_pos == 0) {
            cout << "Case #" << _ << ": " << 1 << endl;
        } else {
            int i = 1;
            int count = 0;
            while (i <= last_pos) {
                if (s[i] != s[i - 1]) count++;
                i++;
            }
            cout << "Case #" << _ << ": " << count + 1 << endl;
        }
    }
}