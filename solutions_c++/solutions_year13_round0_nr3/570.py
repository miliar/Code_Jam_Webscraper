#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

typedef long long ll;

vector<ll> V;

ll str_to_ll(string s){	
  ll n = 1LL;
  ll vys = 0LL;
  for(int i=s.size()-1; i>=0; i--){vys += n*(s[i]-'0'); n*=10LL;}
  return vys;
}

string ll_to_str(ll x){ //reverse
  ll c = x;
  string s;
  while(c>0){
    s += (c%10LL) + '0';
    c /= 10LL;
  }
  return s;
}

string rev_str(string s){
  string o;
  for(int i=s.size()-1; i>=0; i--) o+=s[i];
  return o;
}

bool is_palin(ll x){
  string s = ll_to_str(x);
  if(s == rev_str(s)) return 1;
  return 0;
}

void vsetky_pal(){	// do 10^14 -> 2. mocniny 1 - 10^7
  for(ll i=1; i<10000; i++){
    string s2 = ll_to_str(i);
    string s1 = rev_str(s2);
    string pal1 = s1; pal1 += s2;
    string pal2 = s1; pal2.resize(pal2.size()-1); pal2 += s2;
    ll a = str_to_ll(pal1);
    ll b = str_to_ll(pal2);
    if(is_palin(a*a)) V.push_back(a*a);
    if(is_palin(b*b)) V.push_back(b*b);
  }
  sort(V.begin(), V.end());
}

int main(){
  vsetky_pal();
  //for(int i=0; i<V.size(); i++) printf("%lld\n", V[i]);
  ll T,a,b;
  scanf("%lld", &T);
  for(int t=0; t<T; t++){
    scanf("%lld %lld", &a, &b);
    ll x = lower_bound(V.begin(), V.end(),a) - V.begin();
    ll y = upper_bound(V.begin(), V.end(),b) - V.begin();
    printf("Case #%lld: %lld\n",t+1LL,y-x);
  }
  return 0;
}