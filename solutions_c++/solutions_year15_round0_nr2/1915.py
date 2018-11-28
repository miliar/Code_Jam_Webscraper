#include<iostream>
#include<stdio.h>
#include<cstring>
#include<algorithm>
using namespace std;
const int maxn=10005;
int a[maxn];
int n;
void work()
{
    int maxa=0;
    scanf("%d",&n);
    for (int i=1;i<=n;i++)
        scanf("%d",&a[i]),maxa=max(maxa,a[i]);


    int ans=100000;
    for (int low=1;low<=maxa;low++)
    {
        int tmpans=low;
        for (int j=1;j<=n;j++)
            if (a[j]>low)
            {
                if (a[j]%low==0) tmpans+=a[j]/low-1; else
                    tmpans+=a[j]/low;
            }
        ans=min(ans,tmpans);
    }
    printf("%d\n",ans);
}
int main()
{
    //freopen("large.in","r",stdin);
    //freopen("large.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while (T--)
    {
        cas++;
        printf("Case #%d: ",cas);
        work();
    }
}
