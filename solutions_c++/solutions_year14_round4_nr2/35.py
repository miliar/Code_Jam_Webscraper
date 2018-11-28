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
    int n;

    scanf("%d", &n);

    vector<int> A;
    vector<pair <int, int> > B;

    for (int i = 0; i < n; i++) {
      int val;
      scanf("%d", &val);
      A.push_back(val);
      B.push_back(make_pair(val, i));
    }
    sort(B.begin(), B.end());

    int result = 0;

    for (int i = 0; i < n; i++) {
      int val = B[i].first;
      int pos = B[i].second;
      
      int toleft = 0, toright = 0;

      for (int j = 0; j < pos; j++)
	if (A[j] > val)
	  toleft++;
      for (int j = pos+1; j < n; j++)
	if (A[j] > val)
	  toright++;
      
      result += min(toleft, toright);
    }

    printf("Case #%d: %d\n", t+1, result);
  }

  return 0;
}
