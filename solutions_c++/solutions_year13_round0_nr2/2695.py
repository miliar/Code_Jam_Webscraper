#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int N=100+10;
int a[N][N],n,m;
bool check(int x,int y){
    int i;
    for(i=0;i<m;i++) if(a[x][i]==2) break;
    if(i>=m) return true;
    for(i=0;i<n;i++) if(a[i][y]==2) break;
    if(i>=n) return true;
    return false;
}
bool check(){
    for(int i=0;i<n;i++)
    for(int j=0;j<m;j++)
    if(a[i][j]==1&&!check(i,j)) return false;
    return true;
}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.cpp","w",stdout);
    int T,i,j,k,cas=1;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",cas++);
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        for(j=0;j<m;j++)
        scanf("%d",&a[i][j]);
        if(check()) puts("YES");
        else puts("NO");
    }
    return 0;
}
