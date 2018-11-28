#include<iostream>
#include<cstdio>
#include<cstring>
#include<set>
using namespace std;
int a[10][10];
int b[10][10];
bool vis[200];
int main(){
    int T,cas = 1;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>T;
    while(T--){
        int n,m,ans;
        cin>>n;
        memset(vis,0,sizeof(vis));
        for(int i = 1; i <= 4; i++ )
            for(int j = 1; j <= 4; j++){
                scanf("%d",&a[i][j]);
                if(i == n) vis[a[i][j]] = 1;
            }
        cin>>m;
        int cn = 0;
        for(int i = 1; i <= 4; i++ )
            for(int j = 1; j <= 4; j++){
                scanf("%d",&a[i][j]);
                if(i == m){
                    if(vis[a[i][j]]) {
                        cn++;
                        ans = a[i][j];
                    }
                }
            }
        printf("Case #%d: ",cas++);
        if(cn == 0) printf("Volunteer cheated!\n");
        else if(cn == 1) printf("%d\n",ans);
        else printf("Bad magician!\n");
    }
    return 0;
}
