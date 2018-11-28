#include <cassert>
#include <cstdlib>

#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_SIZE = 100;

bool isLawnPossible(const int lawn[MAX_SIZE][MAX_SIZE], const int n, const int m);

int main() {
    int cases;
    cin >> cases;

    int lawn[MAX_SIZE][MAX_SIZE];

    for (int i = 0; i < cases; ++i) {
        int n, m;
        cin >> n >> m;

        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < m; ++k) {
                cin >> lawn[j][k];
            }
        }

        cout << "Case #" << i + 1 << ": ";
        if (isLawnPossible(lawn, n, m)) {
            cout << "YES";
        } else {
            cout << "NO";
        }
        cout << endl;
    }
}


bool isLawnPossible(
    const int lawn[MAX_SIZE][MAX_SIZE],
    const int n,
    const int m
) {
    int maxHorizontal[MAX_SIZE] = {0};
    for (int i = 0; i < n; ++i) {
        maxHorizontal[i] = lawn[i][0];
        for (int j = 1; j < m; ++j) {
            maxHorizontal[i] = max(lawn[i][j], maxHorizontal[i]);
        }
    }
    int maxVertical[MAX_SIZE] = {0};
    for (int j = 0; j < m; ++j) {
        maxVertical[j] = lawn[0][j];
        for (int i = 1; i < n; ++i) {
            maxVertical[j] = max(lawn[i][j], maxVertical[j]);
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (lawn[i][j] < maxHorizontal[i] && lawn[i][j] < maxVertical[j]) {
                return false;
            }
        }
    }
    return true;
}
