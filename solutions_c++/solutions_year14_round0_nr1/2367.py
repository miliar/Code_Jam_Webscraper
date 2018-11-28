#include<cstdio>
#include<cstring>
using namespace std;
int a[6][6];
bool vis1[20],vis2[20];
int main()
{
    freopen("AA.in","r",stdin);
    freopen("A.out","w",stdout);
    int tt;
    scanf("%d",&tt);
    int cot=1;
    while(tt--)
    {
        int x;
        scanf("%d",&x);
        memset(vis1,0,sizeof(vis1));
        memset(vis2,0,sizeof(vis2));
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
        {
            scanf("%d",&a[i][j]);
            if(x==i)
                vis1[a[i][j]]=1;
        }
        scanf("%d",&x);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
        {
            scanf("%d",&a[i][j]);
            if(i==x)
                vis2[a[i][j]]=1;
        }
        int cnt=0,ans=0;
        for(int i=1;i<=16;i++)
        {
            if(vis1[i]&&vis2[i])
            {
                cnt++;
                ans=i;
            }
        }
        if(cnt==0)
            printf("Case #%d: Volunteer cheated!\n",cot++);
        else if(cnt==1)
            printf("Case #%d: %d\n",cot++,ans);
        else
            printf("Case #%d: Bad magician!\n",cot++);
    }
}
