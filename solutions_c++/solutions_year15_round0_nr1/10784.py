#include<iostream>
#include<cstdio>
using namespace std;
#define max 1002
int main()
{
    int t,smax,i,k,ans,sum,a[max];
    char s[max];
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d %s",&smax,&s);
        ans=0;
        sum=0;
        for(i=0;i<=smax;i++)
        {
            if(sum>=i)
                sum+=(s[i]-'0');
            else
            {
                ans+=(i-sum);
                sum+=(s[i]-'0')+(i-sum);
            }
        }
        a[k]=ans;
        //printf("Case #%d: %d\n",k,ans);
    }
    for(k=1;k<=t;k++)
    {
        printf("Case #%d: %d\n",k,a[k]);
    }
    return 0;
}
