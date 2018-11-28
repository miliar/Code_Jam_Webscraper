#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    int canbe[4] = {};
    for (int l0 = 0; l0 < t; l0++) {
        int row = 0;
        cin >> row;
        for (int l1 = 0; l1 < 4; l1++) {
            int q;
            for (int l2 = 0; l2 < 4; l2++) {
                cin >> q;
                if (l1 + 1 == row) canbe[l2] = q;
            }
        }
        cin >> row;
        int ans = -1;
        for (int l1 = 0; l1 < 4; l1++) {
            int q;
            for (int l2 = 0; l2 < 4; l2++) {
                cin >> q;
                if (l1 + 1 == row) {
                    for (int l3 = 0; l3 < 4; l3++) {
                        if (canbe[l3] == q) {
                            if (ans != -1) {
                                ans = -2;
                            } else {
                                ans = q;
                            }
                        }
                    }
                }
            }
        }
        cout << "Case #" << l0 + 1 << ": ";
        if (ans == -1) cout << "Volunteer cheated!\n";
        else if (ans == -2) cout << "Bad magician!\n";
        else cout << ans << '\n';
    }
    return 0;
}
