#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

typedef  __int128 Int;
const Int MOD = 1000002013;
long n,m;
Int calc(Int dist){
  return ((Int)n + (Int)n - dist + 1) * dist / 2;
}
#define minus ifjdsoajfoajfoda
long l[1000],r[1000],p[1000];
unordered_map<long, Int> add;
unordered_map<long, Int> minus;
vector<long> ds;
typedef pair<Int,Int> P;

int main(){
  int T;
  cin>>T;
  for(int tc=1;tc<=T;tc++){
    cout << "Case #" << tc << ": ";
    ds.clear();
    add.clear();
    minus.clear();
    cin>>n>>m;
    Int nor = 0, min = 0;
    for(int i=0;i<m;i++){
      cin>>l[i]>>r[i]>>p[i];
      nor += (Int)p[i] * calc(r[i] - l[i]);
      add[l[i]] += p[i];
      minus[r[i]] += p[i];
      ds.push_back(l[i]);
      ds.push_back(r[i]);
    }
    sort(ds.begin(),ds.end());
    ds.erase(unique(ds.begin(),ds.end()),ds.end());
    vector<P> now;
    for(int i=0;i<ds.size();i++){
      long d = ds[i];
      if(add[d] > 0){
        now.emplace_back(d,add[d]);
      }
      while(minus[d] > 0){
        Int mm = std::min(minus[d], now.back().second);
        minus[d] -= mm;
        min += mm * calc(d - now.back().first);
        now.back().second -= mm;
        if(now.back().second == 0){
          now.pop_back();
        }
      }
    }
    cout << (long)((nor-min)%MOD) << endl;
  }
}
