#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define DEBUG(x) cout << '>' << #x << ':' << (x) << endl;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int row1, row2, cnt[20];

        // init
        for (int i = 0; i < 20; ++i)
            cnt[i] = 0;

        // first square
        cin >> row1;
        for (int i = 1; i <= 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                int x;
                cin >> x;
                if (i == row1) cnt[x]++;
            }
        }

        // second square
        cin >> row2;
        for (int i = 1; i <= 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                int x;
                cin >> x;
                if (i == row2) cnt[x]++;
            }
        }

        // count twos
        int twos = 0, res = 0;
        for (int i = 1; i <= 16; ++i)
            if (cnt[i] == 2) {
                twos++;
                res = i;
            }

        cout << "Case #" << t << ": ";
        if (twos == 1)
            cout << res << endl;
        else if (twos > 1)
            cout << "Bad magician!" << endl;
        else
            cout << "Volunteer cheated!" << endl;
    }

    return 0;
}