#include <iostream>
#include <iomanip>

using namespace std;

int main() {
        freopen("B.in", "r", stdin);
        freopen("B.out", "w", stdout);
        int T;
        cin >> T;
        for (int i = 0; i < T; i ++) {
                int row0;
                cin >> row0;
                int cnt = 0;
                int cand[4];
                for (int t = 0; t < 16; t ++) {
                        int tmp;
                        cin >> tmp;
                        if (t / 4 + 1 == row0) {
                                cand[cnt] = tmp;
                                cnt ++;
                        }
                }
                cnt = 0;
                int row1;
                int ret;
                cin >> row1;
                for (int t = 0; t < 16; t ++) {
                        int tmp;
                        cin >> tmp;
                        if (t / 4 + 1 == row1) {
                                for (int j = 0; j < 4; j ++) {
                                        if (tmp == cand[j]) {
                                                cnt ++;
                                                ret = tmp;
                                                break;
                                        }
                                }
                        }
                }
                cout << "Case #" << i + 1 << ": ";
                if (cnt == 0) {
                        cout << "Volunteer cheated!" << endl;
                } else  if (cnt == 1) {
                        cout << ret << endl;
                } else {
                        cout << "Bad magician!" << endl;
                }
        } 
        return 0;
}
