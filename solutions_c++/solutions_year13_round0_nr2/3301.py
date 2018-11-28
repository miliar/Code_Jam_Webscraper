#include<cstdlib>
#include<cstdio>
#include<iostream>
using namespace std;
#define REP(i,n) for ( int i = 0; i < (n); i++ )
int plan[128][128];
bool possible;
int n,m;

void check( int a, int b ) {

    possible = true;
    REP(col,m) if (plan[a][b] < plan[a][col]) possible = false;
    if (possible) return;

    possible = true;
    REP(row,n) if (plan[a][b] < plan[row][b]) possible = false;
}

int main() {
    int t;
    scanf("%d",&t);
    REP(testNr,t) {
        possible = true;
        scanf("%d%d",&n,&m);
        REP(i,n) REP(j,m) scanf("%d",&plan[i][j]);
        REP(i,n) REP(j,m) if(possible) check(i,j);
        if (possible) printf("Case #%d: YES\n",testNr+1);
        else printf("Case #%d: NO\n",testNr+1);
    }
    return 0;
}

