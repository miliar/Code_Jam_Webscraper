#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;
typedef unsigned long long ull;

class Bignum{
public:
  Bignum(){}
  Bignum(string s){
    for(int i=0;i<s.length();i++) d.push_front(s[i]-'0');
    normalize();
  }
  Bignum &normalize(){
    for(int i=d.size()-1;i>=0;i--){ if(d[i]!=0) break; d.pop_back(); }
    return *this;
  }
  int operator[](int i){ return i>=d.size()?0:d[i]; }
  int size(){ return normalize(),d.size(); }
  void toZero(){ d.clear(); d.push_front(0); }
  void toOne(){ d.clear(); d.push_front(1); }
  Bignum &inc(){ Bignum one("1"); return operator+=(one); }
  Bignum &operator+=(Bignum n){
    int l=max(size(),n.size());
    d.resize(l+1,0);
    for(int c=0,i=0;i<=l;i++) d[i]=(c=d[i]+n[i]+c/10)%10;
    return normalize();
  }
  Bignum &operator-=(Bignum n){
    for(int c=0,i=0;i<d.size();i++) d[i]=((c=d[i]-n[i]+(c-9)/10)+10)%10;
    return normalize();
  }
  Bignum &operator*=(int n){
    for(int i=0;i<15;i++) d.push_back(0);
    for(int c=0,i=0;i<d.size();i++) d[i]=(c=d[i]*n+c/10)%10;
    return normalize();
  }
  Bignum &operator*=(ull n){
    for(int i=0;i<25;i++) d.push_back(0);
    for(ull c=0,i=0;i<d.size();i++) d[i]=(c=d[i]*n+c/10ULL)%10ULL;
    return normalize();
  }
  Bignum operator+(Bignum n){ return Bignum(*this)+=n; }
  Bignum operator-(Bignum n){ return Bignum(*this)-=n; }
  Bignum operator*(int n){ return Bignum(*this)*=n; }
  Bignum operator*(ull n){ return Bignum(*this)*=n; }
  Bignum operator*(Bignum n){
    Bignum ret;
    int ka=size(),kb=n.size();
    ret.d.resize(ka+kb,0);
    for(int i=0;i<ka;i++) for(int c=0,j=0;j<=kb;j++) ret.d[i+j]=(c=ret.d[i+j]+d[i]*n[j]+c/10)%10;
    return ret.normalize();
  }
  Bignum &operator*=(Bignum n){ return (*this)=(*this)*n; }

  int div(int n){
    int c=0;
    for(int i=size()-1;i>=0;i--) d[i]=(c=c%n*10+d[i])/n;
    return c%n;
  }
  Bignum &operator<<=(int n){
    for(int i=0;i<n;i++) d.push_front(0);
    return normalize();
  }
  Bignum operator<<(int n){ return Bignum(*this)<<=n; }
  bool operator>(Bignum n){
    if(size()!=n.size()) return size()>n.size();
    for(int i=size()-1;i>=0;i--) if(d[i]!=n[i]) return d[i]>n[i];
    return false;
  }
  deque<int> d;
};
pair<Bignum,Bignum> ldiv(Bignum a, Bignum b)
{
  Bignum ret;
  for(int i=a.size()-1;i>=0;i--){
    int n;
    for(n=1;n<10;n++) if(((b*n)<<i)>a) break;
    a-=(b*(n-1))<<i;
    ret.d.push_front(n-1);
  }
  return make_pair(ret.normalize(),a.normalize());
}
ostream &operator<<(ostream &os, const Bignum &l)
{
  Bignum n=l;
  if (n.size()==0) os<<0;
  else for (int i=n.d.size()-1;i>=0;i--) os<<n.d[i];
  return os;
}



unsigned long xor128(){
  static unsigned long x=123456789, y=362436069, z=521288629, w=88675123;
  unsigned long t;
  t=(x^(x<<11));
  x=y; y=z; z=w;
  return w=(w^(w>>19))^(t^(t>>8));
}

Bignum calc(const string& code, ll base){
  Bignum p("1");
  Bignum sum("0");
  for(int i=code.size()-1; i>=0; i--){
    if(code[i]=='1') sum += p;
    p *= (ull)base;
  }
  return sum;
}
ll divisor(Bignum n){
  Bignum i("2");
  Bignum mx("100");
  for(; !(i*i>n)&&!(i>mx); i.inc()){
    pair<Bignum,Bignum> res = ldiv(n, i);
    if(res.second.size() == 0 || (res.second.size() == 1 && res.second.d[0] == 0)){
      ll ret = 0;
      ll p = 1;
      rep(j,i.d.size()){
        ret += p*i.d[j];
        p *= 10;
      }
      return ret;
    }
  }
  return -1;
}
void solve(int N, int J){
  string code(N, '1');
  map<string,int> memo;
  int n = 0;
  while(n<J){
    for(int i=1; i<N-1; i++){
      if(xor128()%2 == 1){
        if(code[i]=='0') code[i] = '1';
        else code[i] = '0';
      }
    }
    if(memo.count(code) > 0) continue;
    bool flg = true;
    vector<ll> res;
    REP(base,2,11){
      ll r = divisor(calc(code, base));
      if(r < 0){ flg = false; break; }
        res.push_back(r);
    }
    if(!flg) continue;
    
    cout << code;
    rep(i,res.size()){
      cout << " " << res[i];
    }
    cout << endl;
      
    memo[code] = 1;
    n++;
  }
}

int main(){
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  rep(t,T){
    int N, J;
    cin >> N >> J;
    cout << "Case #" << t+1 << ":" << endl;
    solve(N, J);
  }
  
  return 0;
}


