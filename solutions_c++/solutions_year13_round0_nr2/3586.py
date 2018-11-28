#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    int t, i, j, x1, y1, cas;
    int maxh, maxv, n, m;
    int arr[100][100];

    bool vert[100][100];
    bool hori[100][100];

    bool result;

    scanf("%d", &t);
    cas = 0;

    while(t--)
    {
        cas++;

        scanf("%d%d", &n, &m);

        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d", &arr[i][j]);
            }
        }

        for(i=0;i<n;i++)
        {
            maxh = arr[i][0];

            for(j=1;j<m;j++)
            {
                if(maxh < arr[i][j])
                    maxh = arr[i][j];
            }

            for(j=0;j<m;j++)
            {
                if(arr[i][j] < maxh)
                    hori[i][j] = false;
                else
                    hori[i][j] = true;
            }
        }

        for(j=0;j<m;j++)
        {
            maxv = arr[0][j];

            for(i=1;i<n;i++)
            {
                if(maxv < arr[i][j])
                    maxv = arr[i][j];
            }

            for(i=0;i<n;i++)
            {
                if(arr[i][j] < maxv)
                    vert[i][j] = false;
                else
                    vert[i][j] = true;
            }
        }

        result = true;

        for(i=0; (i<n) && (result == true) ;i++)
        {
            for(j=0;j<m;j++)
            {
                if( (hori[i][j] == false) && (vert[i][j] == false) )
                {
                    result = false;
                    break;
                }
            }
        }

        if(result == true)
            printf("Case #%d: YES\n", cas);
        else
            printf("Case #%d: NO\n", cas);
    }

	return 0;
}
