#include <bits/stdc++.h>
using namespace std;
#define all(c) (c).begin(),(c).end()
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define REP(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) REP(i,0,n)
#define iter(c) __typeof((c).begin())
#define tr(it,c) for(iter(c) it=(c).begin();it!=(c).end();it++)
#define mem(a) memset(a,0,sizeof(a))
#define pd(a) printf("%.10f\n",a)
#define pb(a) push_back(a)
#define in(a) insert(a)
#define pi M_PI
#define R cin>>
#define F first
#define S second
#define C class
#define ll long long
#define ln cout<<'\n'
#define _(_1,_2,_3,N,...)N
#define pr(...) _(__VA_ARGS__,pr3,pr2,pr1)(__VA_ARGS__)
template<C T>void pr1(T a){cout<<a;ln;}
template<C T,C T2>void pr2(T a,T2 b){cout<<a<<' '<<b;ln;}
template<C T,C T2,C T3>void pr3(T a,T2 b,T3 c){cout<<a<<' '<<b<<' '<<c;ln;}
template<C T>void PR(T a,int n){rep(i,n){if(i)cout<<' ';cout<<a[i];}ln;}
bool check(int n,int m,int x,int y){return x>=0&&x<n&&y>=0&&y<m;}
const ll MAX=1000000007,MAXL=1LL<<60,dx[4]={-1,0,1,0},dy[4]={0,1,0,-1};
typedef pair<int,int> P;

vector<ll> N(ll n) {
  vector<ll> v;
  for(ll i=2; i*i<=n; i++) {
    if(n%i==0) {
      v.pb(i);
      if(i*i!=n) v.pb(n/i);
    }
  }
  sort(all(v));
  return v;
}

void Main() {
  int T;
  R T;
  REP(tt,1,T+1) {
    cout << "Case #" << tt << ":" << endl;
    ll n,m;
    cin >> n >> m;
    ll c=0;
    for(ll t=0; t<(1<<(n-2)); t++) {
      ll x=(1LL<<(n-1))+(t<<1)+1;
      string s="";
      ll y=x;
      while(y) {
        if(y%2) s+='1';
        else s+='0';
        y/=2;
      }
      vector<ll> v[11];
      REP(i,2,11) {
        ll d=0,z=1;
        rrep(j,s.size()) {
          if(s[j]=='1') d+=z;
          z*=i;
        }
        v[i]=N(d);
        if(!v[i].size()) goto next;
      }
      cout << s;
      REP(i,2,11) cout << " " << v[i][0];
      ln;
      c++;
      if(c==m) break;
    next:;
    }
  }
}

int main() {
  ios::sync_with_stdio(0);cin.tie(0);
  Main();return 0;
}
