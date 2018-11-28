#include <bits/stdc++.h>
#define LL long long
#define inf 0x3f3f3f3f
using namespace std;
const int maxn=1000+10;
char C[20], J[20];
int a[4]={1,10,100,1000};
int n;

bool ok(int x,int y,int k)
{
    //printf("%d %d",x,y);
    x = (x % a[k+1]) / a[k];
    y = (y % a[k+1]) / a[k];
    //printf(" %d %d %d\n",x,y,k);
    int kk =  n-1-k;
    if (C[kk]=='?' || x ==(int)(C[kk] - '0'))
    {
        if (J[kk]=='?' || y ==(int)(J[kk] - '0'))
        {
            return 1;
        }
    }
    return 0;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T,cas = 0;
    scanf("%d",&T);
    while(T--)
    {
        int ans=10000 , ansx ,ansy;
        scanf("%s%s",C,J);
        n=strlen(C);
        for (int i=0;i<=a[n]-1;i++)
        {
            for (int j=0;j<=a[n]-1;j++)
            {
                bool flag=1;
                for (int k=0;k<n;k++)
                {
                    if (!ok(i,j,k)) flag=0;
                }
                if (flag)
                {
                    if (ans>abs(i-j))
                    {
                        ans=abs(i-j);
                        ansx=i;ansy=j;
                    }
                }
            }
        }
        //printf("%d %d\n",ansx,ansy);
        printf("Case #%d: ",++cas);
        for (int i=1;i<=n;i++)
        {
            if (ansx/a[i] == 0)
            {
                for (int j=1;j<=n-i;j++) printf("0");
                printf("%d ",ansx);
                break;
            }
        }
        for (int i=1;i<=n;i++)
        {
            if (ansy/a[i] == 0)
            {
                for (int j=1;j<=n-i;j++) printf("0");
                printf("%d\n",ansy);
                break;
            }
        }
    }

    return 0;
}
