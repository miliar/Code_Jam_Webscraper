#include <stdio.h>

#define f(i,n) for(int i=0;i<n;i++)

using namespace std;

int main()
{
    int T; scanf("%d", &T);
    int n, m;
    int l[101][101];
    int rm[101]; int cm[101];
    int rowmax = 0, colmax = 0;
    for (int c = 1; c <= T; c++)
    {
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++)
        {            
            rowmax = 0;
            for (int j = 0; j < m; j++)
            {
                scanf("%d", &l[i][j]);        
                if (l[i][j] > rowmax)
                    rowmax = l[i][j];
            }
            rm[i] = rowmax;
        }   
        
        for (int i = 0; i < m; i++)
        {
            colmax = 0;
            for (int j = 0; j < n; j++)
            {
                if (l[j][i] > colmax)
                    colmax = l[j][i];
            }
            cm[i] = colmax;
        }
        
        // f(i,n)
        //     printf("%d ", rm[i]);
        // printf("\n");
        // f(j,m)
        //     printf("%d ", cm[j]);
        // printf("\n");

        bool ok = true;
        for (int i = 0; i < n; i++)
        {
            int rmax = rm[i];
            for (int j = 0; j < m; j++)
            {
                int cmax = cm[j];
                if (l[i][j] < rmax && l[i][j] < cmax)
                    ok = false;

            }
        }

        if (ok)
            printf("Case #%d: YES\n", c);
        else
            printf("Case #%d: NO\n", c);
    }
}

