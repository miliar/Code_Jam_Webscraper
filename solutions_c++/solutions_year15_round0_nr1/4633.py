#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t,m;
    char str[1010];
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        scanf("%d",&m);
        scanf("%s",str);
        int sum=0;
        int ans=0;
        sum+=str[0]-'0';
        for(int i=1;i<=m;i++)
        {
            if(sum<i&&(str[i]!='0'))
            {
                ans+=i-sum;
                sum+=i-sum;
            }
            sum+=str[i]-'0';
        }
        printf("Case #%d: %d\n",c,ans);
    }
}
