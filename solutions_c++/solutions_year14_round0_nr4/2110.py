#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

namespace problemA {
    void start() {
        int T;
        cin >> T;

        for (int i = 0; i < T; i++) {
            int board[4][4], changed[4][4];
            int row1, row2;
            cin >> row1;
            row1 --;
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    cin >> board[j][k];
                }
            }
            cin >> row2;
            row2 --;
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    cin >> changed[j][k];
                }
            }

            set<int> found;
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    if (board[row1][j] == changed[row2][k]) {
                        found.insert(board[row1][j]);
                    }
                }
            }

            cout << "Case #" << (i+1) << ": ";
            if (found.size() == 0) {
                cout << "Volunteer cheated!" << endl;
            } else if (found.size() == 1) {
                cout << *(found.begin()) << endl;
            } else {
                cout << "Bad magician!" << endl;
            }
        }
    }
}

namespace problemB {
    void start() {
        cout << fixed;
        cout.precision(7);

        int T;
        cin >> T;

        for (int t = 0; t < T; t++) {
            double C, F, X;
            cin >> C >> F >> X;

            double cookies = 0.0, rate = 2.0, totalTime = 0;
            while ((C / rate) + (X / (rate + F)) < (X / rate)) {
                totalTime += (C / rate);
                rate += F;
            }
            cout << "Case #" << (t+1) << ": ";
            cout << (totalTime + X/rate) << endl;
        }
    }
}

namespace problemC {
    const int NONE = 0, CLICK = 1, BOMB = 2, FOUND = 3;

    void start() {
        int T;
        cin >> T;
        for (int t = 0; t < T; t++) {
            int R, C, M;
            cin >> R >> C >> M;

            for (int c1 = 0; c1 < R; c1++) {
                for (int c2 = 0; c2 < C; c2++) {
                    int board[R][C];
                    for (int i = 0; i < R; i++) {
                        for (int j = 0; j < C; j++) {
                            board[i][j] = NONE;
                        }
                    }
                    board[c1][c2] = CLICK;
                }
            }
        }
    }
}

namespace problemD {
    void start() {
        int T;
        cin >> T;
        for (int t = 0; t < T; t++) {
            int n;
            cin >> n;
            vector<double> naomi(n), kenv(n);
            set<double> ken, ken2, naomis;
            for (int i = 0; i < n; i++) {
                cin >> naomi[i];
                naomis.insert(naomi[i]);
            }
            double a;
            for (int i = 0; i < n; i++) {
                cin >> a;
                kenv[i] = a;
                ken.insert(a);
                ken2.insert(a);
            }

            sort(naomi.begin(), naomi.end());
            sort(kenv.begin(), kenv.end());

            int warPoints = 0;
            for (int i = 0; i < n; i++) {
                set<double>::const_iterator it = ken.upper_bound(naomi[i]);
                if (it == ken.end()) {
                    ken.erase(ken.begin());
                    warPoints ++;
                } else {
                    ken.erase(it);
                }
            }

            int deceitWarPoints = 0;
            while (naomis.size()) {
                while (naomis.size() && *(naomis.begin()) < *(ken2.begin())) {
                    //cout << "1. removing " << *(naomis.begin()) << ", " << *(ken2.rbegin()) << endl;
                    naomis.erase(naomis.begin());
                    ken2.erase(ken2.find(*(ken2.rbegin())));
                }
                while (naomis.size() && *(naomis.begin()) > *(ken2.begin())) {
                    //cout << "2. removing " << *(naomis.begin()) << ", " << *(ken2.begin()) << endl;
                    naomis.erase(naomis.begin());
                    ken2.erase(ken2.begin());
                    deceitWarPoints ++;
                }
            }

            cout << "Case #" << (t+1) << ": ";
            cout << deceitWarPoints << " " << warPoints << endl;
        }
    }
}

int main() {
    problemD::start();

    return 0;
}
