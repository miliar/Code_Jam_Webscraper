#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAXN  110
#define EMPTY 0
#define MINE  1
#define FIRST 2

bool ok;
int  r, c;
int  r1, c1;
int  m;
char a[MAXN][MAXN];

void rot() {
    for(int i=0; i<MAXN; ++i) {
        for(int j=0; j+j<i; ++j) swap(a[i-j][j], a[j][i-j]);
    }
}

void C0() {
    ok = true;
    for(int i=0; i<r; ++i)
        for(int j=0; j<c; ++j) a[i][j] = MINE;
    a[0][0] = FIRST;
}

void C1() {
    ok = true;
    a[0][0] = FIRST;
    for(int i=1; i<=m; ++i) a[r-i][0] = MINE;
}

void C2() {
    if (m % 2 != 0) return;
    if (m == r*c - 2) return;
    ok = true;
    
    a[0][0] = FIRST;

    for(int i=r-1; m; m -= 2, i--) {
        a[i][0] = MINE;
        a[i][1] = MINE;        
    }    
}

void C3(int r, int c, int m) {
    int k = r*c - m;
    int i;
    if (k==2 || k==3 || k==5 || k==7) return;
    ok = true;
    
    if (k==4) {
        memset(a, MINE, sizeof(a));
        a[0][0] = FIRST;
        a[0][1] = a[1][0] = a[1][1] = EMPTY;
        return;
    }

    memset(a, 0, sizeof(a));
    a[0][0] = FIRST;
    for(i=r-1; m>=3; m -= 3, i--) a[i][0] = a[i][1] = a[i][2] = MINE;

    if (k >= 8 && k % 3 == 2) {   
        a[i][2] = MINE;        
    }

    if (k >= 10 && k % 3 == 1) {
        a[i][2] = MINE;
        a[i-1][2] = MINE;
    }
}

void C4() {
    int i;
    if (m > (r-3)*c) {
        C3(c, 3, m - (r-3)*c);
        if (!ok) return;
        ok = true;
        rot();
        for(int i=3; i<r; ++i) 
            for(int j=0; j<c; ++j) a[i][j] = MINE;
        return;
    } 
    ok = true;
    a[0][0] = FIRST;
    for(i=r-1; m>=c; m-=c, i--) 
        for(int j=0; j<c; ++j) a[i][j] = MINE;

    if (m == c - 1) {
        for(int j=2; j<c; ++j) a[i][j] = MINE;
        a[i-1][c-1] = MINE;
        return;
    }
    for(int j=0; j<m; ++j) a[i][j] = MINE;

}


int main() {
    int tc;
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        ok = false;
        memset(a, 0, sizeof(a));
        scanf("%i %i %i", &r1, &c1, &m);
        r = max(r1, c1);
        c = min(r1, c1);

        if (r*c <= m) goto result;
        if (r*c == m + 1) C0();
        else if (c==1) C1();
        else if (c==2) C2();
        else if (c==3) C3(r, c, m);
        else C4();

        
        result:

        printf("Case #%i:\n", tt);
        if (!ok) printf("Impossible\n");
        else {
            if (r != r1) rot();
            for(int i=0; i<r1; ++i) {
                for(int j=0, ch=' '; j<c1; ++j) {
                    if (a[i][j] == EMPTY) ch = '.';
                    else if (a[i][j] == MINE) ch = '*';
                    else if (a[i][j] == FIRST) ch = 'c';
                    printf("%c", ch);
                }
                    
                printf("\n");
            }
        }
    }
}