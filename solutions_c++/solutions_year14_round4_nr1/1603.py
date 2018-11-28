#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<string>
#include<map>
#include<cstdio>
#include<cstdlib>
using namespace std;


#define debug(var) show(var, #var)
#define LL long long
#define VI vector <int>
#define VLL vector <LL>
#define VII vector < vector <int> >
#define VVI vector < vector <int> >
#define PII pair <int, int>
#define SI set <int>
#define PQ(x) priority_queue <x>
#define mt make_trip
#define mp make_pair
#define sd second
#define ft first
#define pb push_back
#define ins insert 

void show (VVI v, string nm){
  cerr<<">>> "<<nm<<" : ";
  cout<<"\n";
  for (int i=0;i<v.size();++i){
    for (int j=0;j<v[i].size();++j)cout<<v[i][j]<<" ";
    cerr<<"\n";
  }
}

void show (int n, string nm){
  cerr<<">>> "<<nm<<" : "<<n;
  cout<<"\n";
}

void show (VI v, string nm){
  cerr<<">>> "<<nm<<" : ";
  cout<<"\n";
  for (int i=0;i<v.size();++i)
    cout<<v[i]<<" ";
  cerr<<"\n";
}


struct PIII {
  int x, y, z;
};
PIII make_trip (int x, int y, int z){
  PIII new_; 
  new_.x = x;
  new_.y = y;
  new_.z = z;

  return new_;
}
bool compfirstPIII (PIII a, PIII b){
  if ( a.x < b.x) return true;
  else if ((a.x == b.x) && (a.y < b.y)) return true;
  else if ((a.x == b.x) && (a.y == b.y) && (a.z < b.z))return true;
  else return false;
}
bool compsecondPIII (PIII a, PIII b){
  if ( a.y < b.y) return true;
  else if ((a.y == b.y) && (a.z < b.z))return true;
  else return false;
}
bool compthirdPIII (PIII a, PIII b){
  return a.z < b.z;
}
bool compfirstPII (PII a, PII b){
  if ( a.ft < b.ft) return true;
  else if ((a.ft == b.ft) && (a.sd < b.sd)) return true;
  else return false;
}
bool compsecondPII (PII a, PII b){
  return a.sd < b.sd;
}

int pow (int a, int b){
  LL ans = 1;
  LL cur = a;
  while (b>0){
    if (b%2 == 1)ans = ans * cur;
    cur = cur * cur;
    b/=2;
  }
  return ans;
}
int modpow (int a, int b, int mod){
  LL ans = 1;
  LL cur = a;
  while (b>0){
    if (b%2 == 1)ans = (ans * cur) % mod;
    cur = (cur * cur) % mod;
    b/=2;
  }
  return ans;
}
///////////////////////////

int main (){
  int t;
  cin>>t;
  for (int te=1;te<=t;++te){
    cout<<"Case #"<<te<<": ";
    VI big ;
    VI small ;
    int n, c;
    cin>>n>>c;
    for (int i=0;i<n;++i){
      int x;cin>>x;
      if (x>(c/2))big.pb(x);
      else small.pb(x);
    }

    sort (small.begin(), small.end() );
    sort (big.begin(), big.end() );
    int ans = 0;
    int cs = 0;
    int cb = big.size() - 1;
    while (cb >= 0 && cs<small.size()){
      if (small[cs] + big[cb] <= c)cs++;
      cb--;
      ans ++;
    }
    ans += (((small.size() - cs) + 1)/2);
    ans += cb+1;
    cout<<ans<<"\n";
  }
}
