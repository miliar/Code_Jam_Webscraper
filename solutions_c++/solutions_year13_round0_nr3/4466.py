#include <stdio.h>

int main ()
{
    freopen ("Fair and Square10.in","r",stdin);
    freopen ("Fair and Square10.out","w",stdout);
    int t,m,n,i,j,k;
    scanf ("%d",&t);
    for (i=0;i<t;i++)
        {
            k=0;
            scanf ("%d %d",&m,&n);
            for (j=m;j<=n;j++)
                if (j==1||j==4||j==9||j==121||j==484)
                    k++;
            printf ("Case #%d: %d\n",i+1,k);
        }
    scanf (" ");
    return 0;
}
