#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    freopen("A-small.out", "w", stdout);

    int T;
    scanf("%d", &T);

    int case_test = 1;
    while( case_test <= T )
    {
        int x, y, a[4][4], b[4][4];

        scanf("%d", &x);

        for( int i = 0; i < 4; i++ )
        for( int j = 0; j < 4; j++ )
        scanf("%d", &a[i][j]);

        scanf("%d", &y);

        for( int i = 0; i < 4; i++ )
        for( int j = 0; j < 4; j++ )
        scanf("%d", &b[i][j]);

        int c[4];
        for( int i = 0; i < 4; i++ )
        c[i] = a[x-1][i];

        int br = 0, k = -1;
        for( int i = 0; i < 4; i++ )
        for( int j = 0; j < 4; j++ )
        if( c[i] == b[y-1][j] )  { br++; k = c[i]; }

        printf("Case #%d: ", case_test);
        if( br == 1 )  printf("%d\n", k);
        else if( br == 0 )  printf("Volunteer cheated!\n");
        else                printf("Bad magician!\n");

        case_test++;
    }

    return 0;
}
