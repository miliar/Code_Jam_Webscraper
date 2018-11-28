#include <algorithm>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;
#define PB push_back
#define MP make_pair
#define sz(v) ((v).size())
#define forn(i,n) for(int i=0;i<(n);i++)
#define forv(i,v) forn(i,sz(v))
typedef long long in;
typedef unsigned long long int llu;

void runtc();

int main(){
  std::ios::sync_with_stdio(false);
  std::cin.tie(0);

  int ntc;
  cin>>ntc;
  cout<<setprecision(20);
  for(int i=0;i<ntc;++i) {
    cout<<"Case #"<<(i+1)<<": ";
    runtc();
    cout<<endl;
  }
  
  return 0;
}

struct Water {
  double rate;
  double temp;
  Water(double rate, double temp):rate(rate),temp(temp){};
};
//=============================================================================
void runtc() {
  int N;
  double V, X;
  cin>>N>>V>>X;
  double VX = V*X;
  const double EPSILON = 1e-15;

  vector<Water> w;
  map<double, double> mp;
  forn(i,N) {
    double r, x;
    cin>>r>>x;
    if(mp.find(x)==mp.end()) {
      mp[x]=r;
    } else {
      mp[x] = mp[x]+r;
    }
  }
  for(auto i = mp.begin(); i!=mp.end();++i) {
    w.push_back(Water(i->second,i->first));
  }

  if(w.size()==1) {
    if(X != w[0].temp) {
      cout<<"IMPOSSIBLE";
      return;
    }
    cout<<V/w[0].rate;
    return;
  } else if(w.size()==2) {
    double c1 = w[0].temp;
    double c2 = w[1].temp;
    double r1 = w[0].rate;
    double r2 = w[1].rate;
    if((c1<X && c2<X) || (c1>X && c2>X)) {
      cout<<"IMPOSSIBLE";
      return;
    }
    double t1 = (c2*V-VX)/((c2-c1)*r1);
    double t2 = -(c1*V-VX)/((c2-c1)*r2);
    cout<<max(t1,t2);
    return;
  }
  cout<<"???";

}
