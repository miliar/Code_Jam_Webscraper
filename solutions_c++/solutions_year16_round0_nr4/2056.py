#include <iostream>

using namespace std;

string s;

int main () {
    int T, k, c, s;
    cin >> T;
    for (int _t = 0; _t < T; ++_t) {
        
        cin >> k >> c >> s;
        cout << "Case #" << _t + 1 << ": ";;
        if (k > c * s) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        
        long long acc = 0;
        int acced = 0;
        for (int i = 0; i < k; ++i) {
            acc = k * acc + i;
            ++acced;
            if (acced == c) {
                cout << 1 + acc << " ";
                acced = 0;
                acc = 0;
            }
        }
        if (acced != 0) {
//            for (int i = acced; i < c; ++i) {
//                acc *= k;
//            }
            cout << 1 + acc;
        }

        cout << endl;

    }
    return 0;
}
