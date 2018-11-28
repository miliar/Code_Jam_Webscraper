#include <stdio.h>

FILE *f,*g;

double a[1002],b[1002],min,min1,min2,max,aux1[1002],aux2[1002];
int i,j,n,t,necinstit,cinstit,p,q,poz,poz1,poz2,pozmax,ver[1002];

int main()
{
    f=fopen("prob4.in","r");
    g=fopen("prob4.out","w");

    fscanf(f,"%d",&t);
    for(i=1;i<=t;i++)
    {
        fscanf(f,"%d",&n);

        necinstit=0;
        cinstit=0;

        for(j=1;j<=n;j++)
            fscanf(f,"%lf",&a[j]);

        for(j=1;j<=n;j++)
            fscanf(f,"%lf",&b[j]);

        for(j=1;j<=n;j++)
            aux1[j]=a[j];

        for(j=1;j<=n;j++)
            aux2[j]=b[j];

        for(p=1;p<=n;p++)
        {
            min1=2;
            min2=2;

            for(q=1;q<=n;q++)
                if (a[q]<min1 && a[q]!=0)
                {
                    min1=a[q];
                    poz1=q;
                }

            for(q=1;q<=n;q++)
                if (b[q]<min2 && b[q]!=0)
                {
                    min2=b[q];
                    poz2=q;
                }

            max=0;
            for(q=1;q<=n;q++)
                if (b[q]>max)
                {
                    max=b[q];
                    pozmax=q;
                }

            if (min1>min2)
            {
                necinstit++;
                a[poz1]=0;
                b[poz2]=0;
            }
            else
            {
                a[poz1]=0;
                b[pozmax]=0;
            }

        }




        for(j=1;j<=n;j++)
            a[j]=aux1[j];
        for(j=1;j<=n;j++)
            b[j]=aux2[j];

        for(p=1;p<=n;p++)
        {
            min=2;
            poz=0;
            for(q=1;q<=n;q++)
                if (b[q]>a[p] && b[q]<min)
                {
                    min=b[q];
                    poz=q;
                }
            b[poz]=0;
        }

        for(j=1;j<=n;j++)
            if (b[j]!=0) cinstit++;

        fprintf(g,"Case #%d: %d %d\n",i,necinstit,cinstit);
    }

    return 0;
}
