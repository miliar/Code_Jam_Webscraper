#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <limits>

using namespace std;
typedef std::numeric_limits< double > dbl;

ifstream input("./A-large.in");
//#define input cin
ofstream out("./out.txt");
//#define out cout

vector<vector<char>> data;
vector<vector<char>> bad;


void solve() {
    int R, C;
    input >> R >> C;
    data.resize(R);
    bad.resize(R);
    for (int i = 0; i < R; i++) {
        data[i].resize(C);
        bad[i].resize(C);
        for (int j = 0; j < C; j++) {
            input >> data[i][j];
            bad[i][j] = 0;
        }
    }

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (data[i][j] != '.')
            {
               bad[i][j] |= 1;
               break;
            }
        }
    }

    for (int i = 0; i < R; i++) {
        for (int j = C - 1; j >= 0; j--) {
            if (data[i][j] != '.')
            {
               bad[i][j] |= 2;
               break;
            }
        }
    }
    for (int i = 0; i < C; i++) {
        for (int j = 0; j < R; j++) {
            if (data[j][i] != '.')
            {
               bad[j][i] |= 4;
               break;
            }
        }
    }
    for (int i = 0; i < C; i++) {
        for (int j = R - 1; j >= 0; j--) {
            if (data[j][i] != '.')
            {
               bad[j][i] |= 8;
               break;
            }
        }
    }

    int res = 0;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (data[i][j] != '.')
            {
                if (bad[i][j] == 15) {
                    out << "IMPOSSIBLE" << endl;
                    return;
                }
                if (data[i][j] == '<' && (bad[i][j] & 1)) {
                    res++;
                    continue;
                }
                if (data[i][j] == '>' && (bad[i][j] & 2)) {
                    res++;
                    continue;
                }
                if (data[i][j] == '^' && (bad[i][j] & 4)) {
                    res++;
                    continue;
                }
                if (data[i][j] == 'v' && (bad[i][j] & 8)) {
                    res++;
                    continue;
                }
            }
        }
    }
    out << res << endl;
}

int main(int argc, char** argv)
{
    int T;
    input >> T;

    for (int t = 0; t < T; t++) {
        out << "Case #" << t + 1 << ": ";
        solve(); 
    }

    return 0;
}
