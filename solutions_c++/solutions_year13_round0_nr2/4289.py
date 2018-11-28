#include <iostream>
#include <fstream>
using namespace std;

int n, m;
int a[100][100];

bool test( int x, int y )
{
    int i;
        int num1 = 0, num2 = 0;
        for( i = 0; i < n; i++ )
        {
            if( a[i][y] <= a[x][y] )
                num1++;
        }
        for( i = 0; i < m; i++ )
        {
            if( a[x][i] <= a[x][y] )
                num2++;
        }
        if( num1 == n || num2 == m )
            return true;
        else
            return false;
}

int main()
{
    ifstream cin("B-large.in");
    ofstream cout("b.txt");
    int t;
    cin >> t;
    int i,j,k;

    for( k = 1; k <= t; k++ )
    {
        cin >> n >> m;
        for( i = 0; i < n; i++ )
            for( j = 0; j < m; j++ )
                cin >> a[i][j];
        bool result = true;
        for( i = 0; i < n; i++ )
        {
            for( j = 0; j < m; j++ )
            {
 //               cout << test(i, j);
                if( test(i, j) == false )
                {
                    result = false;
                    break;
                }
            }
//            cout << endl;
            if( !result )
                break;
        }
        if( result )
            cout << "Case #" << k << ": YES" << endl;
        else
            cout << "Case #" << k << ": NO" << endl;
    }
    return 0;
}
