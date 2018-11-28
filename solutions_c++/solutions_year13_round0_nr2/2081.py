#include <iostream>
#include <fstream>
using namespace std;

ifstream inf("Input.txt");
ofstream outf("Output.txt");

int main() {
    int T; inf >> T;
    for (int tc = 1; tc <= T; tc++) {
        outf << "Case #" << tc << ": ";
        int N, M;
        int field[110][110];
        int mn[110], mx[110];
        inf >> N >> M;
        for (int j = 0; j < M; j++) {
            mn[j] = 1;
            mx[j] = 100;
        }
        bool possible = true;
        for (int i = 0; i < N; i++) {
            int c = 1;
            for (int j = 0; j < M; j++) {
                inf >> field[i][j];
                c = max(c, field[i][j]);
            }
            for (int j = 0; j < M; j++) {
                if (field[i][j] < c) {
                    if (field[i][j] < mn[j] || field[i][j] > mx[j])
                        possible = false;
                    else
                        mn[j] = mx[j] = field[i][j];
                } else if (field[i][j] == c) {
                    if (field[i][j] > mx[j])
                        possible = false;
                    else
                        mn[j] = max(field[i][j], mn[j]);
                }
            }
        }
        if (possible) outf << "YES\n";
        else outf << "NO\n";
    }
}
