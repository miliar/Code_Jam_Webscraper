#include<cstdio>
#include<string.h>
int main()
{
    int t,smax,sum,count,count1;
    scanf("%d",&t);
    char shy[2001];
    for(int j=1;j<=t;j++)
    {
        sum=0;
        count=0;
        scanf("%d",&smax);
        scanf("%s",shy);
        for(int i=1;i<=smax;i++)
        {
            sum=sum+(shy[i-1]-'0');
            if(i>sum){
            count1=i-sum;
            sum=sum+count1;
            count=count+count1;
            }
        }
        printf("Case #%d: %d\n",j,count);

    }
    return 0;
}
