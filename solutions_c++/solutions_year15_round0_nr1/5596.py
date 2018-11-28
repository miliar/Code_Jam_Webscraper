#include<bits/stdc++.h>
#define mx 100005
using namespace std;
char a[mx];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        int l;
        scanf("%d",&l);
        scanf("%s",a);

        int now=0,ans=0;
        for(int i=0;i<=l;i++)
        {
            int x=a[i]-'0';
            if(now<i)
            {
                ans+=(i-now);
                now+=(i-now);

            }
            now+=x;

        }
        printf("Case #%d: %d\n",cas,ans);
    }

}
