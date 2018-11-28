#include <iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.in","w",stdout);
    int test,n,tt,i,sum,ans;
    string s;
    scanf("%d",&test);
    for(tt=1;tt<=test;tt++)
    {
        scanf("%d",&n);
        cin>>s;
        sum=0;
        ans=0;
        for(i=0;i<=n;i++)
        {
            if(s[i]>'0')
            {
                if(sum>=i)
                {
                    sum=sum+s[i]-'0';
                }
                else if(sum<i)
                {
                    ans=ans+i-sum;
                    sum=i+s[i]-'0';
                }
            }
        }
        printf("Case #%d: ",tt);
        printf("%d\n",ans);
    }
    return 0;
}
