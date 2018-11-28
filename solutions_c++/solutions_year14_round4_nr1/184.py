
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <complex>
#include <numeric>
using namespace std;
typedef long long ll;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,s) for(__typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)

unsigned myrand() {
  static unsigned x = 123456789, y = 362436069, z = 521288629, w = 88675123;
  unsigned t = (x ^ (x << 11)); x = y; y = z; z = w;
  return (w = (w ^ (w >> 19)) ^ (t ^ (t >> 8)));
}

int vs[10000+10];
bool used[10000+10];


int main(void) {
  int nCase;
  cin >> nCase;
  REP(iCase, nCase) {
    int n;
    int cap;
    cin >> n >> cap;
    map<int,int> ss;
    REP(i, n){
      cin >> vs[i];
      ss[vs[i]]++;
    }
    
    int res = 0;
    while(!ss.empty()){
//       cerr << ">" << ss.size() << endl;
      map<int,int>::reverse_iterator rit = ss.rbegin();
      res++;
      assert(rit->second > 0);
      rit->second--;
      int big = rit->first;
      if(rit->second == 0){
	++rit;
	ss.erase(rit.base());
      }
      
      int rest = cap - big;
      map<int,int>::iterator it = ss.upper_bound(rest);
      if(it == ss.begin())
	continue;
      --it;
      assert(it->first <= rest);
      it->second--;
      if(it->second == 0)
	ss.erase(it);
    }
    
    printf("Case #%d: %d\n", iCase+1, res);
  }
  return 0;
}
