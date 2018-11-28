#include <cstdlib> 
#include <numeric>
#include <cstring>
#include <cstdio> 
#include <cfloat> 
#include <map> 
#include <cassert>
#include <cmath> 
#include <climits> 
#include <utility> 
#include <set> 
#include <iostream> 
#include <memory> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <sstream> 
#include <complex> 
#include <stack> 
#include <queue> 
#include <iomanip>
#include<sys/time.h>
using namespace std; 
double e_time(void){static struct timeval now;gettimeofday(&now, NULL);return (double)(now.tv_sec  + now.tv_usec/1000000.0);}
#define REP(i,b,n) for(int i=b;i<n;i++) 
#define rep(i,n)      REP(i,0,n) 
#define pb push_back  
#define mp make_pair 
#define ALL(C)   (C).begin(),(C).end() 
#define fe(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr != (c).end();itr++)
#define BITSHIFT(X)     ( (1<<(X)) )
#define CONTAIN(S,X) ( ((S)&BITSHIFT(X)) != 0)
typedef complex<double>P; 
typedef long long ll; 
typedef unsigned long long ull; 
typedef pair<int,int> pii; 
typedef vector<int> vint;
double e_time(void);
template<class T> void pvRaw(T a, T b){for(;a != b;++a){cout << *a <<" " ;}cout << endl;}
template<class T> void pvRaw(T * a, int n){for(int i = 0;i < n;++i){cout << a[i] << " " ;}cout << endl;}
template<class T> void pvRaw(T & a, int n){for(int i = 0;i < n;++i){cout << a[i] << " ";}cout << endl;}
#define pv(var, a, n) do{cout << "line:" << __LINE__ << " " << #var << " : "; pvRaw(a, n);}while(0)
template<class T> T ceilUp(const T& a,const T& b){return (a+b-1)/b;}
const ll mod = 1000002013LL;
inline ll modadd(ll a,ll b){a %= mod;b %= mod;return (a+b)%mod;}
inline ll modsub(ll a,ll b){a %= mod;b %= mod;a-=b;a%=mod;if (a<0)a+=mod;return a;}
inline ll modmul(ll a,ll b){a %= mod;b %= mod;return (a*b)%mod;}
inline ll modeq(ll a,ll b,ll m){a = (a%m+m)%m; b = (b%m+m)%m;return a == b;}
ll mypow(ll n,ll p){if (p == 0)return 1;if (p == 1)return n;ll ret=mypow(n,p/2);ret=ret*ret%mod;if (p&1)ret=ret*n%mod;return ret;}
ll getinv(ll a){return 500001007LL;}
inline ll moddiv(ll a, ll b){
  return (a * getinv(b)) % mod;
}

bool isOk(int beg, int end,vector<int> & in, vector<int> &used){
  int cnt = 0;
  for(int i = beg + 1;i < end;i++){
    if (used[i]){
      continue;
    }
    if (in[i] > 0){
      cnt++;
    } else if (in[i] < 0){
      cnt--;
    }
    if (cnt < 0){
      return false;
    }
  }
  return cnt == 0;
}

bool cmp(const pair<ll, ll> & ta,const pair<ll, ll> & tb){
  ll a = ta.first, b = tb.first;
  if (a > 0 && b > 0){
    return a < b;
  } else if (a < 0 && b < 0){
    return -a < -b;
  } else {
    if (abs(a) == abs(b)){
      if (a < 0){
	return false;
      } else {
	return true;
      }
    }
    return abs(a) < abs(b);
  }
  return false;
}

ll solve(vector<pair<ll, ll> >& in,int n){
  ll ret = 0;
  stack<pair<ll, ll> > S;
  for(int i = 0;i < in.size();i++){
    if (in[i].first > 0){
      S.push(in[i]);
    } else {
      pair<ll, ll> e = in[i];
      e.first *= -1;
      while(e.second > 0){
	pair<ll, ll> b = S.top(); S.pop();
	ll num = min(b.second, e.second);
	e.second -= num;
	b.second -= num;
	//cout << b.first <<" " << e.first << " with " << b.second << " " << e.second << endl;
	if (b.second > 0){
	  S.push(make_pair(b.first, b.second - e.second));
	}
	//ret = modadd(ret, modmul(modsub(e, b), n));
	ret = modsub(ret, modmul(num, moddiv(modmul(modsub(e.first,b.first),modsub(modsub(e.first,b.first), 1)), 2)));
      }
    }
  }
  assert(S.size() == 0);
  return ret;
} 

int main(){
  int tc = 0,te = 0;
  cin>>te;
  while(te--){
    cout <<"Case #" << ++tc << ": ";
    int n, m;
    cin >> n >> m;
    vector<int> b(m), e(m), p(m);
    ll original = 0, ans = 0;
    for(int i = 0;i < m;i++){
      cin >> b[i] >> e[i] >> p[i];
      //original = modadd(original,modmul(modmul(modsub(e[i],b[i]),n),p[i]));
      original = modsub(original,modmul(moddiv(modmul(modsub(e[i],b[i]),modsub(modsub(e[i],b[i]),1)),2), p[i]));
    }
    vector<pair<ll, ll> > sol;
    for(int i = 0;i < m;i++){
      sol.push_back(make_pair( b[i], p[i]));
      sol.push_back(make_pair(-e[i], p[i]));
    }
    if (sol.size() == 0){
      break;
    }
    sort(sol.begin(), sol.end(), cmp);
    //pv(sol, sol, sol.size());
    ans = modadd(ans, solve(sol, n));
    ans = modsub(original, ans);
    cout << ans << endl;
  }
  return 0;
}


