// https://code.google.com/codejam/contest/6224486/dashboard#s=p3

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
//#include <cmath>
#include <queue>
#include <climits>

using namespace std;

int D;
priority_queue<int> P;

void parse() {
  P = priority_queue<int>(); // reset
  scanf("%d", &D);
  for(int i = 0; i < D; i++) {
    int p;
    scanf("%d", &p);
    P.push(p);
  }
}

int brute(priority_queue<int> P, int add1, int add2, int acc, int mprec) {
  int m;
  if(acc > mprec) // cut
    return acc;
  if(add1 > 0)
    P.push(add1);
  if(add2 > 0)
    P.push(add2);
  if(P.empty())
    return acc;
  else {
    int p = P.top();
    P.pop();
    // no special turn
    m = acc + p; // min(acc + p, brute(P, -1, -1, acc));

    if(p > 3 && acc < min(mprec, m)) {
      // special turn
      for(int i = p/2; i >= 0; i--)
        m = min(m, brute(P, i, p-i, acc+1, min(m, mprec)));
    }
  }
  return m;
}

/*int solve() {
  int rep = 0;
  while(P.top() - 1 > 0) {
    if(P.top() > 3) { // divise
      cerr << "cut" << P.top() << endl;
      int p = P.top();
      P.pop();
      rep++; // special turn
      // en deux ?
      P.push(ceil(p/2.));
      P.push(floor(p/2.));
    }
    else
      return rep + P.top();
  }
  return rep + 1;
}*/

int main() {
  int T;
  scanf("%d", &T);
  for(int i = 0; i < T; i++) {
    parse();
    cout << "Case #" << i+1 << ": " << brute(P, -1, -1, 0, INT_MAX) << endl;
  }
  return 0;
}
