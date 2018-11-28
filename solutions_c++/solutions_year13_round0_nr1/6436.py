#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;
#define FOR(i, a, b) for(int i=a; i<=b; i++)
#define DOW(i, a, b) for(int i=a; i>=b; i--)
#define FOREACH(it, c) for(typeof(c.begin()) it=c.begin(); it!=c.end(); it++)
#define RESET(c, val) memset(c, val , sizeof(c))

char a[100][100];
int test;

bool cc(char k) {
    FOR(i, 1, 4) 
        if (a[i][1]==a[i][2] && a[i][2]==a[i][3] && a[i][3]==a[i][4] && a[i][4]==k) return true;
    FOR(i, 1, 4) 
        if (a[1][i]==a[2][i] && a[2][i]==a[3][i] && a[3][i]==a[4][i] && a[4][i]==k) return true;
    if (a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[3][3]==a[4][4] && a[4][4]==k) return true;
    if (a[1][4]==a[2][3] && a[2][3]==a[3][2] && a[3][2]==a[4][1] && a[4][1]==k) return true;
    return false;    
}

int main() {
    freopen("a2.in", "r", stdin);
    freopen("test.out", "w", stdout);
    scanf("%d\n", &test);
    FOR(t, 1, test) {
        int X=0, Y=0;
        bool flag=false;
        FOR(i, 1, 4) {
            FOR(j, 1, 4) {
                scanf("%c", &a[i][j]); 
                if (a[i][j]=='.') flag=true;
                if (a[i][j]=='T') X=i, Y=j;
            }
            scanf("\n");
        }
        scanf("\n");
        a[X][Y]='X';
        bool SX=cc('X');
        a[X][Y]='O';
        bool SO=cc('O');
        printf("Case #%d: ", t);
        if (SX && (!SO)) printf("X won\n");
        else if (SO && (!SX)) printf("O won\n");
        else if (SX && SO) printf("Draw\n");
        else if (flag) printf("Game has not completed\n");
        else printf("Draw\n");
        //scanf("\n");
    }
    //system("pause");
    return 0;
}
