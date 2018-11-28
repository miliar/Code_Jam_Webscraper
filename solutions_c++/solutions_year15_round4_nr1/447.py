#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int T,n,m;
char c[233][233];
bool flag,up[233][233],left[233][233],right[233][233],down[233][233];

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
for(int t=1;t<=T;t++){
        int ans=0;
        flag=false;
    scanf("%d %d",&n,&m);
    for(int i=1;i<=n;i++)scanf("%s",c[i]);
    for(int i=1;i<=n;i++)for(int j=m;j>=1;j--)c[i][j]=c[i][j-1];
    for(int i=0;i<=n+1;i++)c[i][0]=c[i][m+1]='.';
    for(int i=0;i<=m+1;i++)c[0][i]=c[n+1][i]='.';

    memset(up,false,sizeof(up));memset(left,false,sizeof(left));memset(down,false,sizeof(down));memset(right,false,sizeof(right));

    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            up[i][j]=up[i-1][j];left[i][j]=left[i][j-1];
            if(c[i-1][j]!='.')up[i][j]=true;
            if(c[i][j-1]!='.')left[i][j]=true;
        }

    }
    for(int i=n;i>=1;i--){
        for(int j=m;j>=1;j--){
            down[i][j]=down[i+1][j];
            right[i][j]=right[i][j+1];
            if(c[i+1][j]!='.')down[i][j]=true;
            if(c[i][j+1]!='.')right[i][j]=true;

        }
    }

    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            if(!(up[i][j]||down[i][j]||right[i][j]||left[i][j]) &&c[i][j]!='.')flag=true;
            if(flag)break;
            if(c[i][j]=='^' && !(up[i][j]))ans++;
            if(c[i][j]=='v' && !(down[i][j]))ans++;
            if(c[i][j]=='>' && !(right[i][j]))ans++;
            if(c[i][j]=='<' && !(left[i][j]))ans++;
        }
        if(flag)break;
    }
    printf("Case #%d: ",t);
    if(flag)printf("IMPOSSIBLE\n");
    else printf("%d\n",ans);
}

    return 0;
}
