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
    int a;
    cin >> a;
    int am[4][4];
    for (int i=0; i<4; i++) for (int j=0; j<4; j++) cin >> am[i][j];
    int b;
    cin >> b;
    int bm[4][4];
    for (int i=0; i<4; i++) for (int j=0; j<4; j++) cin >> bm[i][j];
    int k=0;
    int x=-1;
    for (int i=0; i<4; i++) {
      for (int j=0; j<4; j++) {
	if (am[a-1][i]==bm[b-1][j]) {
	  k++;
	  x=am[a-1][i];
	}
      }
    }
    cout << "Case #" << ii + 1 << ": ";
    if (k==0) {
      cout << "Volunteer cheated!" << endl;
    } else if (k==1) {
      cout << x << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
  exit(0);
}

// g++ -g 1.cpp; ./a.out 1.in 1

// cat ../../1.cpp | sed 's/1/newtask/g' > tmp.cpp



