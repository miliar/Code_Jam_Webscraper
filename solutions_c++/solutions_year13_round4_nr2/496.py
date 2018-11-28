#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <cstdlib>
#include <cstring>
//#include "ttmath/ttmath.h"

using namespace std;

int main() {
  long long p2[55];
  p2[0]=1;
  for (int i=1;i<53;i++) p2[i]=p2[i-1]*2;
  int T;
  cin >> T;
  for (int t=1;t<=T;t++) {
    int N;
    long long P;
    cin >> N >> P;
    long long y=0, Y=0;
    // 3 5
    for (int i=0;i<N;i++) {
      y+=p2[i]; // teams required to be better
      // position worse than this many teams:
      Y+=p2[N-1-i];
      //clog << y << " " << Y << endl;
      if (Y>=P) { // lost prize
	Y=y-1;
	break;
      }
    }
    long long z=0, Z=0;
    for (int i=0;i<N;i++) {
      z+=p2[i]; // teams required to be worse
      // position better than this many teams:
      Z+=p2[N-1-i];
      if (Z+P>=p2[N]) { // got a prize
	Z = p2[N]-1-z;
	break;
      }
    }
    if (P==p2[N]) Z=p2[N]-1;
    printf("Case #%d: %lld %lld\n", t, Y, Z);
  }
  return 0;
}


