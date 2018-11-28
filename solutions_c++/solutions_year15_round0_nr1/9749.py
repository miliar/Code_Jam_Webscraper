#include<stdio.h>

int main()
{
    int tc,t,i,smax,s[1001];
    long int ans,sum;
    char str[1001];

    scanf("%d\n",&tc);
    for(t=0;t<tc;t++)
    {
        ans=0;
        sum=0;
        scanf("%d\n",&smax);
        gets(str);
        printf("Case #%d: ",t+1);
        for(i=0;i<=smax;i++)
            s[i]=str[i]-48;
        for(i=0;i<=smax;i++)
        {
            if(sum<i)
            {
                ans+=i-sum;
                sum=i;
            }
            sum+=s[i];
        }
        printf("%ld\n",ans);
    }
    return 0;
}
