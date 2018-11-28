#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include <sstream>
#include <set>
#include <queue>
#include <cstdlib>
#include <cmath>

using namespace std;

void doit() {
  int n,d;
  scanf("%d %d",&n,&d);
  multiset<int> a;
  for(int i=0;i<n;i++) {
    int x;
    scanf("%d",&x);
    a.insert(x);
  }
  int ret=0;
  while(!a.empty()) {
    ret++;
    int biggest = *--a.end();
    int best_match = d-biggest;
    multiset<int>::iterator match = a.upper_bound(best_match);
    // match is the first thing that doesn't work.
    if (match == a.begin()) {
      // nothing works.
      a.erase(--a.end());
    } else {
      match--;
      if (*match == biggest) {
        if (match != a.begin()) {
          match--;
          a.erase(--a.end());
          a.erase(match);
        } else {
          a.erase(--a.end());
        }
      } else {
          a.erase(--a.end());
          a.erase(match);
      }
    }
  }
  printf("%d\n",ret);
}

int main() {
  int n;
  scanf("%d",&n);
  for(int i=0;i<n;i++) {
    printf("Case #%d: ",i+1);
    doit();
  }
  return 0;
}
