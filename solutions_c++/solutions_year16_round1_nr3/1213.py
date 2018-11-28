#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <string.h>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <sstream>
using namespace std;

int pc(int x) { return !x?0:(x&1)+pc(x>>1); }
int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  getchar();
  for (int rr = 1; rr <= nocases; ++rr) {
    int n, x;
    cin >> n;
    vector<int> f;
    for (int i = 0; i < n; ++i) {
      cin >> x;
      --x;
      f.push_back(x);
    }
    int best = 0;
    for (int m = 1; m < 1<<n; ++m) {
      int p = pc(m);
      if (p < 2) continue;
      if (p < best) continue;
      vector<int> v;
      for (int j = 0; j < n; ++j)
	if (m & (1<<j))
	  v.push_back(j);
      assert(v.size() == p);
      do { 
	bool good = true;
	for (int i = 0; i < v.size(); ++i)
	  if ((v[(i+1)%p] != f[v[i]]) && (v[(i-1+p)%p] != f[v[i]])) {
	    good = false;
	    break;
	  }
	if (good) {
	  best = max(best, p);
	  break;
	}
      } while(next_permutation(v.begin()+1, v.end()));
    }
    printf("Case #%d: %d\n", rr, best);
  }
  return 0;
}
