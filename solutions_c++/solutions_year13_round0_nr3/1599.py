/*lcfr*/




#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<cmath>


#define FO(i,s,e,p) for(int i=(s);i<int(e);i+=p)
#define FOD(i,s,e,p) for(int i=(s);i>int(e);i-=p)


#define FOR(i,s,e) FO(i,s,e,1)
#define FORE(i,s,e) FOR(i,s,e+1)
#define FORD(i,s,e) FOD(i,s,e,1)
#define FORDE(i,s,e) FORD(i,s,e-1)

#define ALL(i,s) for(__typeof((s).begin()) i=(s).begin();i!=(s).end();i++)

#define MEM(tab,fill) memset(tab,fill,sizeof(tab))

#include<iostream>
#include<set>
#include<vector>
#include<string>
#include<sstream>
#include<stack>
#include<queue>
#include<algorithm>
#include<utility>
#include<bitset>
#include<map>
#include<cassert>

using namespace std;


#define pb push_back
#define ll long long
#define EPS 0.0000001
#define MOD 1000000009LL
#define mp make_pair
#define fi first
#define se second
#define inf ((1<<29)-1)
#define deb(a) cout<<#a<<' '<<a<<endl;
#define PI pair<ll,ll>
#define llu unsigned ll

#define AL(a) (a).begin(),(a).end()

vector<ll> inz;

vector<int> x;
inline bool chk(ll a){
    x.clear();
    while(a) x.pb(a%10),a/=10;

    bool ki=1;
    for(int i=0,j=x.size()-1;i<j && ki;i++,j--) ki&=(x[i]==x[j]);
    return ki;
}
void pre(){
    FOR(i,1,10000010){
        if(!chk(i)) continue;
        if(!chk(i*1LL*i)) continue;
        inz.pb(i*1LL*i);
    }

    deb("end");
}

ll solve(ll a){
    int s1=upper_bound(AL(inz),a)-inz.begin();
    return s1;
}

int main() {

    pre();
    int he;
    cin>>he;
    freopen("C:\\a","r",stdin);
    freopen("C:\\w","w",stdout);
    int t;cin>>t;
    FORE(i,1,t){
        printf("Case #%d: ",i);
        ll a,b;
        cin>>a>>b;
        cout<<(solve(b)-solve(a-1));
        cout<<endl;
    }


    return 0;
}
