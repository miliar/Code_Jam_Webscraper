#include <cstdio>
 
int a[100][100], b[100][100];
 
int main()
{
        int n = 4;
        int col;
        scanf("%d", &col);
        for ( int i = 0; i < col; i++)
        {
                printf("Case #%d: ", i + 1);
                int x, y, fl = 0, res = -1;
                scanf("%d", &x);
                for ( int i = 0; i < n; i++)
                        for ( int j = 0; j < n; j++)
                                scanf("%d", &a[i][j]);
                scanf("%d", &y);
                y--;
                x--;
                for ( int i = 0; i < n; i++)
                        for ( int j = 0; j < n; j++)
                                scanf("%d", &b[i][j]);
                for ( int i = 0; i < n; i++)
                {
                        for ( int j = 0; j < n; j++)
                        {
                                if ( a[x][i] == b[y][j])
                                {
                                        fl++;
                                        res = a[x][i];
                                }
                        }
                }
                if ( fl == 0)
                        printf("Volunteer cheated!\n");
                if ( fl == 1)
                        printf("%d\n", res);
                if ( fl > 1)
                        printf("Bad magician!\n");     
        }
 
        return 0;
}
