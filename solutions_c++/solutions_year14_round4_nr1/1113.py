#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

int a[1000];

int main()
{
    int t,n,m,x,ys=0;

    freopen("A-large.in","r",stdin);
    freopen("testA.out","w",stdout);
    scanf("%d",&t);
    while (t--)
    {
        memset(a,0,sizeof(a));
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;i++)
        {
            scanf("%d",&x);
            a[x]++;
        }

        int ans=0;
        for (int i=0;i<=m;i++)
        {
            while (a[i]>0)
            {
                a[i]--;
                //printf("i %d\n",i);
                ans++;
                for (int j=m-i;j>0;j--)
                    if (a[j]>0)
                    {
                        a[j]--;
                        //printf("j %d\n",j);
                        break;
                    }
            }
        }


        printf("Case #%d: %d\n",++ys,ans);
    }

    return 0;
}

