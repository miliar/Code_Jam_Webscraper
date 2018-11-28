#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int T,cas=1;
int vis[17];
int a[5][5];
int nu,n,cur,ans;

int main() {

    freopen("MagicTrick.in","r",stdin);
    cin >> T;
    //freopen("MagicTrick.out","w",stdout);
    while(T--) {
        for(int i=1;i<17;i++) vis[i]=0;
        scanf("%d",&ans);ans--;
        for(int i=0;i<4;i++) for(int j=0;j<4;j++) scanf("%d",&a[i][j]);
        for(int j=0;j<4;j++) vis[a[ans][j]]=1;
        scanf("%d",&ans);ans--;
        for(int i=0;i<4;i++) for(int j=0;j<4;j++) scanf("%d",&a[i][j]);
        nu = 0;
        for(int j=0;j<4;j++) if(vis[a[ans][j]]==1) {nu++;cur=a[ans][j];}
        printf("Case #%d: ",cas++);
        if(nu==0) printf("Volunteer cheated!\n");
        else if(nu==1) printf("%d\n",cur);
        else printf("Bad magician!\n");
    }
    return 0;
}
