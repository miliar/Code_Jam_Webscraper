#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char players[][8] = {"RICHARD", "GABRIEL"};
int t, tc, x, r, c, win, tot;

int main() {
    scanf("%d", &t);

    for(tc=1;tc<=t;++tc) {
        scanf("%d%d%d",&x,&r,&c);
        if (r>c) {
            r = r^c;
            c = r^c;
            r = r^c;
        }

        win = 0;

        if (r>=3 && c>=3) {
            if (x<7) {
                tot = r * c;
                if (!(tot%x)) {
                    win = 1;
                }
            }
        } else if (x < 7) {
            tot = r * c;
            if ((x==2 && r==1 && c==2) || (x==1 && r==1 && c==1)) {
                win = 1;
            } else if (!(tot%x) && x<tot) {
                if (!(x>r && x>c) && x!=r && x!=c) {
                    win = 1;
                } else {
                    if (c>=3) {
                        if (r == 1) {
                            if (x < 3) {
                                win = 1;
                            }
                        } else {
                            if (x < 4) {
                                win = 1;
                            }
                        }
                    } else {
                        win = 1;
                    }
                }
            }
        }

        printf("Case #%d: %s\n", tc, players[win]);
    }
    return 0;
}
