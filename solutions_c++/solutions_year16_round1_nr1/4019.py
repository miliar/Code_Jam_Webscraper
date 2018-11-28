#include <bits/stdc++.h>
using namespace std;

int main() {
    int T; cin >> T;
    for (int t = 0; t < T; t++) {
        string str; cin >> str;
        string crt;
        crt = string(str.begin(), str.begin() + 1);

        for (int i = 1; i < str.size(); i++) {
            if (str[i] >= crt[0]) {
                crt = str[i] + crt;
            } else {
                crt += str[i];
            }
        }

        cout << "Case #" << t+1 << ": " << crt << endl;
    }

    return 0;
}
