#include <iostream>
#include <cstdio>
using namespace std;

int n,m;

bool check(int a[][102], int line, int column)
{
    int min_line = a[line][column], min_column = a[line][column];
    int max_line = min_line; int max_column = min_column;
    for(int j = 1; j<=m; j++)
        if( a[line][j] < min_line )
            for(int k = 1; k <= n; k++ )
                if( a[k][j] > a[line][j])
                    min_line = a[line][j];

    for(int i = 1; i <= n; i++)
        if( a[i][column] < min_column)
            for(int k = 1; k <= m; k++)
                if( a[i][k] > a[i][column] )
                    min_column = a[i][column];

    for(int j = 1; j<=m; j++)
        if( a[line][j] > max_line )
    //        for(int k = 1; k <= n; k++ )
      //          if( a[k][j] < a[line][j])
                    max_line = a[line][j];

    for(int i = 1; i <= n; i++)
        if( a[i][column] > max_column)
    //        for(int k = 1; k <= m; k++)
      //          if( a[i][k] < a[i][column] )
                    max_column = a[i][column];

    if( ((min_line == a[line][column]) || (min_column == a[line][column])) && ((max_line == a[line][column]) || (max_column == a[line][column]) ))
        return true;
    else
        return false;

}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);

    int T;

    int a[102][102];

    scanf("%d",&T);

    for(int i=1; i<=T; i++)
    {
        scanf("%d%d",&n,&m);

        bool possible = true;

        int j,k;
        for(j=1; j<=n; j++)
            for(k=1;k<=m; k++)
                scanf("%d",&a[j][k]);

        for(j=1; j<=n; j++)
        {
            a[j][0] = 100;
            a[j][m+1] = 100;
        }

        for(j=1; j<=m; j++)
        {
            a[0][j] = 100;
            a[n+1][j] = 100;
        }

  /*      for(j=2; j<n; j++)
            for(k=2; k<m; k++)
                if( !check(a,j,k) )
                    possible = false;
        if( (m != 1) && (n != 1))
        {
            for(j=2; j<n; j++)
            {
                if( ((a[j][1] < a[j-1][1]) && (a[j][1] < a[j][2])) || ((a[j][1] < a[j+1][1]) && (a[j][1] < a[j][2])) )
                    possible = false;
                if( ((a[j][m] < a[j-1][m]) && (a[j][m] < a[j][m-1])) || ((a[j][m] < a[j+1][m]) && (a[j][m] < a[j][m-1])) )
                    possible = false;
            }

            for( j=2; j<m; j++)
            {
                if( ((a[1][j] < a[1][j-1]) && (a[i][j] < a[2][j])) || ((a[1][j] < a[1][j+1]) && (a[1][j] < a[2][j])) )
                    possible = false;
                if( ((a[n][j] < a[n][j-1]) && (a[n][j] < a[n-1][j])) || ((a[n][j] < a[n][j+1]) && (a[n][j] < a[n-1][j])) )
                    possible = false;
            }
            if( (a[1][1] < a[1][2]) && (a[1][1]< a[2][1]) )
                possible = false;
            if( (a[1][m] < a[1][m-1]) && ( a[1][m] < a[2][m]) )
                possible = false;
            if( (a[n][m] < a[n-1][m]) && (a[n][m] < a[n][m-1]) )
                possible = false;
            if( (a[n][1] < a[n-1][1]) && (a[n][1] < a[n][2]) )
                possible = false;

        }
*/
        for(j=1; j<=n; j++)
            for(k=1; k<=m; k++)
                if( !check(a,j,k) )
                    possible = false;
        if( (m != 1) && (n != 1))
        {
            for(j=2; j<n; j++)
            {
                if( ((a[j][1] < a[j-1][1]) && (a[j][1] < a[j][2])) || ((a[j][1] < a[j+1][1]) && (a[j][1] < a[j][2])) )
                    possible = false;
                if( ((a[j][m] < a[j-1][m]) && (a[j][m] < a[j][m-1])) || ((a[j][m] < a[j+1][m]) && (a[j][m] < a[j][m-1])) )
                    possible = false;
            }
        }

        if (possible)
            printf("Case #%d: YES\n",i);
        else
            printf("Case #%d: NO\n",i);

    }

    return 0;
}
