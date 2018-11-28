#include<stdio.h>
#include<math.h>
char str[20];
long long arr[11];
void convert_to_bi(long long n)
{
    long long i=0,j;
    while(n>0)
    {
        j=n%2;
        if(j==1)
        str[i++]='1';
        else
           str[i++]='0';
        n/=2;
    }
    for(;i<17;i++)
        str[i]='0';
}
long long inbase(long long k)
{long long i=0,j=1,a=0;
    for(i=0;i<17;i++)
    {
        if(str[i]=='1')
            a+=j;
        j*=k;
    }
    return a;
}
long long primecheck(long long a,long long k)
{
    long long s=sqrt(a);

    long long i;
    for(i=s;i>1;i--)
        if(a%i==0)
    {arr[k]=i;
    return 1;
    }
    return 0;
}
int main()
{
long long t,n,i,j,l,k,a,coun=0,p;
int occur[10],ndig[20];
FILE *fptr,*op;
fptr=fopen("F:/a.txt","r");
op=fopen("F:\co.txt","w");
op=fopen("F:\co.txt","a");
fscanf(fptr,"%lld",&t);
//n=16;j=50;
fscanf(fptr,"%lld %lld",&n,&j);
l=1<<16;
fprintf(op,"Case #1:\n");
for(i=(1<<15)+1 ;i < l && coun<j; i+=2)
{
    convert_to_bi(i);
    /*for(k=0;k<17;k++)
        printf("%c",str[k]);
    printf("\n");*/
    for(k=2;k<11;k++)
    {
        a=inbase(k);
        //printf("%lld %lld %lld\n",i,a,k);
        p=primecheck(a,k);
        if(p!=1)
            break;
    }

    if(p==1)
    {
        ++coun;
        fprintf(op,"%lld ",a);
        for(k=2;k<11;k++)
         fprintf(op,"%lld ",arr[k]);
        fprintf(op,"\n");
    }
}


return 0;
}

