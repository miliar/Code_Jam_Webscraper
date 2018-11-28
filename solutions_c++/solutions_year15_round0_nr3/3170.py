#include <bits/stdc++.h>

using namespace std;

const int NMAX = 200005;

char S[NMAX];
int v[NMAX];
int N, T, L, X;
int Rev[NMAX];

#define I 2
#define J 3
#define K 4

int poz_mult(int x, int y) {
    if (x == 1)
        return y;
    if (y == 1)
        return x;
    if (x == y)
        return -1;
    if (x == I && y == J)
        return K;
    if (x == I && y == K)
        return -J;
    if (x == J && y == I)
        return -K;
    if (x == J && y == K)
        return I;
    if (x == K && y == I)
        return J;
    if (x == K && y == J)
        return -I;

    return 0;
}

int mult(int x, int y) {
    int sgnx = x > 0 ? 1 : -1;
    int sgny = y > 0 ? 1 : -1;

    x = x > 0 ? x : -x;
    y = y > 0 ? y : -y;

    return sgnx * sgny * poz_mult(x, y);
}

bool solve() {
    Rev[N + 1] = 1;
    for (int i = N; i >= 1; i--) {
        Rev[i] = mult(v[i], Rev[i+1]);
    }

    bool Exists[5];
    Exists[I] = Exists[J] = Exists[K] = 0;

    int current = 1;
    bool sol = false;
    for (int i = 1; i <= N && !sol; i++) {
        current = mult(current, v[i]);

        if (Exists[I] && current == K && Rev[i+1] == K) {
            sol = true;
        }

        if (current > 0)
            Exists[current] = true;
    }

    return sol;
}

int main() {
    freopen("test.in", "r", stdin);

    cin.sync_with_stdio(0);
    
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> L >> X;

        int offset = 0;
        cin >> S + 1;
        for (int k = 1; k <= L; k++) {
            if (S[k] == 'i')
                v[k] = I;
            if (S[k] == 'j')
                v[k] = J;
            if (S[k] == 'k')
                v[k] = K;
        }

        for (int j = 2; j <= X; j++) {
            offset += L;
            for (int k = 1; k <= L; k++) {
                v[k + offset] = v[k];
            }
        }

        N = X * L;

        cout << "Case #" << i << ": " << (solve() ? "YES" : "NO") << "\n";
    }

    return 0;
}
