#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++)
    {
        char s[1010];
        int maxv;
        scanf("%d%s",&maxv,s);
        int ans=0;
        int tot=0;
        for(int i=0;i<=maxv;i++)
        {
            int x=s[i]-'0';
            if(i==0)
                tot+=x;
            else
            {
                if(tot<i)
                {
                    ans += i-tot;
                    tot = i;
                }
                tot+=x;
            }
        }
        printf("Case #%d: %d\n",cs,ans);
    }
    return 0;
}
