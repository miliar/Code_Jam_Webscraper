#include <stdio.h>
#include <string.h>
#include<algorithm>
using namespace std;
bool check1[20],check2[20];
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        memset(check1,0,sizeof(check1));
        memset(check2,0,sizeof(check2));
        int chose;
        scanf("%d",&chose);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
        {
            int tt;
            scanf("%d",&tt);
            if(i==chose)check1[tt]=1;
        }
        scanf("%d",&chose);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
        {
            int tt;
            scanf("%d",&tt);
            if(i==chose)check2[tt]=1;
        }
        int ans=0,cnt=0;
        for(int i=1;i<=16;i++)
            if(check1[i]&&check2[i])
            ans=i,cnt++;
        printf("Case #%d: ",cas++);
        if(cnt==1)printf("%d\n",ans);
        else if(cnt==0)puts("Volunteer cheated!");
        else puts("Bad magician!");
    }
}
