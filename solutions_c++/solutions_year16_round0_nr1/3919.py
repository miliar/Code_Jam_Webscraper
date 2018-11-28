#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void solve() {
  int N;
  cin >> N;
  if (N == 0) {
    cout << "INSOMNIA" << endl;
    return;
  }
  set<int> d;
  for (int i = 1; ; ++i) {
    for (int NN = N * i; NN; NN /= 10) {
      d.insert(NN % 10);
    }
    if (d.size() == 10) {
      cout << N * i << endl;
      return;
    } 
  }
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    printf("Case #%d: ", i + 1);
    solve();  
  }
  return 0;
}
