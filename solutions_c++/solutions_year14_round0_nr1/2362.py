#include <cstdio>
#include <cstring>

const int N = 10;
int t, a1, a2;
int A1[N][N], A2[N][N];
bool F[17];

int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
    int ic = 1;
    scanf("%d", &t);
    while ( t-- )
    {
        int ans, num = 0;
        memset(F, 0, sizeof(F));
        scanf("%d", &a1);
        for ( int i = 1; i <= 4; ++i )
            for ( int j = 1; j <= 4; ++j )
            {
                scanf("%d", &A1[i][j]);
                //if ( i == a1 ) F[A1[i][j]] = true;
            }
        scanf("%d", &a2);
        for ( int i = 1; i <= 4; ++i )
            for ( int j = 1; j <= 4; ++j )
            {
                scanf("%d", &A2[i][j]);
            }
        for ( int i = 1; i <= 4; i++ )
            for ( int j = 1; j <= 4; ++j ) if ( A1[a1][i] == A2[a2][j] ) num++, ans = A1[a1][i];
        printf("Case #%d: ", ic++);
        if ( num == 1 ) printf("%d\n", ans);
        else if ( num == 0 ) printf("Volunteer cheated!\n");
        else if ( num > 1 ) printf("Bad magician!\n");
    }
}
