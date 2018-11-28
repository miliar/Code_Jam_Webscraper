#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

int a[6][6], b[6][6], x, y;
int main () {
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-output.txt", "w", stdout);
    int Case;
    scanf("%d", &Case);
    for(int kase = 1; kase <= Case; ++kase) {
        scanf("%d", &x);
        for(int i = 1; i <= 4; ++i)
            for(int j = 1; j <= 4; ++j) scanf("%d", &a[i][j]);

        scanf("%d", &y);
        for(int i = 1; i <= 4; ++i)
            for(int j = 1; j <= 4; ++j) scanf("%d", &b[i][j]);
        int ans = 0, num;
        for(int i = 1; i <= 4; ++i) if(a[x][1] == b[y][i]) ans++, num = a[x][1];
        for(int i = 1; i <= 4; ++i) if(a[x][2] == b[y][i]) ans++, num = a[x][2];
        for(int i = 1; i <= 4; ++i) if(a[x][3] == b[y][i]) ans++, num = a[x][3];
        for(int i = 1; i <= 4; ++i) if(a[x][4] == b[y][i]) ans++, num = a[x][4];
        printf("Case #%d: ", kase);
        if(ans == 1) printf("%d\n", num);
        else if(ans == 0) printf("Volunteer cheated!\n");
        else if(ans > 1) printf("Bad magician!\n");
    }
    return 0;
}
