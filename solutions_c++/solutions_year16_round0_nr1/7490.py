#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("1-large.out","wt",stdout);
    long long int t,n,i,x;
    scanf("%lld",&t);
    x=t;
    while(t--)
    {
        scanf("%lld",&n);
        int arr[10]={0,0,0,0,0,0,0,0,0,0};
        if(n==0)
            printf("Case #%lld: INSOMNIA\n",x-t);
        else
        {
            long long int k,a=n,sum;
            long long int times=1;
            start:
            while(a)
            {
                k=a%10;
                arr[k]=1;
                a=a/10;
            }
            sum=0;
            for(i=0;i<10;i++)
            {
                sum=sum+arr[i];
            }
            if(sum!=10)
            {
                times++;
                a=n*times;
                goto start;
            }
            else
                printf("Case #%lld: %lld\n",x-t,times*n);
        }

    }
}
