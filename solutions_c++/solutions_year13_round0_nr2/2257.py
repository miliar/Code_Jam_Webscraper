#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve(int ind) {
    // input
    int N, M;
    cin >> N >> M;
    vector<vector<int> > lawn(N, vector<int>(M, 0));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> lawn[i][j];
        }
    }
    // process
    vector<vector<int> > newlawn(N, vector<int>(M, 100));
    // process row-wise
    for (int i = 0; i < N; ++i) {
        int maxh = 0;
        for (int j = 0; j < M; ++j) {
            maxh = max<int>(maxh, lawn[i][j]);
        }
        // and ride this on new lawn
        for (int j = 0; j < M; ++j) {
            newlawn[i][j] = min<int>(newlawn[i][j], maxh);
        }
    }
    // process col-wise
    for (int j = 0; j < M; ++j) {
        int maxh = 0;
        for (int i = 0; i < N; ++i) {
            maxh = max<int>(maxh, lawn[i][j]);
        }
        // and ride this on new lawn
        for (int i = 0; i < N; ++i) {
            newlawn[i][j] = min<int>(newlawn[i][j], maxh);
        }
    }
    // compare
    bool can = true;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (newlawn[i][j] != lawn[i][j]) {
                can = false;
            }
        }
    }

    // output
    cout << "Case #" << ind << ": " << (can ? "YES" : "NO") << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        solve(i);
    }
}