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

#define MAXN 10010

int A[MAXN];

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    int N, X; cin >> N >> X;
    for(int i = 0; i < N; i++) {
      cin >> A[i];
    }
    sort(A, A + N);

    int i = 0;
    int j = N - 1;
    int result = 0;
    while(i < j) {
      if(A[i] + A[j] <= X) {
        i++;
        j--;
        result++;
      } else {
        result++;
        j--;
      }
    }
    if(i == j) {
      result++;
    }

    printf("Case #%d: %d\n", t, result);
  }
  return 0;
}
