#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

int arr[105][105];

int main ()
{
    FILE *in = fopen ("B.in","r");
    FILE *out = fopen ("B.out","w");

    int t;
    int k = 1;

    fscanf (in,"%d",&t);

    while( t -- )
    {
        int n,m;
        bool flag = true;

        fscanf (in,"%d %d",&n,&m);

        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                fscanf (in,"%d",&arr[i][j]);

        for (int i=0; i<n; i++)
        {
            for (int j=0; j<m; j++)
            {
                int mx1 = arr[i][j];
                int mx2 = arr[i][j];

                for (int k=0; k<m; k++)
                    mx1 = max( mx1 , arr[i][k] );
                for (int k=0; k<n; k++)
                    mx2 = max( mx2 , arr[k][j] );

                if (mx1 > arr[i][j] && mx2 > arr[i][j])
                {
                    flag = false;
                    break;
                }
            }

            if (flag == false)
                break;
        }

        fprintf (out,"Case #%d: ",k ++);

        if (flag == true)
            fprintf (out,"YES\n");
        else
            fprintf (out,"NO\n");
    }
}
