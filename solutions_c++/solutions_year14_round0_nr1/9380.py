/*
 *       Filename:  A.cpp
 *    Description: 
 *         Author:  Wenzheng Jiang , jwzh.hi@gmail.com
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, const char *argv[])
{

    int T;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    for(int nc = 1; nc <= T; nc++){
        int l, ret = -1, cnt = 0;
        int a[5][5];
        bool vis[20];
        memset(vis, false, sizeof(vis));

        for(int k = 0 ; k < 2; k++) {
            scanf("%d",&l);
            for(int i = 1; i <= 4; i++)
                for(int j = 1; j <= 4; j++)
                    scanf("%d",&a[i][j]);
            for(int j = 1; j <= 4; j++){
                int v = a[l][j];
                if(vis[v]) {
                    ret = v;
                    cnt++;
                }
                else vis[v] = true;
            }
        }

        printf("Case #%d: ", nc);
        if(cnt == 0) puts("Volunteer cheated!");
        else if(cnt > 1) puts("Bad magician!");
        else printf("%d\n", ret);
    }
    return 0;
}

