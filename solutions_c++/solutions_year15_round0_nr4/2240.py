#include <cstdio>
#include <cstdlib>
#include <algorithm>
/*
 * 就先判R, C有沒有任何一個是X倍數(?)
 * 然後如果C是倍數，swap RC(?)
 * 接下來就用X判(?)
 * X=1, 2全部有解(?)
 * X=3, C>=2才有解(?)
 * X=4, C>=3才有解(?)
*/
const char yes[] = "GABRIEL";
const char no[] = "RICHARD";
int main(int argc, char *argv[]) {
    int t;
    scanf("%d", &t);
    for (int tat = 1; tat <= t; tat++) {
        bool isYes = false;
        int x, r, c;
        scanf("%d%d%d", &x, &r, &c);
        if ((r%x==0) || (c%x==0)) {
            if (c%x == 0) {
                int tmp = r; r = c, c = tmp;
            }
            if (x == 1 || x == 2)
                isYes = true;
            else if (x == 3 && c >= 2)
                isYes = true;
            else if (x == 4 && c >= 3)
                isYes = true;
        }
        printf("Case #%d: %s\n", tat, (isYes)?(yes):(no));
    }
    
    return 0;
}
