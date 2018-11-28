#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

int T,n,res,added;
char a[5][5];
int b[5][5];
bool mark[5][5],mx[5],my[5];

void go(int x, int y){
    mx[x]=1; my[y]=1;
    mark[x][y]=1;
    for(int xt=1; xt<=n; ++xt) if(b[xt][y] && !mark[xt][y]) go(xt,y);
    for(int yt=1; yt<=n; ++yt) if(b[x][yt] && !mark[x][yt]) go(x,yt);
}

bool check(int mask){
    int it=0;
    added = 0;
    for(int i=1; i<=n; ++i) for(int j=1; j<=n; ++j){
        b[i][j]=mask>>it&1;
        if(b[i][j]==0 && a[i][j]=='1') return 0;
        if(b[i][j]==1 && a[i][j]=='0') ++added;
        ++it;
    }

    reset(mark,0);
    int cnt=0;
    for(int i=1; i<=n; ++i) for(int j=1; j<=n; ++j) if(b[i][j] && !mark[i][j]){
        reset(mx,0); reset(my,0);
        go(i,j);
        int cx=0,cy=0;
        for(int i=1; i<=n; ++i){
            if(mx[i]) ++cx;
            if(my[i]) ++cy;
        }
        if(cx!=cy) return 0;
        cnt += cx;
        for(int i=1; i<=n; ++i) for(int j=1; j<=n; ++j) if(mx[i] && my[j] && !b[i][j]) return 0;
    }
    return cnt==n;
}

int main(){
//    freopen("input.txt","r",stdin);
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    for(int tt=1; tt<=T; ++tt){
        scanf("%d",&n);
        for(int i=1; i<=n; ++i) scanf("%s",a[i]+1);
        int res = oo;
        for(int mask=0; mask<(1<<(n*n)); ++mask){
            if(check(mask)){
                res=min(res, added);
            }
        }
        printf("Case #%d: %d\n",tt,res);
    }

}

