#include <stdio.h>



int main (void)
{
    int t;
    scanf ("%d",&t);
    int i;

    for (i=0;i<t;++i)
    {
        int a[10]={0};

        long long int n,p,z;
        int m;
        scanf ("%lld",&n);
        if (n==0)
            printf ("Case #%d: INSOMNIA\n",i+1);
            else
            {
                for (p=1;;++p)
                {z=p*n;
                while (z>0)
                {a[z%10]++;
                z=z/10;}

                int x;

                for (m=0;m<10;++m)
                {
                    x=1;
                    if (a[m]==0)
                    {
                        x=0;
                        break;
                    }
                }

                if (x==1)
                {
                    printf ("Case #%d: %lld\n",i+1,p*n);
                    break;
                }


              }
            }


    }
    return 0;
}
