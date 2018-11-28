#include <bits/stdc++.h>

using namespace std;

#define X first
#define Y second
#define INPUT freopen("C.inp","r",stdin)
#define OUTPUT freopen("C.out","w",stdout)
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
const int N=22,M=4e2+10;

string s;
int n,m,g[M][2],Sans,test;
vector <ll> a[N];
map <ll,int> ma;
void prepare(){
    memset(g,0,sizeof(g));
    scanf("%d\n",&n);
    FOR(i,1,n) a[i].clear();
    ma.clear();
    FOR(i,1,n){
        getline(cin,s);
        int m1=s.length();
        REP(j,0,m1){
            ll val=0;
            while (j<m1&&s[j]>='a'&&s[j]<='z') val=val*29+(s[j++]-'a'+1);
            a[i].push_back(val);
        }
    }
    m=0;Sans=0;
    FOR(i,3,n)
        for(auto &j:a[i]){
            if (!ma[j]) ma[j]=++m;
            j=ma[j];
        }
    //printf("tick\n");
    for(auto j:a[1]){
        int v=ma[j];
        if (v&&v<=m) g[v][0]=-1;
        else ma[j]=m+1;
        //printf("%lld %d\n",j,v);
    }
    for(auto j:a[2]){
        int v=ma[j];
        if (v){
            if (v>m) Sans++,ma[j]=0;
            else g[v][1]=-1;
        }
    }
}
int check(int idx){
    FOR(i,3,n){
        int type=(idx&(1<<(i-3)))>0;
        for(auto j:a[i]) if (!g[j][type]) g[j][type]=1;
    }
    int ans=0;
    FOR(i,1,m) if (g[i][0]&&g[i][1]) ans++;
    return ans;
}
int solve(){
    //cout<<ans<<'\n';
    int cans=inf;
    if (n>2) REP(i,0,1<<(n-2)) {
        FOR(j,1,m)
            FOR(k,0,1) if (g[j][k]!=-1) g[j][k]=0;
        cans=min(cans,check(i));
    }else return 0;
    return cans;
}
int main(){
    INPUT;OUTPUT;
    scanf("%d\n",&test);
    FOR(te,1,test){
        prepare();
        printf("Case #%d: %d\n",te,Sans+solve());
    }
}
