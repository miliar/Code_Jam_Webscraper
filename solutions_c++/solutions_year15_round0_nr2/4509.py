#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
using namespace std;

int eat(vector<int> &P)
{
  int ret = 0;
  int maxx = 0;
  
  for (int i = P.size() - 1; i >= 0; --i) {
    if (P[i]) {
      maxx = i;
      break;
    }
  }
  
  if (maxx <= 2) return maxx;
  
  int old_maxx = P[maxx];
  ret = maxx;
  for (int i = 2; i <= maxx / 2; ++i) {
    P[maxx] = 0;
    P[maxx - i] += old_maxx;
    P[i] += old_maxx;
    
    ret = min(ret, eat(P) + old_maxx);
    P[i] -= old_maxx;
    P[maxx - i] -= old_maxx;
    P[maxx] = old_maxx;
  }
  
  //printf("%d,%d-%d\n", maxx, old_maxx, ret);
  return ret;
}

int main()
{
  int T;
  
  cin >> T;
  
  for (int t = 1; t <= T; ++t) {
    int D;
    
    cin >> D;
    
    vector<int> P(1001, 0);
    int x, maxx;
    maxx = 0;
    
    for (int i = 0; i < D; ++i) {
      cin >>x;
      P[x]++;
      maxx = max(maxx, x);
    }
    printf("Case #%d: %d\n", t, eat(P) );
  }
	
	return 0;
}
