#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>

#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <string>

#include <iostream>
#include <sstream>
#include <utility>
#include <functional>
#include <limits>
#include <numeric>
#include <algorithm>

using namespace std;

int N, X;
int S[10000];

int num[10001][10001];
void doit (int casenum) {
  cin >> N >> X;
  for(int i = 0; i < N; ++i)
    cin >> S[i];
  std::sort(S, S + N);
  for(int l = 0; l <= N; ++l) {
    for(int i = 0; i + l <= N; ++i) {
      if(l <= 1)
        num[l][i] = l;
      else {
        if(S[i] + S[i+l-1] <= X)
          num[l][i] = num[l-2][i+1] + 1;
        else
          num[l][i] = std::min(num[l-1][i], num[l-1][i+1]) + 1;
      }
    }
  }
  std::cout << "Case #" << casenum << ": " << num[N][0] << "\n";
}

int main () {
  int t;
  cin >> t;
  for(int i = 1; i <= t; ++i)
    doit(i);
  return 0;
}