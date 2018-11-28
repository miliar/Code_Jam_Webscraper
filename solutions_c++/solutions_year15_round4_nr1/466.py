#include <bits/stdc++.h>
using namespace std;

const int mr[]={0,1,0,-1,0};
const int mc[]={-1,0,1,0,0};
const int INF = 1000000007;

char a[105][105];
bool v[105][105];
int ans;

void dfs(int r, int c, int step){
    v[r][c]=true;
    int o;
    if(a[r][c]=='<') o=0;
    if(a[r][c]=='v') o=1;
    if(a[r][c]=='>') o=2;
    if(a[r][c]=='^') o=3;
    int dr=r,dc=c;
    do{
        dr+=mr[o];
        dc+=mc[o];
    }while(a[dr][dc]=='.');
    if(!a[dr][dc]){
        bool ok=false;
        for(o=0;o<4;o++){
            dr=r,dc=c;
            do{
                dr+=mr[o];
                dc+=mc[o];
            }while(a[dr][dc]=='.');
            if(a[dr][dc]){
                ok=true;
                break;
            }
        }
        if(!ok) ans=INF; else ans++;
    }
}

int main(){
    int cs;
    scanf("%d",&cs);
    for(int no=1;no<=cs;no++){
        ans=0;
        int n,m;
        scanf("%d%d",&n,&m);
        memset(a,0,sizeof(a));
        memset(v,0,sizeof(v));
        for(int i=1;i<=n;i++) scanf("%s",a[i]+1);
        for(int i=1;i<=n;i++) for(int j=1;j<=m;j++){
            if(a[i][j]!='.' && !v[i][j]) dfs(i,j,0);
        }
        printf("Case #%d: ",no);
        if(ans>=INF) puts("IMPOSSIBLE");
                else printf("%d\n",ans);
    }
}
