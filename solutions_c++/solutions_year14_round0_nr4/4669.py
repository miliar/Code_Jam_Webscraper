#include <stdio.h>
#include <stdlib.h>

void sort(double *a, double n);
void dsort(double *a, double n);

int main()
{
    int t, d, i,j, war, dwar;
    double n, naomi[2000], ken[2000];
    freopen("large.in", "r", stdin);
    freopen("war.out", "w", stdout);

    scanf("%d", &t);

    for(d=0; d<t; d++)
    {
        scanf("%lf", &n);
        for(i=0; i<n; i++)
           scanf("%lf", &naomi[i]);

        for(i=0; i<n; i++)
           scanf("%lf", &ken[i]);

        sort(naomi, n);
        sort(ken, n);

        {
        i=0;
        war=0;
        for(j=0; j<n;)
        {
            if(ken[j]>naomi[i])
            {
                war=war+1;
                i++;
                j++;
            }
            else
                j++;
        }
        war=n-war;
        }

        {
            dsort(ken, n);
            dsort(naomi,n);
            i=0;
            dwar=0;
            for(j=0;j<n;)
            {
                if(naomi[i]>ken[j])
                {
                    i++;
                    j++;
                    dwar=dwar+1;
                }
                else
                    j++;
            }
        }

        printf("Case #%d: %d %d\n", d+1, dwar, war);
         }
         return 0;
   }




void sort(double *a, double n)
{
    int i, j;
    double t;
    for (i=1 ; i<=n-1; i++)
    {
      j=i;

      while ( j > 0 && a[j] < a[j-1])
      {
      t = a[j];
      a[j] = a[j-1];
      a[j-1] = t;

      j--;
    }
  }
}

void dsort(double *a, double n)
{
    int i, j;
    double t;
    for (i = 1 ; i<= n - 1; i++) {
    j=i;

    while ( j > 0 && a[j] > a[j-1]) {
      t = a[j];
      a[j] = a[j-1];
      a[j-1] = t;

      j--;
    }
  }
}
