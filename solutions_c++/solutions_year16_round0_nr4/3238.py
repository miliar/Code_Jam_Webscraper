#include <iostream>
#include <string>
using namespace std;

int main () {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int k, c, s;
        cin >> k; cin >> c; cin >> s;
        if (k == 1) {
            cout << "Case #" << t << ": 1" << endl;
            continue;
        }
        long long len = 1;
        for (int i = 0; i < c; i++) {
            len *= k;
        }
        len -= s;
        len /= (s - 1);
        if (c == 1) {
            len = 1;
        }
        long long pos = 1;
        cout << "Case #" << t << ":";
        for (int i = 0; i < s; i++) {
            cout << " " << pos;
            pos += len;
        }
        cout << endl;
    }
    return 0;
}
