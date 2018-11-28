#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++)

using namespace std;

int test, r, c, m;

bool found = false;
int x[7][7];
int a[7][7];
bool visited[7][7];

const int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

void coutRes() {
    FOR(i, 1, r) {
        FOR(j, 1, c) {
            if (x[i][j] == 0) printf(".");
            if (x[i][j] == 1) printf("*");
            if (x[i][j] == 2) printf("c");
        }
        printf("\n");
    }
    found = true;
}

bool inSide(int x, int y) {
    return (1 <= x && x <= r && 1 <= y && y <= c);
}

void visit(int x, int y) {
    visited[x][y] = true;
    if (a[x][y] != 0) return;
    FOR(k, 0, 7) {
        if (!visited[x + dx[k]][y + dy[k]] && inSide(x + dx[k], y + dy[k]))
            visit(x + dx[k], y + dy[k]);
    }
}

void checkk(int a, int b) {
    memset(visited, false, sizeof(visited));
    visit(a, b);
    bool chose = true;
    FOR(i, 1, r)
    FOR(j, 1, c)
        if (visited[i][j] == false && x[i][j] == 0)
            chose = false;
    if (chose) {
        x[a][b] = 2;
        coutRes();
    }
}

void check() {
    memset(a, 0, sizeof(a));
    FOR(i, 1, r) FOR(j, 1, c)
    if (x[i][j] == 1) {
        FOR(k, 0, 7)
            a[i+dx[k]][j+dy[k]] = 1;
        }
    FOR(i, 1, r) FOR(j, 1, c)
        if (x[i][j] == 0) {
            if (found) break;
            checkk(i, j);
        }
}

void attempt(int i, int j, int m) {
    if (found) return;
    if ((i > r && m == 0) || m == 0) {
        check();
        return;
    }
    if (i > r)
        return;
    FOR(k, 0, 1) {
        x[i][j] = k;
        if (j == c) attempt(i+1, 1, m-k);
        else
            attempt(i, j+1, m-k);
        x[i][j] = 0;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &test);
    FOR(T, 1, test) {
        memset(x, 0, sizeof(x));
        memset(a, 0, sizeof(a));
        printf("Case #%d:\n", T);
        scanf("%d %d %d", &r, &c, &m);
        found = false;
        attempt(1, 1, m);
        if (found == false) printf("Impossible\n");
    }
    return 0;
}

