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
    int N;
    cin >> N;
    double a[N], b[N];
    for (int i=0; i<N; i++) {
      scanf("%lf", &a[i]);
    }
    for (int i=0; i<N; i++) {
      scanf("%lf", &b[i]);
    }
    sort(a, a+N);
    sort(b, b+N);
    int dwar=0;
    for (int k=0; k<=N; k++) {
      bool wrk=true;
      for (int i=0; i<k; i++) {
	if (a[N-k+i]<b[i]) {
	  wrk=false;
	}
      }
      if (wrk) dwar=k;
    }
    int nwar=0;
    int e=N-1;
    int s=0;
    for (int i=N-1; i>=0; i--) {
      if (a[i]<b[e]) {
	e--;
      } else  {
	s++;
	nwar++;
      }
    }
    cout << "Case #" << ii + 1 << ": ";
    cout << dwar << " ";
    cout << nwar << endl;
  }
  exit(0);
}

// g++ -g 4.cpp; ./a.out 4.in 1

// cat ../../4.cpp | sed 's/4/newtask/g' > tmp.cpp



