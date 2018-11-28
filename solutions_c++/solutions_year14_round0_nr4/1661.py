#include <iostream>
#include <stdlib.h>
#include <cstdio>
#include <fstream>
#include <algorithm>
using namespace std;
int main()
{
    int i,j,k,l,n;
    int t;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&n);
        double a[n],b[n];double ct,bt;
        for(i=0;i<n;i++)
            scanf("%lf",&a[i]);

        for(i=0;i<n;i++)
            scanf("%lf",&b[i]);
            for(i=0;i<n-1;i++)
            {
                for(j=i+1;j<n;j++)
                {
                    if(a[i]>a[j])
                    {
                        ct=a[i];
                        a[i]=a[j];
                        a[j]=ct;
                    }
                    if(b[i]>b[j])
                    {
                        bt=b[i];
                        b[i]=b[j];
                        b[j]=bt;
                    }
                }
            }
            double xa[n],xb[n];
            for(i=0;i<n;i++)
            {
                xa[i]=a[i];
                xb[i]=b[i];
            }
            int di=0,vi=0,g=0,h=0;
            if(a[n-1]<b[0])
                vi=0;
            else
            {
                for(i=0;i<n;i++)
                {
                    h=0;
                    for(j=0;j<n;j++)
                    {
                        if(b[j]>a[i])
                        {
                            h=1;
                            b[j]=0;
                            a[i]=0;
                            break;
                        }
                    }
                    if(h==0)
                    {
                        vi=n-(i);
                        break;
                    }

                }

            }int xm=0;
            h=0;
            for(i=n-1;i>=0;i--)
                {
                    h=0;
                    for(j=0;j<n;j++)
                    {
                        if(xa[j]>xb[i]&&(xa[j]!=0)&&(xb[i]!=0))
                        {
                            xa[j]=0;
                            xb[i]=0;
                            h=1;
                            break;
                        }
                    }
                    if(h==1)
                    {
                        xm++;
                    }
                }
                printf("Case #");printf("%d",k);printf(": ");printf("%d",xm);printf(" ");printf("%d\n",vi);


    }
}


