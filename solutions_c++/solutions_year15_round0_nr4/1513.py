#include <iostream>
#include <fstream>
#include <string>
using namespace std;
typedef long long ll;
typedef long double ld;

int T,x,w,h;

int main()
{
    ///freopen("input.txt", "r", stdin);
    ///freopen("output.txt", "w", stdout);

    scanf("%d",&T);
    for (int TTT = 1; TTT <= T; ++TTT) {
        scanf("%d%d%d",&x,&w,&h);
        if (x == 1) printf("Case #%d: GABRIEL\n", TTT);
        else if (x == 2) {
            if (w * h % 2 == 0) printf("Case #%d: GABRIEL\n", TTT);
            else printf("Case #%d: RICHARD\n", TTT);
        } else if (x == 3) {
            if (w <= 1 || h <= 1) { printf("Case #%d: RICHARD\n", TTT); continue; }
            if (w * h % 3 == 0) printf("Case #%d: GABRIEL\n", TTT);
            else printf("Case #%d: RICHARD\n", TTT);
        } else if (x == 4) {
            if (w <= 2 || h <= 2) { printf("Case #%d: RICHARD\n", TTT); continue; }
            if ((w >= 4 || h >= 4) && w * h % 4 == 0) printf("Case #%d: GABRIEL\n", TTT);
            else printf("Case #%d: RICHARD\n", TTT);
        } else if (x == 5) {
            if (w <= 3 || h <= 3 || w * h % 5 != 0 || (w <= 4 && h <= 4)) { printf("Case #%d: RICHARD\n", TTT); continue; }
            else printf("Case #%d: GABRIEL\n", TTT);
        } else if (x == 6) {
            if (w <= 3 || h <= 3 || w * h % 6 != 0 || (w <= 5 && h <= 5)) { printf("Case #%d: RICHARD\n", TTT); continue; }
            else printf("Case #%d: GABRIEL\n", TTT);
        } else printf("Case #%d: RICHARD\n", TTT);
    }

    return 0;
}
