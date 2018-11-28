#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
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
#include <cstring>
#include <sstream>
#include <cassert>
#include <ctime>
#include <list>
#include <numeric>
#include <fstream>

using namespace std;
static const double EPS = 1e-8;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> PI;
#ifndef M_PI
const double M_PI=acos(-1.0);
#endif
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define FORR(i,c) for(__typeof((c).rbegin())i=(c).rbegin();i!=(c).rend();++i)
#define ALL(c) (c).begin(), (c).end()
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define SZ(a) (int((a).size()))
#define F first
#define S second
int dx[]={0,-1,0,1,1,1,-1,-1},dy[]={1,0,-1,0,1,-1,1,-1};

string ret;
string add(const string&a,const string&b){
  int as=a.size(),bs=b.size();
  ret.resize(max(as,bs));
  int c=0;
  rep(i,max(as,bs)){
    int t=c;
    if(i<as)t+=a[as-i-1]-'0';
    if(i<bs)t+=b[bs-i-1]-'0';
    c=t/10;
    t%=10;
    ret[i]=t+'0';
  }
  if(c)ret+=c+'0';
  reverse(ALL(ret));
  return ret;
}

string mulcret;
string multc(char m,const string&a){
  if(m=='1') return a;
  if(m=='0') return "0";
  m-='0';
  mulcret.clear();

  int c=0;
  int as=a.size();
  rep(i,as){
    int t=c+m*(a[as-i-1]-'0');
    c=t/10;
    t%=10;
    mulcret+=t+'0';
  }
  if(c)mulcret+=c+'0';
  reverse(ALL(mulcret));
  return mulcret;
}

string mulret;
string mult(const string&a,string b){
  mulret.clear();
  int as=a.size();
  
  rep(i,as){
    mulret=add(mulret,multc(a[as-i-1],b));
    b+='0';
  }
  return mulret;
}


char dig[1000];
int cnt;
vector<pair<int,string> > bef;

void even(int depth,int sum){
  if(depth>=30) return;
  if(sum>5) return;
  if(++cnt%5000==0){
    cerr << cnt << ' ' << depth << ' ' << sum << endl;
  }

  if(depth){
    string ss(dig,dig+depth),tt(dig,dig+depth);
    reverse(ALL(tt));
    ss += tt;
    tt=mult(ss,ss);
    bool ok = true;
    rep(i,SZ(tt))
      if(tt[i] != tt[SZ(tt)-1-i]){
        ok=false;
        break;
      }
      
    if(ok)bef.pb(mp(SZ(tt),tt));
  }

  
  rep(k,4){
    if(k==0 && depth==0) continue;
    dig[depth]=k+'0';
    if(2*sum+k*k<10){
      ++cnt;
      string ss(dig,dig+depth),tt(dig,dig+depth);
      reverse(ALL(tt));
      ss += (k+'0');
      ss += tt;
      tt=mult(ss,ss);
      bool ok = true;
      rep(i,SZ(tt))
        if(tt[i] != tt[SZ(tt)-1-i]){
          ok=false;
          break;
        }
      
      if(ok)bef.pb(mp(SZ(tt),tt));
      //bef.pb(mp(depth+1,string(dig,dig+depth+1)));
    }
    even(depth+1,sum+k*k);
  }
  dig[depth]='0';
}


void solve(int ca){
  string a,b;
  cin >> a >> b;
  printf("Case #%d: %d\n",ca,
         upper_bound(ALL(bef),mp(SZ(b),b))-lower_bound(ALL(bef),mp(SZ(a),a)));
}

main(){
  memset(dig,'0',sizeof(dig));
  even(0,0);
  cerr << SZ(bef) << endl;
  sort(ALL(bef));
  rep(i,100) cerr << bef[i].S << endl;

  int t;
  cin >> t;
  rep(i,t) solve(i+1);
}
