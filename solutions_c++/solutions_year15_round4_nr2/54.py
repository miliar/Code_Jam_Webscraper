/* Opgave: B */
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
#include <cstdint>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>

#include <iostream>
#include <sstream>
#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm>

// lp_solve 5.5, open source available at http://lpsolve.sourceforge.net
#include <lpsolve/lp_lib.h>
using namespace std;

void log(lprec *, void *, char *) {
}
double N, V, X;
double R[100], C[100];
void doit(int testcase) {
  cin >> N >> V >> X;
  for(int i = 0; i < N; ++i)
    cin >> R[i] >> C[i];
  double smallest = INFINITY;
  double largest = -INFINITY;
  for(int i = 0; i < N; ++i) {
    smallest = std::min(smallest, C[i]);
    largest = std::max(largest, C[i]);
  }
  // acc issues
  if(smallest == X || largest == X) {
    double r = 0;
    for(int i = 0; i < N; ++i)
      if(C[i] == X)
        r += R[i];
    cout << "Case #" << testcase << ": " << (V/r) << "\n";
    return;
  }
  
  auto lp = make_lp(0, N + 1);
  set_add_rowmode(lp, TRUE);
  
  {
    int cols[100];
    REAL vals1[100];
    REAL vals2[100];
    for(int i = 0; i < N; ++i) {
      cols[i] = 2 + i;
      vals1[i] = 1.0;
      vals2[i] = C[i];
    }
    add_constraintex(lp, N, vals1, cols, EQ, V);
    add_constraintex(lp, N, vals2, cols, EQ, V * X);
  }
  
  for(int i = 0; i < N; ++i) {
    int cols[] = {1, 2 + i};
    REAL vals[] = {R[i], -1.0};
    add_constraintex(lp, 2, vals, cols, GE, 0.0);
  }
  set_add_rowmode(lp, FALSE);
  
  {
    int objCols[] = {1};
    REAL objVals[] = {1.0};
    set_obj_fnex(lp, 1, objVals, objCols);
  }
  set_minim(lp);
  set_verbose(lp, IMPORTANT);
  //write_LP(lp, stdout);
  
  cout << "Case #" << testcase << ": ";
  
  auto ret = solve(lp);

  //bool poss = ret == OPTIMAL;
  /*
  if((poss && (largest < X || smallest > X)) || (!poss && (largest >= X && smallest <= X))) {
    std::cout << "abort in case " << testcase << "\n";
    cout << N << " " << V << " " << X << "(" << poss << " " << ret << " " << largest << " " << smallest << ")\n";
    for(int i = 0; i < N; ++i) {
      cout << " " << R[i] << " " << C[i] << "\n";
    }
    
    vector<double> r(N + 2);
    get_variables(lp, r.data());
    for(int i = 0; i < N + 2; ++i)
      cout << " " << i << " " << r[i] << "\n";
    std::abort();
  }*/
  if(ret == OPTIMAL && ( X >= smallest && X <= largest)) {
    cout << get_objective(lp);
  } else
    cout << "IMPOSSIBLE";
  
  cout << "\n";
  delete_lp(lp);
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(10);
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i)
    doit(i);
  return 0;
}
/* Opgave: B */
