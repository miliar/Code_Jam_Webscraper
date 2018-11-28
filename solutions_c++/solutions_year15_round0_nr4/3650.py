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
    freopen("4.in", "r", stdin);
  assert( fin!=NULL );
  DEBUG = (argc>=3) ? atoi(argv[2]) : 0;
  if(!DEBUG) freopen("4.out", "w", stdout);

  int T;
  cin >> T;
  for(int ii = 0; ii < T; ii++){
    int X, R, C;
    cin >> X >> R >> C;
    cout << "Case #" << ii + 1 << ": ";
    int ans=0;
    if ((R*C)%X!=0) {
      ans=0;
    } else {
      if (X==1) {
	ans=1;
      } else if (X==2) {
	ans=1;
      } else if (X==3) {
	if (R!=1 && C!=1) {
	  ans=1;
	}
      } else if (X==4) {
	if (R==4 && C==3) ans=1;
	if (R==4 && C==4) ans=1;
	if (R==3 && C==4) ans=1;
      }
    }
    if (ans==1) cout << "GABRIEL\n";
    else cout << "RICHARD\n";
  }
  exit(0);
}

// g++ -g 4.cpp; ./a.out 4.in 4

// cat ../../4.cpp | sed 's/4/newtask/g' > tmp.cpp



