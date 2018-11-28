#include <iostream>
#include <cstring>
using namespace std;

bool digitCheck (bool (* boolmap)[10], int num) {
    while (num != 0) {
        int digit = num % 10;
        (*boolmap)[digit] = true;
        num = num / 10;
    }

    bool res = true;
    for (int i = 0; i < 10; i++) {
        res = res && (*boolmap)[i];
    }
    return res;
}

int main () {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, n;
        cin >> N;
        n = N;

        if (n == 0) {
            cout << "Case #" << t << ": INSOMNIA" << endl;
            continue;
        }

        bool boolmap [10];
        bool found = false;
        memset(boolmap, 0, 10 * sizeof(bool));

        for (int i = 1; i <= 101; i++) {
            if (digitCheck(&boolmap, n)) {
                cout << "Case #" << t << ": " << n << endl;
                found = true;
                break;
            }
            n += N;
        }

        if (found) continue;
        cout << "Case #" << t << ": INSOMNIA" << endl;
    }
    return 0;
}
