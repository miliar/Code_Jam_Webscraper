#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void doCase(int caseNum) {
    int N, M;

    cin >> N >> M;

    int grid[N][M];
    int rowmax[N];
    int colmax[M];
    memset(rowmax, 0, sizeof(rowmax));
    memset(colmax, 0, sizeof(colmax));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            int val;
            cin >> val;
            grid[i][j] = val;
            rowmax[i] = max(rowmax[i], val);
            colmax[j] = max(colmax[j], val);
        }
    }

    bool ok = true;
    for (int i = 0; ok && i < N; i++) {
        for (int j = 0; ok && j < M; j++) {
            int val = grid[i][j];
            if (val < rowmax[i] && val < colmax[j]) {
                ok = false;
            }
        }
    }

    cout << "Case #" << caseNum << ": " << (ok ? "YES" : "NO") << endl;
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
