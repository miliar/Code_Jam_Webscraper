#include <stdio.h>

int sq (int a)
{
    return a*a;
}

int main ()
{
    freopen ("Bullseye10.in","r",stdin);
    freopen ("Bullseye10.out","w",stdout);
    int n,r,t,i,j=0,k;
    scanf ("%d",&n);
    for (i=0;i<n;i++)
        {
            scanf ("%d %d",&r,&t);
            k = 0; j = sq(r+1)-sq(r++);
            while (j<=t)
                {
                    j-=sq(++r);
                    j+=sq(++r);
                    k++;
                }
            printf ("Case #%d: %d\n",i+1,k);
        }
    scanf (" ");
    return 0;
}
