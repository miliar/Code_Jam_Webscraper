#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int len,wid;
int s[105][105];
int num[105],big;
int ux[105],uy[105];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int amm,count=1;
    scanf("%d",&amm);
    while (amm--)
    {
        scanf("%d%d",&len,&wid);
        memset(num,0,sizeof num);
        big=0;
        for (int i=0;i<len;i++)
        {
            for (int j=0;j<wid;j++)
            {
                scanf("%d",&s[i][j]);
                num[s[i][j]]++;
                big=max(big,s[i][j]);
            }
        }
        bool flag=1;
        memset(ux,0,sizeof ux);
        memset(uy,0,sizeof uy);
        for (int k=1;k<=big;k++)
        {
            if (num[k]==0)continue;

            for (int i=0;i<len;i++)if (!ux[i])
            {
                bool yes=1;int co=0;
                for (int j=0;j<wid;j++)if (!uy[j])
                {
                    if (s[i][j]!=k){yes=0;break;}
                    co++;
                }
                if (yes)
                {
                    num[k]-=co;
                    ux[i]=1;
                }
            }
            for (int j=0;j<wid;j++)if (!uy[j])
            {
                bool yes=1;int co=0;
                for (int i=0;i<len;i++)if (!ux[i])
                {
                    if (s[i][j]!=k){yes=0;break;}
                    co++;
                }
                if (yes)
                {
                    num[k]-=co;
                    uy[j]=1;
                }
            }
            if (num[k]!=0)flag=0;
        }
        if (flag)printf("Case #%d: YES\n",count++);
        else printf("Case #%d: NO\n",count++);
    }
    return 0;
}
