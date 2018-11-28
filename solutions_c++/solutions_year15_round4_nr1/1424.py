#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int R, C;
char tablero[101][101];

void mueve(int &r, int &c, char d) {
    if (d=='^')
        r--;
    else if (d=='>')
        c++;
    else if (d=='v')
        r++;
    else if (d=='<')
        c--;
}

bool hay(int r, int c, char d) {
    do {
        mueve(r, c, d);
        if ((r<0) || (c<0) || (r>=R) || (c>=C)) {
            return false;
        }
    } while (tablero[r][c]=='.');
    return true;
}

int main()
{
    int T;
    int N;
    cin >> T;
    for (int t=1;t<=T;t++) {
        cin >> R;
        cin >> C;
        int malos = 0;
        for (int r=0; r< R; r++) {
            cin >> tablero[r];
        }
        for (int r=0;(r<R) && (malos>=0);r++) {
            for (int c=0; (c<C) && (malos>=0);c++) {
                if (tablero[r][c] == '.')
                    continue;
                if (hay(r, c, tablero[r][c]))
                    continue;
                if (hay(r, c, '^') || hay(r, c, '>') || hay(r, c, 'v') || hay(r, c, '<')) {
                    malos++;
                    continue;
                }
                malos = -1;
            }
        }
        if (malos == -1)
            printf("Case #%d: IMPOSSIBLE\n", t);
        else
            printf("Case #%d: %d\n", t, malos);
    }
    return 0;
}
