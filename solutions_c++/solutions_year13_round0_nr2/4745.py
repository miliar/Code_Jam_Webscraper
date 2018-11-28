#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
using namespace std;

typedef long long LL;

typedef int matrix[105][105];

matrix mat, L, R, U, D;

void solve(int ri) {
    int r, c; cin >> r >> c;
    for ( int i = 1; i <= r; ++i ) {
        for ( int j = 1; j <= c; ++j ) {
            cin >> mat[i][j];
        }
    }
    for ( int i = 1; i <= r; ++i ) {
        L[i][0] = 0;
        for ( int j = 1; j <= c; ++j )
            L[i][j] = max(L[i][j-1], mat[i][j]);
        R[i][c+1] = 0;
        for ( int j = c; j >= 1; --j )
            R[i][j] = max(R[i][j+1], mat[i][j]);
    }
    for ( int j = 1; j <= c; ++j ) {
        U[0][j] = 0;
        for ( int i = 1; i <= r; ++i )
            U[i][j] = max(U[i-1][j], mat[i][j]);
        D[r+1][j] = 0;
        for ( int i = r; i >= 1; --i )
            D[i][j] = max(D[i+1][j], mat[i][j]);
    }
    int ok = 1;
    for ( int i = 1; i <= r; ++i ) {
        for ( int j = 1; j <= c; ++j ) {
            int o1 = max(L[i][j], R[i][j]) == mat[i][j];
            int o2 = max(U[i][j], D[i][j]) == mat[i][j];
            if ( !o1 && !o2 ) ok = 0;
        }
    }
    printf("Case #%d: %s\n", ri, ok ? "YES" : "NO");
}

int main() {
    freopen("C:/Users/john/Downloads/B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int re; cin >> re;
    for ( int ri = 1; ri <= re; ++ri ) solve(ri);
}
