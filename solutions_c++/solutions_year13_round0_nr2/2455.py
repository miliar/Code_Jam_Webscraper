#include <iostream>
using namespace std;

#define MAXN 100

int t, T, n, m;
int d[MAXN][MAXN];
bool mark_i[MAXN], mark_j[MAXN];

void printd() {
    cout << endl;
    for (int j = 0; j < m; j++) {
        cout << '\t' << mark_j[j];
    }
    cout << endl;
    for (int i = 0; i < n; i++) {
        cout << mark_i[i];
        for (int j = 0; j < m; j++) {
            cout << '\t' << d[i][j];
        }
        cout << endl;
    }
}

bool solve() {
    while (true) {
        //printd();
        int min = 1000, min_i = -1, min_j = -1;
        for (int i = 0; i < n; i++) {
            if (mark_i[i]) continue;
            for (int j = 0; j < m; j++) {
                if (mark_j[j]) continue;
                if (d[i][j] < min) {
                    min = d[i][j];
                    min_i = i;
                    min_j = j;
                }
            }
        }
        //cout << "~~~" << min_i << ", " << min_j << endl;
        if (min_i >= 0) {
            // check h
            bool ok = true;
            for (int j = 0; j < m; j++) {
                if (mark_j[j]) continue;
                if (d[min_i][j] != min) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                mark_i[min_i] = true;
                continue;
            }
            ok = true;
            for (int i = 0; i < n; i++) {
                if (mark_i[i]) continue;
                if (d[i][min_j] != min) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                mark_j[min_j] = true;
                continue;
            } else {
                return false;
            }
        } else {
            return true;
        }
    }
}

int main() {
    cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> d[i][j];
            }
        }
        for (int i = 0; i < n; i++) mark_i[i] = false;
        for (int j = 0; j < m; j++) mark_j[j] = false;
        if (solve()) {
            cout << "Case #" << (t + 1) << ": YES" << endl;
        } else {
            cout << "Case #" << (t + 1) << ": NO" << endl;
        }
    }
}
