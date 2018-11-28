#include <cstdio>
#include <cstring>
using namespace std;

int T, n, m;
bool bl[50];
int a[5][5], b[5][5];
int main()
{
    scanf( "%d", &T );
    for (int I = 1; I <= T; ++I )
    {
        memset( bl, 0, sizeof(bl));
        scanf( "%d", &n );

        for ( int i = 0; i < 4; ++i )
            for ( int j = 0; j < 4; ++j )
                scanf( "%d", &a[i+1][j+1]);
        for ( int i = 0; i < 4; ++i )
            bl[a[n][i+1]] = true;

        scanf( "%d", &m );
        for ( int i = 0; i < 4; ++i )
            for ( int j = 0; j < 4; ++j )
                scanf( "%d", &b[i+1][j+1]);
        int cnt = 0, last;
        for ( int i = 0; i < 4; ++i )
            if (bl[b[m][i+1]])
            {
                cnt++;
                last = b[m][i+1];
            }
        printf( "Case #%d: ", I);
        if ( cnt == 1 )
            printf( "%d\n", last);
        else if ( cnt == 0)
            printf( "Volunteer cheated!\n");
        else
            printf( "Bad magician!\n");
    }
}
        

