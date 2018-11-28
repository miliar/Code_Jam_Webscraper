#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

typedef int _loop_int;
#define REP(i,n) for(_loop_int i=0;i<(_loop_int)(n);++i)
#define FOR(i,a,b) for(_loop_int i=(_loop_int)(a);i<(_loop_int)(b);++i)
#define FORR(i,a,b) for(_loop_int i=(_loop_int)(b)-1;i>=(_loop_int)(a);--i)

#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define DEBUG_VEC(v) cout<<#v<<":";REP(i,v.size())cout<<" "<<v[i];cout<<endl
#define ALL(a) (a).begin(),(a).end()

#define CHMIN(a,b) a=min((a),(b))
#define CHMAX(a,b) a=max((a),(b))

// mod
const ll MOD = 1000000007ll;
#define FIX(a) ((a)%MOD+MOD)%MOD

// floating
typedef double Real;
const Real EPS = 1e-11;
#define EQ0(x) (abs(x)<EPS)
#define EQ(a,b) (abs(a-b)<EPS)
typedef complex<Real> P;

void solve(){
  string s;
  cin>>s;
  int k;
  cin>>k;
  int n = s.size();
  int ans = 0;
  REP(i,n-k+1){
    if(s[i]=='-'){
      // flip
      REP(j,k)s[i+j] = s[i+j]=='+' ? '-' : '+';
      ans++;
    }
  }
  if(count(ALL(s),'-')>0){
    puts("IMPOSSIBLE");
  }else{
    printf("%d\n",ans);
  }
}

int main(){
  int t;
  scanf("%d",&t);
  REP(i,t){
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}
