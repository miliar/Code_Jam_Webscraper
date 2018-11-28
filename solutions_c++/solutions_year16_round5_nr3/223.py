#include <bits/stdc++.h>

using namespace std;

#define X first
#define Y second
#define INPUT freopen("codejam.inp","r",stdin)
#define OUTPUT freopen("codejam.out","w",stdout)
#define FOR(i,l,r) for(auto i=(l);i<=(r);i++)
#define REP(i,l,r) for(auto i=(l);i<(r);i++)
#define FORD(i,l,r) for(auto i=(l);i>=(r);i--)
#define REPD(i,l,r) for(auto i=(l);i>(r);i--)
#define ENDL printf("\n")
#define debug 1

typedef long long ll;
typedef pair<int,int> ii;

const int inf=1e9;
const int MOD=1e9+7;
const int N=1e3+10;

int n,m;
int d[N],h[N];
struct point{
    int x,y,z;
    point (int _x=0,int _y=0,int _z=0){
        x=_x;y=_y;z=_z;
    }
}a[N],v[N];
int sqr(int x){
    return x*x;
}
int dist(point a,point b){
    return sqr(a.x-b.x)+sqr(a.y-b.y)+sqr(a.z-b.z);
}
void prepare(){
    scanf("%d%d",&n,&m);
    FOR(i,1,n) scanf("%d%d%d%d%d%d",&a[i].x,&a[i].y,&a[i].z,&v[i].x,&v[i].y,&v[i].z);
}
double solve(){
    fill(d,d+n+1,inf);
    memset(h,0,sizeof(h));
    d[1]=0;
    FOR(pha,1,n){
        int st=0;
        FOR(i,1,n) if (!h[i]&&d[i]<d[st]) st=i;
        h[st]=1;
        FOR(i,1,n) if (!h[i]) d[i]=min(d[i],max(d[st],dist(a[st],a[i])));
    }
    return sqrt(d[2]);
}
int main(){
    freopen("input.inp","r",stdin);
    OUTPUT;
    int test;
    scanf("%d",&test);
    FOR(te,1,test){
        prepare();
        printf("Case #%d: %.6f\n",te,solve());
    }
}
