#include<stdio.h>
#include<math.h>
#define MAX 10000002
int a[MAX],b[MAX];
int pal(long long i)
{
    long long j=0,k=i;
    while(k)
    {
        j*=10;
        j+=k%10;
        k=k/10;
    }
    if(j==i)
        return 1;
    else
        return 0;
}
int main()
{
    int t,j,k;
    long long i,x,y,temp;
    scanf("%d",&t);
    for(i=0;i<MAX;i++)
        a[i]=0;
    for(i=1;i<MAX;i++)
    {
        if(pal(i)&&pal(i*i))
        {
            a[i]=1;
        }
    }
    for(i=1,b[0]=0;i<MAX;i++)
    {
        b[i]=b[i-1]+a[i];
    }
    for(k=1;k<=t;k++)
    {
        scanf("%lld%lld",&x,&y);
        /*if(x>y)
        {
               temp=x;
               x=y;
               y=temp;
        }*/
        y=(int)sqrt(y);
        x=(int)sqrt(x-1);
        printf("Case #%d: %d\n",k,b[y]-b[x]);
    }
    return 0;
}
