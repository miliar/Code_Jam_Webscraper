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
const int N=12;
const string name="PRS";

string dict[20][3];
int level,nr,np,ns;
void prepare(){
    FOR(i,0,2) dict[0][i]=name[i];
    FOR(lv,1,N){
        FOR(i,0,2){
            string s1=dict[lv-1][i],s2=dict[lv-1][(i+1)%3];
            if (s1>s2) swap(s1,s2);
            dict[lv][i]=s1+s2;
//            cout<<lv<<" "<<i<<" "<<dict[lv][i]<<"\n";
        }
    }
}
string solve(){
    FOR(i,0,2) {
        bool ok=1;
        if (count(dict[level][i].begin(),dict[level][i].end(),'R')!=nr) ok=0;
        if (count(dict[level][i].begin(),dict[level][i].end(),'P')!=np) ok=0;
        if (count(dict[level][i].begin(),dict[level][i].end(),'S')!=ns) ok=0;
        if (ok) return dict[level][i];
    }
    return "IMPOSSIBLE";
}
int main(){
    freopen("input.inp","r",stdin);
    OUTPUT;
    prepare();
    int test;
    cin>>test;
    FOR(te,1,test){
        cin>>level>>nr>>np>>ns;
        printf("Case #%d: ",te);
        cout<<solve()<<'\n';
    }
}
