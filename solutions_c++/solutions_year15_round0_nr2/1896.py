#include <iostream>
#include <map>
#include <set>
#include <functional>
#include <vector>

using namespace std;

typedef struct {
  int p;
  int c;
  int r;
} Data;

typedef multimap<int, Data, greater<int> > S;

int main(void){
  int t;
  cin >> t;
  for(int k = 0; k < t; ++k){
    int n, p;
    cin >> n;
    S ps;
    for(int i = 0; i < n; ++i){
      cin >> p;
      if(ps.find(p) == ps.end()) {
        ps.insert(make_pair(p, Data()));
        S::iterator iter = ps.find(p);
        iter->second.p = p;
        iter->second.c = 0;
        iter->second.r = 1;
      }
      S::iterator iter = ps.find(p);
      ++iter->second.c;
    }
    int res = ps.begin()->first;
    int add = 0;
    while(!ps.empty()) {
      Data d = ps.begin()->second;
      ps.erase(ps.begin());
      d.r++;
      add += d.c;
      if(d.r <= d.p) {
        ps.insert(make_pair(d.p/d.r + (d.p%d.r != 0), d));
      }

      res = min(res, add + ps.begin()->first);
    }
    cout << "Case #" << k+1 << ": "<< res << endl;
  }

  return 0;
}
