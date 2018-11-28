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
const int N=4;


int n,p[N],f[1<<N];
string s[N];
bool check(){
    REP(i,0,n) p[i]=i;
    for(;;){
        memset(f,0,sizeof(f));
        f[0]=1;
        REP(i,0,(1<<n)-1) if (f[i]){
            int pos=p[__builtin_popcount(i)];
            bool ok=0;
            REP(j,0,n) if (s[pos][j]=='1'){
                if (!(i&(1<<j))) {
                    f[i|(1<<j)]=1;
                    ok=1;
                }
            }
            if (!ok) return 0;
        }
        if (!next_permutation(p,p+n)) break;
    }
//    REP(i,0,n) cout<<s[i]<<'\n';ENDL;
    return 1;
}
int build(int pos,int cur,int use){
    if (pos==n){
        if (check()) return use;
        return inf;
    }
    if (cur==n) return build(pos+1,0,use);
    int ans=inf;
    if (s[pos][cur]=='0'){
        s[pos][cur]='1';
        ans=min(ans,build(pos,cur+1,use+1));
        s[pos][cur]='0';
    }
    ans=min(ans,build(pos,cur+1,use));
    return ans;
}
int solve(){
    return build(0,0,0);
}
int main(){
    freopen("input.inp","r",stdin);
    OUTPUT;
    int test;
    cin>>test;
    FOR(te,1,test){
        cin>>n;
        REP(i,0,n) cin>>s[i];
        printf("Case #%d: %d\n",te,solve());
    }
}
