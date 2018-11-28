#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int cases;
    cin >> cases;

    for (int t = 1; t <= cases; t++) {
        int af[4][4], as[4][4];
        int ansf, anss;
        cin >> ansf;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> af[i][j];
            }
        }

        set<int> rowf;
        for (int i = 0; i < 4; i++) {
            rowf.insert(af[ansf - 1][i]);
        }

        cin >> anss;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> as[i][j];
            }
        }

        int count = 0;
        int ans = -1;
        for (int i = 0; i < 4; i++) {
            if (rowf.count(as[anss - 1][i])) {
                count++;
                ans = as[anss - 1][i];
            }
        }

        cout << "Case #" << t << ": ";
        if (count == 0) {
            cout << "Volunteer cheated!" << endl;
        } else if (count == 1) {
            cout << ans << endl;
        } else {
            cout << "Bad magician!" << endl;
        }
    }
}