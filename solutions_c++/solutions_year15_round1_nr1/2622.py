#include<stdio.h>
#include<iostream>
int main()
{
    int t,n,i,m[10000],x,d,sum,sum1,j,k,r;
    int max1;
   FILE *out;
    FILE *in;
    in=freopen("A.in","r",stdin);
    out=freopen("A1.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
        for(j=0;j<n;j++)
            scanf("%d",&m[j]);
        sum=0;sum1=0;
        for(k=0;k<n-1;k++)
        {
            x=m[k]-m[k+1];
            if(x<0)
                x= 0;
            sum+=x;
        }
        max1=0;
        for(k=0;k<n-1;k++)
        {
            r=m[k]-m[k+1];
            if(r<0)
                r= 0;
            if(r>max1)
                max1=r;
        }
        for(k=0;k<n-1;k++)
        {
            if(max1!=0)
            {
                if(m[k]>max1)
                sum1+=max1;
                else
                sum1+=m[k];
            }
            else
                sum1=0;
        }
        printf("Case #%d: %d %d\n",i,sum,sum1);
    }
    return 0;
}
