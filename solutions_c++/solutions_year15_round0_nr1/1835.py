#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

char s[1010];

int main()
{
    int T,n,Case=0;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        scanf("%s",s);
        int sum=0,ans=0;
        for (int i=0;i<=n;i++)
            if (s[i]!='0')
            {
                if (i<=sum)
                {
                    sum=sum+s[i]-'0';
                }
                else
                {
                    ans=ans+i-sum;
                    sum=i+s[i]-'0';
                }
            }
        printf("Case #%d: %d\n",++Case,ans);
    }
    return 0;
}
