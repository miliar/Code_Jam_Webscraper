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
    freopen("2.in", "r", stdin);
  assert( fin!=NULL );
  DEBUG = (argc>=3) ? atoi(argv[2]) : 0;
  if(!DEBUG) freopen("2.out", "w", stdout);

  int T;
  cin >> T;
  for(int ii = 0; ii < T; ii++){
    double C,F,X;
    scanf("%lf%lf%lf", &C, &F, &X);
    double rhs=(X*F/C)-2.0;
    int a=rhs/F;
    double k=a*(1.0);
    double time=0.0;
    if (k<0.0) k=0.0;
    for (int i=0; i<a; i++) {
      int iii=i+0.0;
      time=time+(C/(2.0+F*iii));
    }
    time=time+(X/(2.0+F*k));
    cout << "Case #" << ii + 1 << ": ";
    printf("%7f\n", time);
  }
  exit(0);
}

// g++ -g 2.cpp; ./a.out 2.in 1

// cat ../../2.cpp | sed 's/2/newtask/g' > tmp.cpp



