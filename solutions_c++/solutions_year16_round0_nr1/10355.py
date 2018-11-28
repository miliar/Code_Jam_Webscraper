#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

char s[10005];
int main()
{
    freopen("in2.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    LL T,cas=0;
    scanf("%lld",&T);
    while (T--)
    {
        LL n;
        scanf("%lld",&n);
        LL cur=0;
        bool flag=0;
        LL ans=0;

        printf("Case #%lld: ",++cas);

        if (n==0) 
        {
            printf("INSOMNIA\n");
            continue;
        }

        //for (LL i=1;i<=100000;i++)
        while (1)
        {
            cur+=n;
            sprintf(s,"%lld",cur);
            //printf("%s\n",s);
            LL len=strlen(s);
            for (LL j=0;j<len;j++)
            {
                ans|=1LL<<(s[j]-'0');
            }
            // printf("%lld\n",ans);
            if (ans==((1LL<<10)-1)) 
            {
                printf("%lld\n",cur);
                flag=1;
                break;
            }
        }
    }
}