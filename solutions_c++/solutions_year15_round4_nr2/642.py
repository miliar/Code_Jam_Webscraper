#include <bits/stdc++.h>

using namespace std;

#define X first
#define Y second
#define INPUT freopen("B.inp","r",stdin)
#define OUTPUT freopen("B.out","w",stdout)
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
const double eps=1e-8;

int n,test;
double V[N],T[N];
void solve(){
    if (n==1){
        if (abs(T[1]-T[0])>eps){
            printf("IMPOSSIBLE\n");
            return;
        }
        printf("%.8f\n",V[0]/V[1]);
    }else{
        if (abs(T[1]-T[2])<eps){
            V[1]+=V[2];
            n=1;
            solve();
            return;
        }
        if (T[1]>T[2]) {
            swap(V[1],V[2]);
            swap(T[1],T[2]);
        }
        if (T[2]<T[0]||T[1]>T[0]){
            printf("IMPOSSIBLE\n");
            return;
        }
        double V2=V[0]*(T[0]-T[1])/(T[2]-T[1]),V1=V[0]-V2;
        printf("%.8f\n",max(V2/V[2],V1/V[1]));
    }
}
int main(){
    INPUT;OUTPUT;
    scanf("%d",&test);
    FOR(te,1,test){
        scanf("%d%lf%lf",&n,V,T);
        FOR(i,1,n) scanf("%lf%lf",V+i,T+i);
        printf("Case #%d: ",te);
        solve();
    }
}
