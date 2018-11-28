#include <iostream>

const size_t N = 111;
const size_t M = 111;
const int DEF = 100;

int heights[N][M];
int rowmax[N];
int colmax[M];

using namespace std;

int main() {

    size_t T, n, m;
    cin >> T;
    for (size_t casen = 1; casen <= T; ++casen) {
        cout << "Case #" << casen << ": ";
        cin >> n >> m;
        for (int i = 0; i < n; ++i) rowmax[i] = 0;
        for (int j = 0; j < m; ++j) colmax[j] = 0;
        for (int l = 0; l < n; ++l) {
            for (int c = 0; c < m; ++c) {
                cin >> heights[l][c];
                rowmax[l] = max(rowmax[l], heights[l][c]);
                colmax[c] = max(colmax[c], heights[l][c]);
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (rowmax[i] > heights[i][j] && colmax[j] > heights[i][j]) {
                    cout << "NO\n";
                    goto endcase;
                }
            }
        }
        cout << "YES\n";
        endcase:
        casen; // nope
    }
}