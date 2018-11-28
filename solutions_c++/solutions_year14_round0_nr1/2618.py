#include <iostream>
#include <cstdio>
using namespace std;

int a[11][11],b[11][11],c[111];

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int cas,x,y;
    scanf("%d",&cas);
    int tt=0;
    while(cas--){
        tt++;
        scanf("%d",&x);
        for(int i=1;i<=16;i++)
            c[i]=0;
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
            scanf("%d",&a[i][j]);
        scanf("%d",&y);
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
            scanf("%d",&b[i][j]);
        for(int i=1;i<=4;i++)
            c[a[x][i]]++;
        for(int i=1;i<=4;i++)
            c[b[y][i]]++;
        int cnt=0,ans=0;
        for(int i=1;i<=16;i++)
        {
            if(c[i]>=2)
                cnt++,ans=i;
        }
        printf("Case #%d: ",tt);
        if(cnt>=2)
            puts("Bad magician!");
        else if(cnt==1)
            printf("%d\n",ans);
        else
            puts("Volunteer cheated!");


    }
    return 0;
}
