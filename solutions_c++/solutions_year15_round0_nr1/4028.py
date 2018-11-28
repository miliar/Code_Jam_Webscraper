#include<stdio.h>
#include<iostream>
#include<string.h>


using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out4.txt","w", stdout);
    long long t;
    scanf("%lld",&t);

    long long a=1;
    while(t--)
    {
        long long i, len;
        char A[10003];
        scanf("%lld %s",&len,A);
         //printf("%c",A[]);
         long long sum=(long long)(A[0]-'0');
         long long count=0;
         //cout<<sum;

         for(i=1;i<=len;i++)
         {
             if(sum<i)
             {
                 count+=(i-sum);
                 sum+=i-sum;
             }
              sum=sum+(long long)(A[i]-'0');
         }
         printf("Case #%lld: %lld",a,count);
         printf("\n");
         a++;
    }

    return 0;
}
