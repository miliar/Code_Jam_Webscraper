#include<bits/stdc++.h>
using namespace std;

long long arr[1100];

int main()
{
    long long test,i,j,k;
    long long n;
    long long sum=0,count1;

    scanf("%lld",&test);

    for(i=0;i<test;i++)
    {
        sum=0;
        count1=0;

        scanf("%lld",&n);

        for(j=0;j<=n;j++)
        {
            scanf("%1lld",&arr[j]);
        }

        sum=arr[0];

        for(j=1;j<=n;j++)
        {
            if(j>sum)
            {
                count1=count1+(j-sum);
                sum=j;
            }

            sum=sum+arr[j];
        }

        printf("Case #%lld: %lld\n",i+1,count1);
    }
}














