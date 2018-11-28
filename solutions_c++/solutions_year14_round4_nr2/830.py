#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <set>

using namespace std;

#define MAXN 1024

int N;
pair<int, int> A[MAXN];

int DP[2][MAXN];

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    cin >> N;
    for(int i = 0; i < N; i++) {
      cin >> A[i].first;
      A[i].second = i;
    }
    sort(A, A + N);

    int result = 0;
    for(int i = N - 2; i >= 0; i--) {
      int pos = 0;
      for(int j = i + 1; j < N; j++) {
        if(A[j].second < A[i].second) {
          pos++;
        }
      }
      result += min(pos, N - i - 1 - pos);
    }

    printf("Case #%d: %d\n", t, result);
  }
  return 0;
}
