#include <stdio.h>
#include <string.h>
long long GoNum(long long *num,long long base,long long size)
{
    long long i;
    long long sum;
    sum=0;
    for(i=0;i<size;i++)
    {
        sum*=base;sum+=num[i];
    }
    return sum;
}
void SetNum(long long *num,long long size)
{
    long long i;
    num[size-2]+=1;
    if(num[size-2]>1)
    {
        for(i=size-2;i>0;i--)
        {
            if(num[i]>1)
            {
                num[i]-=2;num[i-1]+=1;
            }
        }
    }


    return;
}
long long IsPrime(long long number)
{   

    long long i;
    for(i=2;i*i<number;i++)
    {
        if(number%i==0) return i;
    }
    return -1;//-1代表质数，i代表一个约数
}
int main()
{
    long long t,i,j,m,n;
    long long k;
    long long num[50];
    long long tmp;
    long long di[20];
    
    scanf("%lld",&t);
    for(m=1;m<=t;m++)
    {   
        printf( "Case #%lld:\n",m);
        scanf("%lld %lld",&n,&j);//N为长度J为个数
        for(i=0;i<n;i++)  num[i]=0;
        num[0]=1;num[n-1]=1;
        while(j)
        {
            for(i=2;i<=10;i++)
            {   
                tmp=GoNum(num,i,n);
                di[i]=IsPrime(tmp);
                if(di[i]==-1)  goto S;
            }
            //for(k=0;k<n;k++)  prlong longf("%lld",num[k] );prlong longf("\n");

            for(i=0;i<n;i++)  printf( "%lld",num[i]);
            for(i=2;i<=10;i++)  printf(" %lld",di[i]);
            printf("\n");
            j--;

            S:SetNum(num,n);
        }
    }


    return 0;
}
