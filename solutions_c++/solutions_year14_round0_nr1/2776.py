#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int first;
        cin >> first;
        --first;
        vector< vector<int> > v(4, vector<int>(4));
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                int current;
                cin >> current;
                v[i][j] = current;
            }
        }
        int second;
        cin >> second;
        --second;
        vector< vector<int> > v2(4, vector<int>(4, 0));
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                int current;
                cin >> current;
                v2[i][j] = current;
            }
        }
        
        int cnt = 0;
        int eq = 0;
        for (int i = 0; i < 4; ++i) {
            for (int j =0; j < 4; ++j) {
                if (v[first][i] == v2[second][j]) {
                    ++cnt;
                    eq = v[first][i];
                }
            }
        }
        if (cnt == 0) {
            cout << "Case #" << t << ": Volunteer cheated!" << endl;
        } else if (cnt == 1) {
            cout << "Case #" << t << ": " << eq << endl;
        } else {
            cout << "Case #" << t << ": Bad magician!" << endl;
        }
    }
}

int main(int argc, const char * argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    solve();
    return 0;
}

