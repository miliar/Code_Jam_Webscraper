#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>

#define rep(i,n) for(int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for(int i=(a); i>=(b); i--)
#define MAXN 105

using namespace std;

int board[MAXN][MAXN];
int rows[MAXN];
int cols[MAXN];
int N,M,T;

bool feasible() {
    rep(i,MAXN) rows[i]=cols[i]=0;
    rep(i,N) rep(j,M) {
        rows[i] = max(rows[i],board[i][j]);
        cols[j] = max(cols[j],board[i][j]);
    }
    rep(i,N) rep(j,M) {
        if (board[i][j]!=rows[i] && board[i][j]!=cols[j]) return false;
    }
    return true;
}

int main() {
    cin >> T;
    rep(tc,T) {
        cin >> N >> M;
        rep(i,N) rep(j,M) cin >> board[i][j];
        const char *s = (feasible()) ? "YES" : "NO";
        printf("Case #%d: %s\n",tc+1,s);
    }
}
