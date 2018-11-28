# include <math.h>
# include <stdio.h>
# include <stdlib.h>
# include <string.h>

# define PN printf("\n")
# define PI 3.1415926536
# define MAXINT 0x7fffffff
# define GetMax(a, b) ((a)>(b)?(a):(b))
# define GetMin(a, b) ((a)<(b)?(a):(b))

# define MAXN 9

int map[MAXN][MAXN];
int graph[MAXN][MAXN];

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t, i, j, cnt = 1, row_a, row_b, count, c;
    scanf("%d", &t);
    while(cnt <= t)
    {
        printf("Case #%d: ", cnt++);
        scanf("%d", &row_a);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                scanf("%d", &map[i][j]);
        scanf("%d", &row_b);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                scanf("%d", &graph[i][j]);
        for(i = 1, count = 0; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                if(map[row_a][i] == graph[row_b][j])
                    count++,
                    c = map[row_a][i];
        if(count)
        {
            if(count == 1)
                printf("%d\n", c);
            else
                puts("Bad magician!");
        }
        else
            printf("Volunteer cheated!\n");
    }
    return 0;
}
