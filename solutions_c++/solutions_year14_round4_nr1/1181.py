#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cctype>
#include <stack>
#include <complex>
using namespace std;

typedef long long int int64;

#define EPS 10e-9
#define INF 0x3f3f3f3f
#define REP(i,n) for(int i=0; i<(n); i++)

int n;
int c;
multiset<int> s;
multiset<int>::iterator it, it2;

int main()
{	
  int t;
  scanf("%d", &t);
  REP(ct, t) {
    scanf("%d %d", &n, &c);
    s.clear();
    REP(i, n) {
      int x;
      scanf("%d", &x);
      s.insert(x);
    }
    int res = 0;
    while (s.size() > 1) {
      it = s.begin();
      it2 = s.upper_bound(c - *it);
      if (it2 != s.begin()) {
        it2--;
      }
      if (it2 == s.begin()) {
        s.erase(it);
        res++;
      }
      else {
        s.erase(it2);
        s.erase(s.begin());
        res++;
      }
    }
    res += s.size();
    printf("Case #%d: %d\n", ct+1, res);
  }
	return 0;
}