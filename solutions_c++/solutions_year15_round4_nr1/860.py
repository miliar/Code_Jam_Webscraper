#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

const int dir[5][2] = {{0,0},{0,1},{0,-1},{-1,0},{1,0}};
int map[105][105];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int times;
    int r,c;
    cin >> times;
    for (int t = 1; t <= times ; t ++)
    {
        cin >> r >> c;
        memset(map,0,sizeof(map));
        char temp;
        scanf("%c",&temp);

        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j ++)
            {
                scanf("%c",&temp);
                switch (temp)
                {
                    case '>': map[i][j] = 1;break;
                    case '<': map[i][j] = 2;break;
                    case '^': map[i][j] = 3;break;
                    case 'v': map[i][j] = 4;break;
                }
            }
            scanf("%c",&temp);
        }
        int ans = 0;
        bool ansflag = true;
        for (int i = 0; i < r; i++)
        {
            if (!ansflag) break;
            for (int j = 0; j < c; j++)
            {
                if (!ansflag) break;
                if (map[i][j] == 0) continue;
                int curx = i;
                int cury = j;
                int dx = dir[map[i][j]][0];
                int dy = dir[map[i][j]][1];
                curx += dx;
                cury += dy;
                while (curx >= 0 &&  curx < r && cury >=0 && cury < c)
                {
                    if (map[curx][cury] != 0) break;
                    curx += dx;
                    cury += dy;
                }
                if (curx < 0 || curx >= r || cury < 0|| cury >= c)
                {
                    bool flag = false;
                    for (int dd = 1; dd < 5; dd++)
                    {
                            curx = i;
                            cury = j;
                            dx = dir[dd][0];
                            dy = dir[dd][1];
                            curx += dx;
                            cury += dy;
                            while (curx >= 0 &&  curx < r && cury >=0 && cury < c)
                            {
                                if (map[curx][cury] != 0) break;
                                curx += dx;
                                cury += dy;
                            }
                            if (curx >= 0 &&  curx < r && cury >=0 && cury < c)
                            {
                                flag = true;
                                break;
                            }
                    }
                    if (flag == false)
                    {
                        ansflag = false;
                        break;
                    }
                    else
                    {
                        ans ++;
                    }
                }
            }
        }
        if (!ansflag)
        {
            printf("Case #%d: IMPOSSIBLE\n",t);
        }
        else{
            printf("Case #%d: %d\n",t,ans);
        }

    }
}
