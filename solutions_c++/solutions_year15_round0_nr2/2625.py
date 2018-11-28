#include <functional>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;


int timeIsPossible(priority_queue<int> P, int t) {
  if (P.top() <= t) { 
    return true;
  } else {
    int top = P.top(); P.pop();
    int d = 2;
    // top = q*d + r
    int q = top / d;
    int r = top % d;
    while ((r == 0 && q + (d - 1) < top) || (r > 0 && q + 1 + (d - 1) < top)) {
      priority_queue<int, vector<int>, less<int>> newP(P);
      for (int i = 0; i < r; ++i) newP.push(q + 1);
      for (int i = r; i < d; ++i) newP.push(q); 
      if (timeIsPossible(newP, t - d + 1)) return true;
      ++d; q = top / d; r = top % d;
    }
  }
  return false;
}

int calculateTime(priority_queue<int> P) {
  int t = 9;
  while (timeIsPossible(P, t)) {
    --t;
  }
  return t + 1;
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int D; cin >> D;
    priority_queue<int, vector<int>, less<int>> P;
    for (int j = 0; j < D; ++j) {
      int p; cin >> p;
      P.push(p);
    }
    int t = calculateTime(P);
    cout << "Case #" << i+1 << ": " << t << endl;
  }
  return 0;
}
