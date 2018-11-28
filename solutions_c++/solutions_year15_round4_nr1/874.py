#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <queue>
using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
typedef long long ll;

const int MAXN = 110;

char s[MAXN][MAXN];

char dir[4] = {'^', '>', 'v', '<'};
int R, C;

bool check(int x, int y, int dir)
{
    //up
    if (dir == 0) {
        for (int i = x - 1; i >= 0; -- i) {
            if (s[i][y] != '.')
            {
                return true;
            }
        }
        return false;
    }
    
    //right
    if (dir == 1)
    {
        for (int i = y + 1; i < C; ++ i)
        {
            if (s[x][i] != '.') {
                return true;
            }
        }
        return false;
    }
    
    //down
    if (dir == 2)
    {
        for (int i = x + 1; i < R; ++ i)
        {
            if (s[i][y] != '.') {
                return true;
            }
        }
        return false;
    }
    
    //left
    if (dir == 3)
    {
        for (int i = y - 1; i >= 0; -- i)
        {
            if (s[x][i] != '.') {
                return true;
            }
        }
        return false;
    }
    
    return false;
}

void work()
{
    scanf("%d%d", &R, &C);
    
    for (int i = 0; i < R; ++ i)
    {
        scanf("%s", s[i]);
    }
    
    int ans = 0;
    
    for (int i = 0; i < R; ++ i)
    {
        for (int j = 0; j < C; ++ j)
        {
            if (s[i][j] == '.') continue;
            
            int flag = 0;
            
            for (int k = 0; k < 4; ++ k) {
                if (check(i, j, k)) {
                    if (dir[k] == s[i][j]) {
                        flag = 1;
                        break;
                    }
                    else {
                        flag = 2;
                    }
                }
            }
            
            if (!flag) {
                printf("IMPOSSIBLE\n");
                return;
            }
            
            if (flag == 2) {
                ++ ans;
            }
        }
    }
    
    printf("%d\n", ans);
}

int main()
{
    ios :: sync_with_stdio(false);
    int T;
    scanf("%d", &T);
    int kase = 1;
    while (T --) {
        printf("Case #%d: ", kase ++);
        work();
    }
    return 0;
}