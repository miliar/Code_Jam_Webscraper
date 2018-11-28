#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

const int dx[4] = {0 , -1 , 0 , 1};
const int dy[4] = {1 , 0 , -1 , 0};

int T , testcase , n , m;
int data[200][200];
int ans;

void init()
{
    scanf("%d%d" , &n , &m);
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            scanf("%d" , &data[i][j]);
}

inline bool isin(int x , int y)
{
    return (x >= 1) && (x <= n) && (y >= 1) && (y <= m);
}

void work()
{
    printf("Case #%d: " , testcase);
    if (n == 1 || m == 1)
    {
        printf("YES\n");
        return;
    }
    int i , j , k , l , dir;
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= m; j++)
        {
            int flag = 0;
            int cnt = 0;
            int first[2];
            int flag_first[2];
            first[0] = first[1] = 1;
            flag_first[0] = flag_first[1] = 1;
            for (dir = 0; dir < 4; dir++)
            {
                int x = i + dx[dir] , y = j + dy[dir];
                while (isin(x , y))
                {
                    cnt += first[dir % 2];
                    if (first[dir % 2]) first[dir % 2] = 0;
                    if (data[x][y] > data[i][j])
                    {
                        flag += flag_first[dir % 2];
                        if (flag_first[dir % 2]) flag_first[dir % 2] = 0;
                        break;
                    }
                    x += dx[dir];
                    y += dy[dir];
                }
            }
            if (flag == cnt)
            {
                printf("NO\n");
                return;
            }
        }
    }
    printf("YES\n");
}

int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    scanf("%d" , &T);
    for (testcase = 1; testcase <= T; testcase++)
    {
        init();
        work();
    }
    return 0;
}
