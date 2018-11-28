#include <bits/stdc++.h>
#define sz(x) (int((x).size()))
#define pb push_back
#define eb emplace_back
#define all(x) (x).begin(), (x).end()
template<typename T> bool domax(T &a, T b) { return (b > a ? (a = b, true) : false); }
template<typename T> bool domin(T &a, T b) { return (b < a ? (a = b, true) : false); }
typedef long long ll;

const int maxn = 405;

int Y, X, p[maxn];
char g[maxn][maxn];

void clear() {
    for (int y = 0; y < maxn; y++) for (int x = 0; x < maxn; x++) {
        g[y][x] = ' ';
    }
}
bool possible() {
    std::stack<int> s;
    for (int i = 0; i < 2*(Y+X); i++) {
        if (p[i] < i) {
            if (s.empty() || s.top() != p[i]) return false;
            else s.pop();
        } else s.push(i);
    }
    assert(s.empty());
    return true;
}
void go(int &y, int &x, int &d) {
    if (g[y][x] == '\\') {
        if (d == 0) {
            x++;
            d = 3;
        } else if (d == 1) {
            y--;
            d = 2;
        } else if (d == 2) {
            x--;
            d = 1;
        } else {
            assert(d == 3);
            y++;
            d = 0;
        }
    } else {
        assert(g[y][x] == '/');
        if (d == 0) {
            x--;
            d = 1;
        } else if (d == 1) {
            y++;
            d = 0;
        } else if (d == 2) {
            x++;
            d = 3;
        } else {
            assert(d == 3);
            y--;
            d = 2;
        }
    }
}
int getplace(int y, int x) {
    if (y < 0) return x;
    else if (x >= X) return X+y;
    else if (y >= Y) return X+Y+(X-1-x);
    else return X+Y+X+(Y-1-y);
}
bool solve(int i) {
    int y, x, d;
    //char prev;
    if (i < X) {
        y = 0;
        x = i;
        d = 0;
        //prev = '\\';
    } else if (i < X+Y) {
        x = X-1;
        y = i-X;
        d = 1;
        //prev = '/';
    } else if (i < X+Y+X) {
        x = X-1 - (i-(X+Y));
        y = Y-1;
        d = 2;
        //prev = '\\';
    } else {
        x = 0;
        y = Y-1 - (i-(X+Y+X));
        d = 3;
        //prev = '/';
    }

    //printf("solve(%d), x = %d, y = %d, d = %d, prev = %c\n", i, x, y, d, prev);

    while (0 <= x && x < X && 0 <= y && y < Y) {
        //printf("x = %d, y = %d, d = %d, prev = %c\n", x, y, d, prev);
        if (g[y][x] == ' ') {
            if (d&1) {
                g[y][x] = '/';
            } else {
                g[y][x] = '\\';
            }
        }// else prev = g[y][x];
        go(y, x, d);
    }
    if (getplace(y, x) != p[i]) return false;
    return true;
}

int main() {
    int testcases; scanf("%d", &testcases);
    clear();
    for (int testnum = 1; testnum <= testcases; testnum++) {
        printf("Case #%d:\n", testnum);
        scanf("%d%d", &Y, &X);
        for (int i = 0; i < (Y+X); i++) {
            int a, b; scanf("%d%d", &a, &b); a--; b--;
            p[a] = b;
            p[b] = a;
        }
        for (int y = 0; y < Y; y++) g[y][X] = '\0';
        if (possible()) {
            bool rip = false;
            for (int i = 0; i < 2*(Y+X); i++) {
                if (p[i] < i) {
                    //printf("here's the grid so far:\n");
                    //for (int y = 0; y < Y; y++) {
                    //    printf("%s\n", g[y]);
                    //}
                    //printf("now solving %d and %d\n", p[i], i);
                    if (!solve(p[i])) {
                        rip = true;
                        break;
                    }
                }
            }
            if (rip) {
                printf("IMPOSSIBLE\n");
            } else {
                for (int y = 0; y < Y; y++) {
                    for (int x = 0; x < X; x++) if (g[y][x] == ' ') g[y][x] = '\\';
                    printf("%s\n", g[y]);
                }
            }
        } else {
            printf("IMPOSSIBLE\n");
        }
        clear();
    }
}

