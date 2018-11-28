#include <bits/stdc++.h>

using namespace std;

#define X first
#define Y second
#define INPUT freopen("A.inp","r",stdin)
#define OUTPUT freopen("A.out","w",stdout)
#define FOR(i,l,r) for(auto i=l;i<=r;i++)
#define REP(i,l,r) for(auto i=l;i<r;i++)
#define FORD(i,l,r) for(auto i=l;i>=r;i--)
#define REPD(i,l,r) for(auto i=l;i>r;i--)
#define ENDL printf("\n")
#define debug 1

typedef long long ll;
typedef pair<int,int> ii;

const int inf=1e9;
const int MOD=1e9+7;
const int N=1e2+10;
const char use[6]=".^v<>";
const int dx[4]={-1,1,0,0},dy[4]={0,0,-1,1};

int g[2][N],a[N][N],test,n,m;
char s[N];
int cv(char c){
    int ans=0;
    while (use[ans]!=c) ans++;
    return ans;
}
bool ok(int x,int y){
    return (x&&x<=n&&y&&y<=m);
}
void prepare(){
    memset(g,0,sizeof(g));
    scanf("%d%d",&n,&m);
    FOR(i,1,n){
        scanf("\n%s",s);
        FOR(j,1,m) {
            a[i][j]=cv(s[j-1]);
            if (a[i][j]) g[0][i]++,g[1][j]++;
        }
    }
}
void solve(){
    int ans=0;
    FOR(i,1,n)
        FOR(j,1,m) if (a[i][j]){
            if (g[0][i]==1&&g[1][j]==1){
                printf("IMPOSSIBLE\n");
                return;
            }
            int type=a[i][j]-1,x=i+dx[type],y=j+dy[type];
            while (ok(x,y)&&!a[x][y]) x+=dx[type],y+=dy[type];
            if (!ok(x,y)) ans++;
        }
    printf("%d\n",ans);
}
int main(){
    INPUT;OUTPUT;
    scanf("%d",&test);
    FOR(te,1,test){
        prepare();
        printf("Case #%d: ",te);
        solve();
    }
}
