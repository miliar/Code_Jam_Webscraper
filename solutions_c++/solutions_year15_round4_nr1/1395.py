#include <cstdio>
#include <vector>

char map[111][111];
bool cannot[4][111][111];
int n,m;

int conv(char x){
    if(x=='<') return 0;
    if(x=='>') return 1;
    if(x=='^') return 2;
    if(x=='v') return 3;
    return -1;
}

int main()
{
    freopen("D:\\gcj\\in.txt","r",stdin);
    freopen("D:\\gcj\\out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int _;
    int i,j, ans=0; int k;
    for(_=1;_<=t;++_){
        scanf("%d%d",&n,&m);
        ans=0;
        for(i=0;i<n;++i) scanf("%s",map[i]);
        for(i=0;i<n;++i)for(j=0;j<m;++j) for(k=0;k<4;++k) cannot[k][i][j]=false;
        for(i=0;i<n;++i){
            for(j=0;j<m;++j)    if(map[i][j]!='.'){ cannot[0][i][j]=true; break; }
            for(j=m-1;0<=j;--j) if(map[i][j]!='.'){ cannot[1][i][j]=true; break; }
        }
        for(j=0;j<m;++j){
            for(i=0;i<n;++i)    if(map[i][j]!='.'){ cannot[2][i][j]=true; break; }
            for(i=n-1;0<=i;--i) if(map[i][j]!='.'){ cannot[3][i][j]=true; break; }
        }
        for(i=0;i<n;++i){
            for(j=0;j<m;++j){
                if(map[i][j]=='.') continue;
                for(k=0;k<4;++k) if(!cannot[k][i][j]) break;
                if(k==4) {
                    printf("Case #%d: IMPOSSIBLE\n",_);
                    break;
                } else {
                    if(cannot[conv(map[i][j])][i][j]) {
                        ++ans;
                    }
                }
            }
            if(j!=m) break;
        }
        if(i!=n) continue;
        printf("Case #%d: %d\n",_,ans);
    }
    return 0;
}
