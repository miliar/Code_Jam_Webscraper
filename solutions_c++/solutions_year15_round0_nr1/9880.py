#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#include <iostream>
#include <string.h>
#include <deque>
#include <set>
#include <queue>
#include <complex>
#include <deque>
#include <map>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;
#define LL int64_t

int DEBUG = 0;
#define MAXM 50

main(int argc, char **argv) {
  FILE *fin = (argc>=2) ? freopen(argv[1], "r", stdin) :
    freopen("1.in", "r", stdin);
  assert( fin!=NULL );
  DEBUG = (argc>=3) ? atoi(argv[2]) : 0;
  if(!DEBUG) freopen("1.out", "w", stdout);

  int T;
  cin >> T;
  for(int ii = 0; ii < T; ii++){
    int S;
    cin >> S;
    char bad[S+5];
    cin >> bad;
    int cur=0;
    int ans=0;
    for (int i=0; i<=S; i++) {
      int x=bad[i]-'0';
      if (cur<i) {
	ans+=(i-cur);
	cur=i+x;
      } else {
	cur+=x;
      }
    }
    cout << "Case #" << ii + 1 << ": ";
    cout << ans << endl;
  }
  exit(0);
}

// g++ -g 1.cpp; ./a.out 1.in 1

// cat ../../1.cpp | sed 's/1/newtask/g' > tmp.cpp



