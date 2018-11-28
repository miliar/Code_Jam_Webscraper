#include <iostream>
#include <cstring>
#include <string>

using namespace std;
int a[102][2];

int main() {
    int tt, n, ttt = 0;

    cin >> tt;
    string s;
    while (ttt++ < tt) {
        cout << "Case #" << ttt << ": ";
        cin >> s;
        a[0][s[0] == '+'] = 0;
        a[0][1 - (s[0] == '+')] = 1;

        for (int i = 1; i < s.size(); i++) {
            if (s[i] == '+') {
                a[i][1] = min(a[i - 1][0] + 1, a[i - 1][1]);
                a[i][0] = min(a[i - 1][0] + 3, a[i - 1][1] + 1);
            } else {
                a[i][1] = min(a[i - 1][0] + 1, a[i - 1][1] + 3);
                a[i][0] = min(a[i - 1][0], a[i - 1][1] + 1);
            }
        }
        cout << a[s.size() - 1][1] << endl;
    }
}

