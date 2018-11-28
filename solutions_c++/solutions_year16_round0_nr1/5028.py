#include<bits/stdc++.h>

using namespace std;

int main ()
{
    int n,mask,m;
    int T,cs=0;
//    freopen("a.txt","r",stdin);
//    freopen("b.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",++cs);
            continue;
        }
        mask=0;
        int ans=n;
        int i=1;
        while(mask!=((1<<10)-1))
        {
            m=i*n;
            ans=m;
            while(m)
                {
                    int c=m%10;
                    mask|=(1<<c);
                    if(mask==((1<<10)-1))break;
                    m/=10;
                }
                i++;
        }
        printf("Case #%d: %d\n",++cs,ans);

    }
    return 0;
}
