#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#define INF (1<<30)
#define N 5
using namespace std;
int x[N][N],y[N][N];
void solve(){
    int k,sec;
    scanf("%d",&k);
    k--;
    for(int i=0;i<4;i++)for(int j=0;j<4;j++)
        scanf("%d",&x[i][j]);
    scanf("%d",&sec);
    sec--;
    for(int i=0;i<4;i++)for(int j=0;j<4;j++)
        scanf("%d",&y[i][j]);
    int ans=0,cnt=0;
    for(int i=0;i<4;i++){
        int cur=y[sec][i];
        for(int j=0;j<4;j++){
            if(cur==x[k][j]){
                ans=cur;
                cnt++;
            }
        }
    }
    if(cnt==1)printf("%d\n",ans);
    else if(cnt==0)printf("Volunteer cheated!\n");
    else printf("Bad magician!\n");
}
int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
