#include<iostream>
#include<cstdio>
using namespace std;
int a[10000];
int main()
{
    int t,axe=0;
    scanf("%d",&t);
    while(t--)
    {
        int mx=0,n;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            mx=max(mx,a[i]);
        }
        int ans=mx;
        for(int i=1;i<=mx;i++)
        {
            int cur=0,mxx=0;
            for(int j=1;j<=n;j++)
            {
                if(a[j]>i)
                {
                    cur = cur + (a[j] / i)+((a[j]%i==0)?0:1)-1;
                    mxx=max(mxx,i);
                }
                else mxx=max(mxx,a[j]);
            }
            cur=cur+mxx;
            if(cur<ans)
                ans=cur;
        }
        printf("Case #%d: %d\n",++axe,ans);
    }
    return 0;
}