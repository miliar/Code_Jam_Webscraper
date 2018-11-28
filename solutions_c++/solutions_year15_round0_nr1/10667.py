#include<stdio.h>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    int j;
    for(j=1;j<=t;j++)
    {
        int m;
        long long int cnt=0;
        scanf("%d ",&m);
        char arr[m+3];
        scanf("%s",arr);
        int i;
        long long sum=0;
        for(i=0;arr[i]!='\0';i++)
        {
             //printf("%lld %d ",sum,i);
            if(sum<i)
               {cnt=cnt+i-sum; sum=i;}
            sum=sum+arr[i]-'0';

        }
        printf("Case #%d: %lld\n",j,cnt);
    }
}
