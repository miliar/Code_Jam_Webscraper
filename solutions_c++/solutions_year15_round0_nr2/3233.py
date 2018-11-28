#include <bits/stdc++.h>
#define LENGTH 1000005
#define INF 0x3f3f3f
using namespace std;
int a[LENGTH];
int main()
{
    //freopen("C:\\input\\B-large.in","r",stdin);
    //freopen("C:\\input\\output.out","w",stdout);
    int T;
    scanf("%d",&T);
    int Case=1;
    while (T--)
    {
        int n;
        scanf("%d",&n);
        int mx=0;
        for (int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            if (a[i]>mx) mx=a[i];
        }
        int ans=INF;
        for (int i=1;i<=mx;i++)
        {
            int tmp=0;
            for (int j=1;j<=n;j++)
            {
                tmp+=(a[j]-1)/i;
            }
            if (tmp+i<ans) ans=tmp+i;
        }
        cout<<"Case #"<<Case++<<": "<<ans<<endl;
    }
    return 0;
}
