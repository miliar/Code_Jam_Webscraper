#include <bits/stdc++.h>

using namespace std;

#define X first
#define Y second
#define INPUT freopen("codejam.inp","r",stdin)
#define OUTPUT freopen("codejam2.out","w",stdout)
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
const int N=2e2+10;

int n,k,p[N];
double a[N],f[N][N<<1];
void prepare(){
    cin>>n>>k;
    FOR(i,1,n) cin>>a[i];
    sort(a+1,a+n+1);
}
double solve(){
    double ans=-1;
    FOR(L,0,k){
        FOR(i,1,L) p[i]=i;
        REP(i,0,k-L) p[L+i+1]=n-i;
        FOR(i,1,k)
            REP(j,0,N<<1) f[i][j]=.0;
        f[0][N]=1;
        FOR(i,1,k)
            FOR(j,-i,i) {
                f[i][j+1+N]+=f[i-1][j+N]*a[p[i]];
                f[i][j-1+N]+=f[i-1][j+N]*(1-a[p[i]]);
            }
        ans=max(ans,f[k][N]);
    }
    return ans;
}
int main(){
    freopen("input.inp","r",stdin);
    OUTPUT;
    int test;
    cin>>test;
    FOR(te,1,test){
        prepare();
        printf("Case #%d: %.6f\n",te,solve());
    }
}
