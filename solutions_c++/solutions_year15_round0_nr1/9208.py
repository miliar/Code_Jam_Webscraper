#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
    int t,j;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        int n,i;
        long long int total=0,need=0;
        scanf("%d",&n);
        char a[n+5];
        scanf("%s",a);
        total=a[0]-'0';
        for(i=1;i<=n;i++)
        {
            if((a[i]-'0')>0)
            {


            if(total < i)
            {
                need+=(i-total);
                total=i;
            }
                total+=(a[i]-'0');
             }
        }
        printf("Case #%d: %lld\n",j,need);
    }
return 0;
}
