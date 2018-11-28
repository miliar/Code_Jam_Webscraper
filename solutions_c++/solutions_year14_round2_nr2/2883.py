#include <cstdio>

int main ()
{
    freopen ("New Lottery Game.in","r",stdin);
    freopen ("New Lottery Game.out","w",stdout);
    int t,a,b,k,n;
    scanf ("%d",&t);
    for (int g=1;g<=t;g++)
    {
        n=0;
        scanf ("%d %d %d",&a,&b,&k);
        for (int i=0;i<a;i++)
            for (int j=0;j<b;j++)
                if ((i&j)<k)
                    n++;
        printf ("Case #%d: %d\n",g,n);
    }
    scanf (" ");
    return 0;
}
