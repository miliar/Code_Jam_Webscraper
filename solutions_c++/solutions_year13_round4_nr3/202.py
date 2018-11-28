#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int N, A[32], B[32];

bool done;
int used, X[32];

void attempt()
{
  int rev = 0;
  for (int i = N - 1; i >= 0; --i) {
    int b = 1;
    for (int j = i + 1; j < N; ++j)
      if (X[j] < X[i])
        b = max(b, B[j] + 1);
    if (b != B[i])
      return;
    rev |= 1 << X[i];
  }
  for (int i = 0; i < N; ++i)
    cout << ' ' << X[i] + 1;
  cout << endl;
  done = true;
}

void dfs(int depth)
{
  if (done)
    return;

  if (depth == N) {
    attempt();
    return;
  }

  for (int i = 0; i < N; ++i) {
    if (~used >> i & 1) {
      int a = 1;
      for (int j = 0; j < depth; ++j)
        if (X[j] < i)
          a = max(a, A[j] + 1);
      if (a == A[depth]) {
        used ^= 1 << i;
        X[depth] = i;
        dfs(depth + 1);
        used ^= 1 << i;
      }
    }
  }
}

int main()
{
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> N;
    for (int i = 0; i < N; ++i)
      cin >> A[i];
    for (int i = 0; i < N; ++i)
      cin >> B[i];

    cout << "Case #" << t << ':';

    done = false;
    used = 0;
    dfs(0);
  }

  return 0;
}
