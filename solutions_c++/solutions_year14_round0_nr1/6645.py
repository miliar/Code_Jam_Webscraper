#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int x,y,u[17],a[5][5],b[5][5];
int main(){
   // freopen("test.in","r",stdin);
   // freopen("test.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int it=1;it<=t;it++){
        printf("Case #%d: ",it);
        memset(u,0,sizeof(u));
        scanf("%d",&x);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++) scanf("%d",&a[i][j]);
        scanf("%d",&y);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++) scanf("%d",&b[i][j]);
        for (int i=1;i<=4;i++) u[a[x][i]]++;
        for (int i=1;i<=4;i++) u[b[y][i]]++;
        int res = 0, cnt = 0;
        for (int i=1;i<17;i++) if (u[i] > 1){
            cnt++; res = i;
        }
        if (cnt == 0) puts("Volunteer cheated!");
        else if (cnt > 1) puts("Bad magician!");
        else printf("%d\n",res);
    }
    return 0;
}
