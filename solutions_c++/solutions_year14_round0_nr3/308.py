#include <iostream>
#include <set>
#include <map>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>

using namespace std;

int main() {
    int T = 0;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cout << "Case #" << t + 1 << ": ";
        int R, C, M;
        cin >> R >> C >> M;
        int empty = R * C - M;
        cout << endl;
        if (R == 1) {
            cout << "c";
            for (int i = 0; i < C - 1 - M; ++i)
                cout << ".";
            for (int i = 0; i < M; ++i)
                cout << "*";
            cout << endl;
            continue;
        }
        if (C == 1) {
            cout << "c" << endl;
            for (int i = 0; i < R - 1 - M; ++i)
                cout << "." << endl;
            for (int i = 0; i < M; ++i)
                cout << "*" << endl;
            continue;
        }
        vector<string> result(R, string(C, '*'));
        result[0][0] = 'c';
        if (empty == 1) {
            for (int i = 0; i < R; i++)
                cout << result[i] << endl;
            continue;
        }
        int count = 4;
        int r = 2;
        int c = 2;
        result[0][1] = result[1][0] = result[1][1] = '.';
        while (count + 2 <= empty) {
            if (r < R && (c >= C || (r+c) % 2 > 0)) {
                result[r][0] = result[r][1] = '.';
                r++;
            } else if (c < C) {
                result[0][c] = result[1][c] = '.';
                c++;
            } else {
                break;
            }
            count = r * 2 + c * 2 - 4;
        }
        int x = 2;
        int y = 2;
        while (count < empty && r > 2 && c > 2) {
            count++;
            if (x >= R) {
                x = 2;
                y++;
            }
            if (x >= R)
                break;
            if (y >= C)
                break;
            result[x][y] = '.';
            x++;
        }
        if (count != empty) {
            cout << "Impossible" << endl;
        } else {
            for (int i = 0; i < R; i++)
                cout << result[i] << endl;
        }
    }
}
