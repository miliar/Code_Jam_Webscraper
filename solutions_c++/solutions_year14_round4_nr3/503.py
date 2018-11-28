#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct xd
{
    int x0, y0, x1, y1;
}aoa;
aoa buildings[1005];

int map[1005][3005];
int usefuly[3005];

int comp(const void *x, const void *y)
{
    return (*(int*)x) - (*(int*)y);
}

int W, H, B, nH, judge;
int pos[4][2];

int bfs[15000000][3];

bool isWall(int x, int y)
{
    if (x < 0 || x >= W || y < 0) return true;
    if (map[x][y] == 1) return true;
    return false;
}

void walk(int x, int y, int p)
{
    int total = 1;
    bfs[1][0] = x;
    bfs[1][1] = y;
    bfs[1][2] = p;
    
    for (;;)
    {
        if (total == 0) break;
        int i = total;
        total--;
        
        int xx = bfs[i][0];
        int yy = bfs[i][1];
        int pp = bfs[i][2];
        if (yy == nH)
        {
            judge = 1;
            break;
        }
        
        if (map[xx][yy] == 1) continue;
        map[xx][yy] = 1;
        
        
        int mp;
        mp = (pp + 3) % 4;
        if (isWall(xx + pos[mp][0], yy + pos[mp][1]) == false)
        {
            total++;
            bfs[total][0] = xx + pos[mp][0];
            bfs[total][1] = yy + pos[mp][1];
            bfs[total][2] = mp;
        }
        mp = pp;
        if (isWall(xx + pos[mp][0], yy + pos[mp][1]) == false)
        {
            total++;
            bfs[total][0] = xx + pos[mp][0];
            bfs[total][1] = yy + pos[mp][1];
            bfs[total][2] = mp;
        }
        mp = (pp + 1) % 4;
        if (isWall(xx + pos[mp][0], yy + pos[mp][1]) == false)
        {
            total++;
            bfs[total][0] = xx + pos[mp][0];
            bfs[total][1] = yy + pos[mp][1];
            bfs[total][2] = mp;
        }
    }
}

int main()
{
    freopen("C-small-attempt5.in", "r", stdin);
    freopen("C-small-attempt5.out", "w", stdout);
    
    pos[0][0] = 0;
    pos[0][1] = 1;
    pos[1][0] = 1;
    pos[1][1] = 0;
    pos[2][0] = 0;
    pos[2][1] = -1;
    pos[3][0] = -1;
    pos[3][1] = 0;
    
    int cases;
    scanf("%d", &cases);
    
    for (int index = 1; index <= cases; index++)
    {
        scanf("%d %d %d", &W, &H, &B);
        
        for (int i = 0; i < B; i++)
        {
            scanf("%d %d %d %d", &buildings[i].x0, &buildings[i].y0, &buildings[i].x1, &buildings[i].y1);
        }
        
        /*nH = 2;
        usefuly[0] = 0;
        usefuly[1] = H - 1;
        for (int i = 0; i < B; i++)
        {
            for (int j = 0; j < nH; j++)
            {
                if (usefuly[j] == buildings[i].y0)
                {
                    goto next1;
                }
            }
            usefuly[nH] = buildings[i].y0;
            nH++;
            next1:
            for (int j = 0; j < nH; j++)
            {
                if (usefuly[j] == buildings[i].y1)
                {
                    goto next2;
                }
            }
            usefuly[nH] = buildings[i].y1;
            nH++;
            next2:;
            
            if (buildings[i].y1 != H - 1)
            {
                for (int j = 0; j < nH; j++)
                {
                    if (usefuly[j] == buildings[i].y1 + 1)
                    {
                        goto next3;
                    }
                }
                usefuly[nH] = buildings[i].y1 + 1;
                nH++;
                next3:;
            }
        }
        qsort(usefuly, nH, sizeof(int), comp);*/
        
        /*for (int i = 0; i < B; i++)
        {
            for (int j = 0; j < nH; j++)
            {
                if (usefuly[j] == buildings[i].y0)
                {
                    buildings[i].y0 = j;
                    break;
                }
            }
            for (int j = 0; j < nH; j++)
            {
                if (usefuly[j] == buildings[i].y1)
                {
                    buildings[i].y1 = j;
                    break;
                }
            }
        }*/nH = H;
        
        memset(map, 0, sizeof(map));
        for (int i = 0; i < B; i++)
        {//printf("!!!!!!!! %d %d %d %d\n", buildings[i].x0, buildings[i].y0, buildings[i].x1, buildings[i].y1);
            for (int x = buildings[i].x0; x <= buildings[i].x1; x++)
            {
                for (int y = buildings[i].y0; y <= buildings[i].y1; y++)
                {
                    map[x][y] = 1;
                }
            }
        }
        
        int ans = 0;
        for (int x = W - 1; x >= 0; x--)
        {/*printf("========\n");
            for (int xx = 0; xx < W; xx++)
            {
                for (int yy = 0; yy < nH; yy++)
                {
                    printf("%d ", map[xx][yy]);
                }printf("\n\n");
            }printf("========\n");*/
            
            if (map[x][0] == 0)
            {
                judge = 0;
                walk(x, 0, 0);
                if (judge == 1)
                {
                    ans++;
                }
            }
        }
        
        
        printf("Case #%d: %d\n", index, ans);
    }
    
    return 0;
}
