#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAX_N = 100 + 5;
const int MAX_SIZE = 1000000 + 5;

int A;
int N;
int size[MAX_N];

int dp[MAX_SIZE][MAX_N];
int rec(int curSize, int pos) {
  if (curSize == 1) {
    return N;
  }
  if (pos == N) {
    return 0;
  }
  if (curSize > size[N - 1]) {
    curSize = size[N - 1] + 1;
  }
  int& ret = dp[curSize][pos];
  if (ret != -1) {
    return ret;
  }
  ret = INT_MAX;
  if (size[pos] < curSize) {
    ret = rec(curSize + size[pos], pos + 1);
  }
  ret = min(ret, rec(curSize, pos + 1) + 1);
  if (curSize <= size[N - 1]) {
    ret = min(ret, rec(curSize * 2 - 1, pos) + 1);
  }
  return ret;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    scanf("%d %d", &A, &N);
    for (int i = 0; i < N; ++i) {
      scanf("%d", size + i);
    }
    sort(size, size + N);
    memset(dp, -1, sizeof(dp));
    printf("Case #%d: %d\n", t + 1, rec(A, 0));
  }
}
