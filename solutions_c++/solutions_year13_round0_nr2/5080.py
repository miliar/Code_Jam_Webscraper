#include <cstdio>
#include <iostream>

using namespace std;

const char in[]  = "B-large.in.txt";
const char out[] = "B.out.txt";

int a[100][100] = {0};

int main(void)
{
    freopen(in, "rt", stdin);
    freopen(out, "wt", stdout);
    
    int T = 0;
    scanf("%d", &T);
    
    for (int casenum = 1; casenum <= T; ++casenum)
    {
        bool result = true;
        int rows, cols;
        scanf("%d%d", &rows, &cols);
              
        for ( int i=0; i<rows; ++i )
            for ( int j=0; j<cols; ++j )
                cin >> a[i][j];
        
        if ( rows == 1 || cols == 1 )
            goto L1;
        
        for ( int i=0; i<rows; ++i )
            for ( int j=0; j<cols; ++j )
            {
                for ( int k=0; k<cols; ++k )
                {
                    if ( a[i][k] > a[i][j] )
                    {
                        for ( int m = 0; m<rows; ++m )
                        {
                            if ( a[m][j] > a[i][j] )
                            {
                                result = false;
                                goto L1;
                            }
                        }
                    }
                }
            }
        
L1:
        printf("Case #%d: %s\n", casenum, result ? "YES" : "NO");
    }
}
