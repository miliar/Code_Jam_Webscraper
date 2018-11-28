#include<bits/stdc++.h>
#define INT long long int
using namespace std;

bool num[10];

void set_value(INT n)
{
    INT rem;
    while(n)
    {
        rem=n%10;
        num[rem]=1;
        n/=10;
    }
}

int main()
{
    INT t,caseno=0,n,i,j,a,b,c,m,flag;
    FILE *fp,*fq;
    fp=fopen("A-large.in","r");
    fq=fopen("Output.txt","w");
    fscanf(fp,"%lld",&t);
    while(t--)
    {
        for(i=0;i<10;i++)
            num[i]=0;
        fscanf(fp,"%lld",&n);
        a=n;
        fprintf(fq,"Case #%lld: ",++caseno);
        if(n==0)
        {
            fprintf(fq,"INSOMNIA\n");
            continue;
        }
        for(i=1;true;i++)
        {
            n=a*i;
            set_value(n);
            flag=0;
            for(j=0;j<10;j++)
            {
                if(num[j]==0)
                    flag=1;
            }
            if(flag==0)
                break;
        }
        fprintf(fq,"%lld\n",n);
    }
    return 0;
}
