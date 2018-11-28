
#include <iostream>
#include <vector>

using namespace std;

struct figure {
    vector<char> data;
    int n, w, h;

    figure(int size) {
        n = size, w = 0, h = 0;
        data.assign(n * n, 0);
    }
    figure(const figure &f) {
        n = f.n, w = f.w, h = f.h;
        data = f.data;
    }

    inline char get(int i, int j) const {
        return data[i * n + j];
    }
    inline void set(int i, int j, char c) {
        data[i * n + j] = c;
    }

    bool equals(const figure &other) {
        if (n != other.n || w != other.w || h != other.h)
            return false;
        for (int i = 0; i < n * n; i++)
            if (data[i] != other.data[i])
                return false;
        return true;
    }

    void display() {
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++)
                cerr << (get(i, j) ? 'x' : ' ');
            cerr << endl;
        }
        cerr << endl;
    }
};

void update(vector<figure> &A, figure &f) {
    for (int n = A.size(), i = 0; i < n; i++)
        if (f.equals(A[i]))
            return;
    A.push_back(f);
}

vector<figure> generate(int N) {
    if (N == 1) {
        figure unit(1);
        unit.w = unit.h = 1;
        unit.data[0] = 1;
        return vector<figure>(1, unit);
    }
    vector<figure> prev = generate(N - 1);
    vector<figure> next;
    int i, j, k;
    for (i = 0; i < (int)prev.size(); i++) {
        const figure &f = prev[i];
        for (j = 0; j < f.w; j++)
            for (k = 0; k < f.h; k++)
                if (!f.get(k, j)) {
                    figure t(f);
                    t.set(k, j, 1);
                    update(next, t);
                }
        for (j = 0; j < f.w; j++) {
            for (int side = 0; side <= 1; side++)
            if (f.get(side ? f.h - 1 : 0, j)) {
                figure t(N);
                for (int y = 0; y < f.h; y++)
                    for (int x = 0; x < f.w; x++)
                        t.set(y + !side, x, f.get(y, x));
                t.set(side ? f.h : 0, j, 1);
                t.w = f.w, t.h = f.h + 1;
                update(next, t);
            }
        }
        for (k = 0; k < f.h; k++) {
            for (int side = 0; side <= 1; side++)
            if (f.get(k, side ? f.w - 1 : 0)) {
                figure t(N);
                for (int y = 0; y < f.h; y++)
                    for (int x = 0; x < f.w; x++)
                        t.set(y, x + !side, f.get(y, x));
                t.set(k, side ? f.w : 0, 1);
                t.w = f.w + 1, t.h = f.h;
                update(next, t);
            }
        }
    }
    return next;
}

int flood(int *A, int R, int C, int y, int x) {
    A[y * C + x] = 1;
    int n = 1;
    if (y > 0 && !A[(y - 1) * C + x])
        n += flood(A, R, C, y - 1, x);
    if (y < R - 1 && !A[(y + 1) * C + x])
        n += flood(A, R, C, y + 1, x);
    if (x > 0 && !A[y * C + x - 1])
        n += flood(A, R, C, y, x - 1);
    if (x < C - 1 && !A[y * C + x + 1])
        n += flood(A, R, C, y, x + 1);
    return n;
}

bool check1(int *A, int R, int C, int X) {
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            if (!A[i * C + j]) {
                int n = flood(A, R, C, i, j);
                if (n % X)
                    return true;
            }
    return false;
}

bool check(const figure &F, int R, int C, int X) {
    bool fit = (F.w <= C && F.h <= R),
         fit_turn = (F.w <= R && F.h <= C);
    if (!fit)
        return !fit_turn;
    if (R >= F.h + 2 && C >= F.w + 2)
        return false;

    int x, y, i, j;
    for (y = R - F.h; y >= 0; y--) {
        for (x = C - F.w; x >= 0; x--) {
            vector<int> A(R * C, 0);
            for (i = 0; i < F.h; i++)
                for (j = 0; j < F.w; j++)
                    if (F.get(i, j))
                        A[(y + i) * C + (x + j)] = -1;
            if (!check1(&A[0], R, C, X))
                return false;
        }
    }
    return true;
}

bool solve(int X, int R, int C) {
    if (X >= 7) return true;
    if (X >= 1 + 2 * std::min(R, C)) return true;
    if ((R * C) % X) return true;
    vector<figure> A = generate(X);
    for (int n = A.size(), i = 0; i < n; i++)
        if (check(A[i], R, C, X))
            return true;
    return false;
}

main() {
    int T, X, R, C, i;
    cin >> T;
    for (i = 0; i < T; i++) {
        cin >> X >> R >> C;
        bool res = solve(X, R, C);
        cout << "Case #" << (i + 1) << ": " << (res ? "RICHARD" : "GABRIEL") << endl;
    }
}
