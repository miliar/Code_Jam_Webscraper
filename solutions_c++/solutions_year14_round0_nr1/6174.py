#include <iostream>
#include <cstdio>

using namespace std;

int a[5][5],b[5][5],n,x,y,c,m;

int main()
{
//    freopen("A-small-attempt3.in","r",stdin);
//    freopen("out.out","w",stdout);
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d",&x);
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                scanf("%d",&a[j][k]);

        scanf("%d",&y);
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                scanf("%d",&b[j][k]);

        c=0;x--;y--;
        for(int j=0;j<4;j++) for(int k=0;k<4;k++)
            if(a[x][j]==b[y][k]){c++;m=a[x][j];}

        if(c==1) printf("Case #%d: %d\n",i,m);
        if(c==0) printf("Case #%d: Volunteer cheated!\n",i);
        if(c>1) printf("Case #%d: Bad magician!\n",i);
    }
    return 0;
}
