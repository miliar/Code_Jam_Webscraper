#include<stdio.h>
int main()
{
    int t,k=1;
    scanf("%d",&t);
    while(t--)
    {
        long long r,t;
        scanf("%lld%lld",&r,&t);
        long long sum=0,i=r;
        long long real,arr[2]={0};
        for(;sum<=t;i+=2)
        {
            sum+=(2*i+1);
            arr[1]=arr[0];
            arr[0]=sum;
        }
        i-=2;
        if(sum>t)
            real=(i-r)/2;
        else
            real=(i-r)/2+1;
        printf("Case #%d: %lld\n",k++,real);
    }
    return 0;
}
