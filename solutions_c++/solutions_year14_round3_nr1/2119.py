#include <cstdio>
#include <math.h>

using namespace std;

long long i,p,q,c,cc,t,ket,k;
FILE *fp(fopen("input.txt","r"));
FILE *fp2(fopen("output.txt","w"));

void egyszerus(long long &x, long long &y)
{
    long long s(y);
    for(long long j=s;j>2;j--)
    {
        if(y%j==0){
            if(x%j==0){
                x=x/j;
                y=y/j;
            }
        }
    }
}

int kettoh(long long x)
{
    long long s(x);
    int c(0);
    while(s%2==0)
    {
        s=s/2;
        c++;
    }
    if(s>1){
        return(0);
    }
    return(c);
}

int main()
{
    fscanf(fp,"%d",&t);
    for(k=0;k<t;k++)
    {
        fscanf(fp,"%lld/%lld",&p,&q);
        egyszerus(p,q);
        ket=kettoh(q);
        fprintf(fp2,"Case #%d: ",k+1);
        if(ket==0){
            fprintf(fp2,"impossible\n");
        } else {
            for(i=ket;i<40;i++)
            {
                p=p*2;
            }
            c=1;
            for(i=0;i<40;i++)
            {
                c=c*2;
            }
            cc=0;
            while(c>p)
            {
                c=c/2;
                cc++;
            }
            fprintf(fp2,"%lld\n",cc);
        }
    }
    return 0;
}
