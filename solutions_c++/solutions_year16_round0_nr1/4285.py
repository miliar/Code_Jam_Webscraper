#include <bits/stdc++.h>
using namespace std;
int cnt[15];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas,c=1;
    scanf("%d",&cas);
    while(cas--)
    {
        int n,m;
        scanf("%d",&n);
        if(!n)
        {
            printf("Case #%d: INSOMNIA\n",c++);
            continue;
        }
        memset(cnt,0,sizeof(cnt));
        for(int i=1;;i++)
        {
            m=n*i;
            while(m)
            {
                cnt[m%10]=1;
                m/=10;
            }
            int flag=1;
            for(int j=0;j<10;j++)
                if(!cnt[j])
                {
                    flag=0;
                    break;
                }
            if(flag)
            {
                m=n*i;
                break;
            }
        }
        printf("Case #%d: %d\n",c++,m);
    }
}
