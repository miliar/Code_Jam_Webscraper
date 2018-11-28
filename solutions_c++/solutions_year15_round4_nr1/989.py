#include<cstdio>
#include<cstring>
using namespace std;
const int MAXN=105;
const char dc[]="^>v<";
const int dx[]= {-1,0,1,0},dy[]= {0,1,0,-1};
char mat[MAXN][MAXN];
int ans;
bool check(int x,int y) {
    int k;
    for(int i=0; i<4; ++i)
        if(dc[i]==mat[x][y]) {
            k=i;
            break;
        }
    int tx=x,ty=y;
    do {
        tx+=dx[k];
        ty+=dy[k];
    } while(mat[tx][ty]=='.');
    if(mat[tx][ty]!='\0')
        return true;
    bool flag=false;
    for(int i=0; !flag&&i<4; ++i) {
        if(i==k)
            continue;
        tx=x;
        ty=y;
        do {
            tx+=dx[i];
            ty+=dy[i];
        } while(mat[tx][ty]=='.');
        flag=mat[tx][ty]!='\0';
    }
    if(flag)
        ++ans;
    return flag;
}
int main() {
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t,r,c;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas) {
        scanf("%d%d",&r,&c);
        memset(mat,'\0',sizeof(mat));
        for(int i=1; i<=r; ++i)
            scanf("%s",mat[i]+1);
        bool flag=true;
        ans=0;
        for(int i=1; flag&&i<=r; ++i)
            for(int j=1; flag&&j<=c; ++j)
                flag=mat[i][j]=='.'||check(i,j);
        printf("Case #%d: ",cas);
        if(flag)
            printf("%d\n",ans);
        else
            puts("IMPOSSIBLE");
    }
}
