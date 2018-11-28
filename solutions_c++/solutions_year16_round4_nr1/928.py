#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef complex<double> P;
typedef pair<int,int> pii;
#define REP(i,n) for(ll i=0;i<n;++i)
#define REPR(i,n) for(ll i=1;i<n;++i)
#define FOR(i,a,b) for(ll i=a;i<b;++i)

#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define DEBUG_VEC(v) cout<<#v<<":";REP(i,v.size())cout<<" "<<v[i];cout<<endl
#define ALL(a) (a).begin(),(a).end()

#define MOD (ll)(1e9+7)
#define ADD(a,b) a=((a)+(b))%MOD
#define FIX(a) ((a)%MOD+MOD)%MOD

string s[13][3];

void init(){
  s[0][0] = "0";
  s[0][1] = "1";
  s[0][2] = "2";
  REPR(i,13){
    REP(j,3){
      string a = s[i-1][j];
      string b = s[i-1][(j+2)%3];
      s[i][j] = min(a,b) + max(a,b);
    }
  }
  map<char,char> mp;
  mp['0'] = 'P';
  mp['1'] = 'R';
  mp['2'] = 'S';
  REP(i,13)REP(j,3){
    REP(k,s[i][j].size()){
      s[i][j][k] = mp[s[i][j][k]];
    }
  }
}

void solve(){
  int n;
  ll a,b,c;
  scanf("%d%lld%lld%lld",&n,&a,&b,&c);
  REP(k,3){
    string t = s[n][k];
    ll aa = count(ALL(t),'R');
    ll bb = count(ALL(t),'P');
    ll cc = count(ALL(t),'S');
    if(aa==a && bb==b && cc==c){
      puts(t.c_str());
      return;
    }
  }
  printf("IMPOSSIBLE\n");
  return;
}

int main(){
  int t;
  scanf("%d",&t);
  init();
  REP(i,t){
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}
