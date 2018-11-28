#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

const int Dx[4]={-1,0,1,0};
const int Dy[4]={0,1,0,-1};
int T,r,c,n,a[222],w,h,cnt;
int mark[222][222];
char res[222][222];

void go(int x, int y){
    mark[x][y]=cnt;
    for(int k=0; k<4; ++k){
        int xt=x+Dx[k], yt=y+Dy[k];
        if(xt<0 || yt<0 || xt>h || yt>w || mark[xt][yt]) continue;
        go(xt,yt);
    }
}

int getMark(int id){
    int x,y;
    if(id<=c){
        x=0; y=(id-1)*4+2;
    }else if(id<=c+r){
        y=w;
        x=(id-c-1)*4+2;
    }else if(id<=c+r+c){
        x=h;
        y=w-((id-c-r-1)*4+2);
    }else{
        y=0;
        x=h-((id-c-r-c-1)*4+2);
    }
    return mark[x][y];
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%d",&T);
    for(int tt=1; tt<=T; ++tt){
        scanf("%d%d",&r,&c);
        n=2*(r+c);
        for(int i=1; i<=n; ++i) scanf("%d",&a[i]);
        w = c*4;
        h = r*4;
        bool found=0;
        for(int mask=0; mask<(1<<(r*c)); ++mask){
            int it=0;
            for(int x=0; x<=h; ++x) for(int y=0; y<=w; ++y) mark[x][y]=0;
            for(int i=0; i<r; ++i) for(int j=0; j<c; ++j){
                if(mask>>it&1) res[i][j]='/';
                else res[i][j]='\\';
                int x=2+i*4;
                int y=2+j*4;
                int dx=1, dy=1;
                if(res[i][j]=='/') dy=-1;
                for(int k=-2; k<=2; ++k) mark[k*dx+x][k*dy+y] = -1;
                ++it;
            }

            cnt = 0;
            for(int x=0; x<=h; ++x) for(int y=0; y<=w; ++y) if(!mark[x][y]){
                ++cnt;
                go(x,y);
            }
            bool ok=1;
            set<int> mys;
            for(int i=1; i<=n; i+=2){
                if(getMark(a[i])==getMark(a[i+1]) && !mys.count(getMark(a[i]))){
                    mys.insert(getMark(a[i]));
                }else{
                    ok=0;
                    break;
                }
            }
            if(ok){
                found=1;
                break;
            }
        }
        printf("Case #%d:\n",tt);
        if(!found) puts("IMPOSSIBLE");
        else{
            for(int i=0; i<r; ++i){
                for(int j=0; j<c; ++j) printf("%c",res[i][j]);
                puts("");
            }
        }
    }
}

