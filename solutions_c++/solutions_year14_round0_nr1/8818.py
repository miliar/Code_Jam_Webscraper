#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class Solver {
public:
    int a[4][4], b[4][4], row[17];
    int rowA, rowB;
    int T, curTest;
    void getData() {
        cin >> rowA;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                cin >> a[i][j];
            }
        }
        cin >> rowB;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                cin >> b[i][j];
            }
        }
    }
    void solve() {
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                row[a[i][j]] = i;
            }
        }
        int i = rowB - 1, cnt = 0;
        for(int j = 0; j < 4; j++) {
            if (row[b[i][j]] == rowA - 1) {
                cnt++;
            }
        }
        if (cnt == 1) {
            for(int j = 0; j < 4; j++) {
                if (row[b[i][j]] == rowA - 1) {
                    cout << "Case #" << curTest << ": "<< b[i][j] <<"\n";
                    break;
                }
            }
        } else if (cnt > 1) {
            cout << "Case #" << curTest << ": Bad magician!\n";
        } else {
            cout << "Case #" << curTest << ": Volunteer cheated!\n";
        }
    }
    void run() {
        cin >> T;
        for(int i = 0; i < T; i++) {
            curTest = i + 1;
            getData();
            solve();
        }
    }
};
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    Solver* s = new Solver();
    s->run();
    return 0;
}
