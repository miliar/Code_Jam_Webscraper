#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <climits>

#define INF (INT_MAX/2)

typedef long long lint;

using namespace std;

int main() {
  int ntest;

  scanf("%d", &ntest);

  for (int t = 0; t < ntest; t++) {
    int n, cap;
    vector<int> sizes;

    scanf("%d %d", &n, &cap);

    for (int i = 0; i < n; i++) {
      int size;
      scanf("%d", &size);
      sizes.push_back(size);
    }

    sort(sizes.begin(), sizes.end());

    int result = 0;

    for (int j = n-1; j >= 0; j--) {
      if (sizes[j] == -1) continue;
      int i = -1;

      for (int k = 0; k < j; k++)
	if (sizes[k] != -1 && sizes[k] + sizes[j] <= cap)
	  i = k;

      if (i != -1) sizes[i] = -1;
      sizes[j] = -1;
      result ++;
    }

    printf("Case #%d: %d\n", t+1, result);
  }

  return 0;
}
