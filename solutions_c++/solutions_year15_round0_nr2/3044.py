#include<cstdio>
#include<algorithm>
using namespace std;
#define inf 0x3f3f3f3f
int T,n,p[1010],maxp,cnt,ans;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int parts,i,j,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        maxp=0,ans=inf;
        for(i=0;i<n;i++) scanf("%d",&p[i]),maxp=max(maxp,p[i]);
        for(i=1;i<=maxp;i++)
        {
            cnt=0;
            for(j=0;j<n;j++)
            {
                parts=p[j]/i+(p[j]%i==0?0:1)-1;
                cnt+=parts;
            }
            ans=min(ans,cnt+i);
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
