#include<iostream>
#include<cstdio>
using namespace std;

int x,y;
int a[4][4],b[4][4];

int main()
{
    freopen("A-small-attempt0.in","rb",stdin);
    freopen("test.out","wb",stdout);
    int T,cas=1;scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",cas++);
        scanf("%d",&x);
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                scanf("%d",&a[i][j]);
        scanf("%d",&y);
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                scanf("%d",&b[i][j]);
        int ans=0,xx,yy;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                if(a[x-1][i]==b[y-1][j]) ++ans,xx=i,yy=j;
        if(ans==0) printf("Volunteer cheated!\n");
        else if(ans==1) printf("%d\n",a[x-1][xx]);
        else printf("Bad magician!\n");
    }
    return 0;
}
