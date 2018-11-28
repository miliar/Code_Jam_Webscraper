#include<cstdio>
#include<cstdlib>
#include<queue>
using namespace std;

#define Maxn 1100

int sa[Maxn];

int main()
{
    int t;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);

    for(int ca=1;ca<=t;ca++)
    {
        int d;
        scanf("%d",&d);
        int maxp=-1;
        for(int i=1;i<=d;i++)
        {
            scanf("%d",&sa[i]);
            if(sa[i]>maxp)
                maxp=sa[i];
        }
        int ans=maxp;
        for(int i=1;i<=maxp;i++)
        {
            int cnt = 0;
            for(int j=1;j<=d;j++)
                cnt += sa[j]/i + (sa[j]%i==0?0:1) -1;
            ans=min(ans,cnt+i);
        }

        printf("Case #%d: %d\n",ca,ans);

    }




    return 0;
}

