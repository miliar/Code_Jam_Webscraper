#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1000;
int n;
int a[MAXN];

int solve(int l, int r) {
  if (l == r) {
    return 0;
  }
  int minPos = l;
  for (int i = l; i <= r; i++) {
    if (a[i] < a[minPos]) {
      minPos = i;
    }
  }
  if (minPos - l < r - minPos) {
    for (int i = minPos; i > l; i--) {
      swap(a[i], a[i - 1]);
    }
    return minPos - l + solve(l + 1, r);
  } else {
    for (int i = minPos; i < r; i++) {
      swap(a[i], a[i + 1]);
    }
    return r - minPos + solve(l, r - 1);
  }
}

int main() {
  int totCas;
  scanf("%d", &totCas);
  for (int cas = 1; cas <= totCas; cas++) {
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%d", &a[i]);
    }
    printf("Case #%d: %d\n", cas, solve(0, n - 1));
  }
	return 0;
}

