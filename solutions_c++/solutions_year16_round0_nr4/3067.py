#include<stdio.h>
long long pow(long long a,long long z)// z is base
{
    long long p,m;
    m=a;p=1;
    while(m)
    {
        while((m%2)==0)
            {
                m=m/2;
                z=(z*z);
            }
        m=m-1;
        p=(p*z);
    }
    return p;
}

int main()
{
long long n,t,i,j,k,c,s,diff,agp,a,r,d,diff2,p;
FILE *fptr,*op;
fptr=fopen("F:/a.txt","r");
op=fopen("F:\co.txt","w");
op=fopen("F:\co.txt","a");
fscanf(fptr,"%lld",&t);
    for(j=1;j<=t;j++)
    {
        fscanf(fptr,"%lld %lld %lld",&k,&c,&s);
        fprintf(op,"Case #%lld: ",j);
        diff=k-(c-1);
        r=k;d=-1;
        if(s>=k)
        {
            for(i=1;i<=k;i++)
            fprintf(op,"%lld ",i);
        }
        else if (c>=k)
        {
            n=k-1;a=k-1;
            agp=((a+(n-1)*d)*pow(n,r)-a)/(r-1) + (d*r*(pow(n-1,r)-1))/pow(2,r-1);
            diff2=c-k;
            p=pow(diff2,k);
            fprintf(op,"%lld",agp*p+1);
        }
        else if(s>=diff)
        {
            n=c-1;a=n;
            agp=((a+(n-1)*d)*pow(n,r)-a)/(r-1) + (d*r*(pow(n-1,r)-1))/pow(2,r-1);
            for(i=0;i<diff;i++)
                fprintf(op,"%lld ",++agp);
        }
        else
            fprintf(op,"IMPOSSIBLE");
        fprintf(op,"\n");
    }
return 0;
}

