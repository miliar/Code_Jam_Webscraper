#include <cstdio>
#define NMAX 125
int tests, r, c;
char A[NMAX][NMAX];

inline int isValid(int i, int j)
{
    return 1 <= i && i <= r && 1 <= j && j <= c;
}

inline int go(int i, int j)
{
    if (A[i][j] == '.')
        return 0;
    
    int dx, dy;
    switch (A[i][j])
    {
        case '^':
            dx = -1;
            dy = 0;
            break;
        case '>':
            dx = 0;
            dy = 1;
            break ;
        case 'v':
            dx = 1;
            dy = 0;
            break ;
        case '<':
            dx = 0;
            dy = -1;
            break ;
    }
    
    i += dx; j += dy;
    while (isValid(i, j))
    {
        if (A[i][j] != '.')
            return 0;
        
        i += dx;
        j += dy;
    }
    
    return 1;
}

inline int check(int i, int j)
{
    char pos[] = {'^', '>', '<', 'v'};
    for (int idx = 0; idx < 4; idx++)
    {
        A[i][j] = pos[idx];
        if (!go(i, j))
            return 1;
    }
    return 0;
}

int main()
{
    freopen("pegman.in", "r", stdin);
    freopen("pegman.out", "w", stdout);
    
    scanf("%d\n", &tests);
    for (int test_no = 1; test_no <= tests; test_no++)
    {
        scanf("%d%d\n", &r, &c);
        for (int i = 1; i <= r; i++)
            fgets(A[i] + 1, NMAX, stdin);
            
        int res = 0;
        bool impos = false;
        for (int i = 1; i <= r; i++)
        {
            for (int j = 1; j <= c; j++)
            {
                res += go(i, j);
                if (go(i, j) && !check(i, j))
                    impos = true;
            }
        }
        
        printf("Case #%d: ", test_no);
        if (impos)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", res);
    }
    return 0;
}
