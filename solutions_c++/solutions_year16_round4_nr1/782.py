#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    vector<vector<string>> sol(3, vector<string>(13));
    sol[0][0] = "P";
    sol[1][0] = "R";
    sol[2][0] = "S";
    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j < 12; j++) {
            for (char c : sol[i][j]) {
                if (c == 'P') {
                    sol[i][j+1].push_back('P');
                    sol[i][j+1].push_back('R');
                }
                if (c == 'R') {
                    sol[i][j+1].push_back('R');
                    sol[i][j+1].push_back('S');
                }
                if (c == 'S') {
                    sol[i][j+1].push_back('S');
                    sol[i][j+1].push_back('P');
                }
            }
        }
    }
    /*
    cout << sol[0][1] << endl;
    cout << sol[0][2] << endl;
    cout << sol[0][3] << endl;
    cout << sol[0][4] << endl;
    */
    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 12; j++) {
            for (int k = 1; k < (1 << j); k <<= 1) {
                for (int h = 0; h < (1 << j); h += 2*k) {
                    if (sol[i][j].compare(h, k, sol[i][j], h+k, k) > 0) {
                        string s = sol[i][j].substr(h, k);
                        sol[i][j].replace(h, k, sol[i][j], h+k, k);
                        sol[i][j].replace(h+k, k, s);
                    }
                }
            }
        }
    }

    vector<vector<vector<long>>> cnt(3, vector<vector<long>>(13, vector<long>(3)));
    cnt[0][0][0] = 1;
    cnt[1][0][1] = 1;
    cnt[2][0][2] = 1;
    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j < 12; j++) {
            for (int k = 0; k <= 2; k++) {
                cnt[i][j+1][k] += cnt[i][j][k];
                cnt[i][j+1][(k+1)%3] += cnt[i][j][k];
            }
        }
    }

    long T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long N, R, P, S;
        cin >> N >> R >> P >> S;
        vector<long> tup = {P, R, S};
        //cout << tup[0] << tup[1] << tup[2] << endl;
        //cout << cnt[0][N][0] << cnt[0][N][1] << cnt[0][N][2] << endl;

        cout << "Case #" << t << ": ";
        long done = 0;
        for (int i = 0; i <= 2; i++) {
            long match = 1;
            for (int k = 0; k <= 2; k++) {
                if (cnt[i][N][k] != tup[k]) match = 0;
            }
            if (match) {
                done = 1;
                cout << sol[i][N] << endl;
            }
        }
        if (!done) cout << "IMPOSSIBLE" << endl;
    }
}
