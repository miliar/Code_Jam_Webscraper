#include <bits/stdc++.h>

using namespace std;

int vis[10];

int main()
{
    freopen("A_large.in","r",stdin);
    freopen("A_large.out","w",stdout);
    int t;
    cin >> t;
    int tc;
    int i;
    for(tc=1;tc<=t;tc++)
    {
        long long x,y;
        cin >> x;
        y=x;
        for(i=0;i<=9;i++)
            vis[i]=0;
        long long ans=0;
        if(x==0)
        {
            printf("Case #%d: INSOMNIA\n",tc);
        }
        else
        {
            bool ok=0;
            while(!ok)
            {
                ok=1;
                ans++;
                if(ans>=10000000) {x=-1; break;}
                long long m=x;
                while(m)
                {
                    vis[m%10]=1;
                    m/=10;
                }
                for(i=0;i<10;i++)
                    ok&=vis[i];
                x+=y;
            }
            if(x==-1) printf("Case #%d: INSOMNIA\n",tc);
            else {x-=y; printf("Case #%d: %I64d\n",tc,x);}
        }
    }
}
