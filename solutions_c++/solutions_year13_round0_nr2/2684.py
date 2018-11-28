#include <iostream>

using namespace std;

int main() {
    int N, M, t;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> N >> M;
        int lawn[N][M];

        for (int row = 0; row < N; ++row) {
            for (int col = 0; col < M; ++col) {
                cin >> lawn[row][col];
            }
        }

        bool rowtrace[N], coltrace[M];
        for (int row = 0; row < N; ++row) {
            bool lawned = true;
            for (int col = 0; col < M && lawned; ++col) {
                lawned = (lawn[row][col] < 2);
            }
            rowtrace[row] = lawned;
        }

        for (int col = 0; col < M; ++col) {
            bool lawned = true;
            for (int row = 0; row < N && lawned; ++row) {
                lawned = (lawn[row][col] < 2);
            }
            coltrace[col] = lawned;
        }
        
        bool possible = true;
        for (int row = 0; row < N && possible; ++row) {
            for (int col = 0; col < M && possible; ++col) {
                possible = (lawn[row][col] == 2) || rowtrace[row] || coltrace[col];
            }
        }

        cout << "Case #" << i << ": " << (possible ? "YES" : "NO") << endl;
    }
}
