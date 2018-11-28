#include <bits/stdc++.h>
using namespace std;
const int MAXN = 3 + 1;
const int MAXM = (1 << MAXN) + 5;

int T, N, R, P, S;

char path[MAXM], temp[MAXM];

char result(char a, char b) {
    if (a == 'R' && b == 'S') return 'R';
    if (a == 'S' && b == 'R') return 'R';
    if (a == 'S' && b == 'P') return 'S';
    if (a == 'P' && b == 'S') return 'S';
    if (a == 'P' && b == 'R') return 'P';
    if (a == 'R' && b == 'P') return 'P';
}

bool check() {
    strcpy(temp, path);
    for (int i = (1 << N); i > 1; i >>= 1) {
        for (int j = 0; j < (i >> 1); ++j) {
            if (temp[j * 2] == temp[j * 2 + 1]) {
                return false;
            }
            temp[j] = result(temp[j * 2], temp[j * 2 + 1]);
        }
    }
    return true;
}

bool gen(int d, int R, int P, int S) {
    if (R == 0 && P == 0 && S == 0) {
        path[d] = 0;
        if (check()) {
            return true;
        }
        return false;
    }
    if (P) {
        path[d] = 'P';
        if (gen(d + 1, R, P - 1, S)) {
            return true;
        }
    }
    if (R) {
        path[d] = 'R';
        if (gen(d + 1, R - 1, P, S)) {
            return true;
        }
    }
    if (S) {
        path[d] = 'S';
        if (gen(d + 1, R, P, S - 1)) {
            return true;
        }
    }
    return false;
}

int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    ios::sync_with_stdio(false);
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> R >> P >> S;
        cout << "Case #" << t << ": ";
        if (gen(0, R, P, S)) {
            cout << path;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
    return 0;
}
