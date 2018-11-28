#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        string s;
        int len, sol = 0;
        cin >> s;
        len = s.length();
        for (int i = len-1; i >= 0; i--) {
            if (s[i] == '+') {
                continue;
            }
            else {
                int j;
                for (j = 0; s[j] == '+'; j++) {
                    s[j] = '-';
                }
                if (j > 0) {
                    sol++;
                }
                string flip = s.substr(0, i+1);
                for (j = 0; j < i+1; j++) {
                    s[j] = (flip[i-j] == '+')? '-':'+';
                }
                sol++;
            }
        }
        cout << "Case #" << tc + 1 << ": " << sol << endl;
    }
    return 0;
}