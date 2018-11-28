#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<iostream>
#include<time.h>
#include<sstream>
#include<string>
#include<string.h>
#include<algorithm>

#define nl printf("\n")

using namespace std;

int main()
{
    int T;
    scanf("%d",&T);

    for (int t = 1; t <= T; t++) {
        int rows, columns;
        scanf("%d %d",&rows,&columns);

        int pole[rows][columns];

        int maxx[columns];
        int maxy[rows];
        memset(maxx,0,sizeof(int)*columns);
        memset(maxy,0,sizeof(int)*rows);

        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < columns; x++) {
                scanf("%d",&pole[y][x]);
                maxy[y] = max(pole[y][x],maxy[y]);
                maxx[x] = max(pole[y][x],maxx[x]);
            }
        }

        bool jde_to = true;
        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < columns; x++) {
                if (pole[y][x] < maxy[y] && pole[y][x] < maxx[x]) {
                    jde_to = false;
                }
            }
        }

        if (jde_to) {
            printf("Case #%d: YES\n",t);
        } else {
            printf("Case #%d: NO\n",t);
        }

    }
}
