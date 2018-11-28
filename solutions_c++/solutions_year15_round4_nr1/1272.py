#include <iostream>
#include <string>
#define MAXX 110
using namespace std;

string T[MAXX];
int R, C;

bool visible(int x, int y, int dx, int dy) {
    x+=dx; y+=dy;
    while(x>=0 && x<R && y>=0 && y<C) {
        if (T[x][y] != '.')
            return true;
        x+=dx;
        y+=dy;
    }
    return false;
}

int main() {
    int test=0, tests; cin >> tests;
    while(++test <= tests) {
        cin >> R >> C;
        for(int i=0; i<R; i++) {
                cin >> T[i];
        }

        int outside = 0;
        bool impossible = false;
        for(int i=0; i<R; i++) {
            for(int j=0; j<C; j++) {
                int dx, dy;
                if (T[i][j] == '^') {
                    dx = -1; dy = 0;
                } else if (T[i][j] == 'v') {
                    dx = 1; dy = 0;
                } else if (T[i][j] == '>') {
                    dx = 0; dy = 1;
                } else if (T[i][j] == '<') {
                    dx = 0; dy = -1;
                } else {
                    continue;
                }

                if (!visible(i, j, dx, dy))
                    outside++;

                if (!visible(i, j, 0, 1) && !visible(i, j, 0, -1) &&
                    !visible(i, j, 1, 0) && !visible(i, j, -1, 0))
                    impossible = true;

            }
        }
        cout << "Case #" << test << ": ";
        if (impossible)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << outside << endl;
    }
}
