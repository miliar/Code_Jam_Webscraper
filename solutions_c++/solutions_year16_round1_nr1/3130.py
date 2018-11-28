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

char q[N<<1];
string s;
int main(){
    freopen("input.inp","r",stdin);
    OUTPUT;
    int test;
    cin>>test;
    FOR(te,1,test){
        cin>>s;
        printf("Case #%d: ",te);
        int top=N,bot=N;
        int n=s.length();
        q[top]=s[0];
        REP(i,1,n) if (s[i]>=q[top]) q[--top]=s[i];
        else q[++bot]=s[i];
        FOR(i,top,bot) printf("%c",q[i]);ENDL;
    }
}
