#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int getResult (vector<int> vals, int D, int maxElm) {
  int result = maxElm, accm, iter = 0;
  if (vals.size() == 0)
    return 0;

  for (iter = 1; iter <= maxElm; iter++) {
    accm = iter;
    for (int j = 0; j < D; j++) {
      if (vals[j] > iter) {
        accm += (vals[j] / iter) - ((vals[j] % iter) == 0);
      }
    }
    result = min(result, accm);
  }
  return result;
}

int main() {
  int tcase;
  scanf ("%d", &tcase);
  for (int i = 1; i <= tcase; i++) {
    int v, result = 0, D, maxElm = INT_MIN;
    scanf ("%d", &D);
    
    vector<int> arr;
    for (int k = 0 ; k < D; k ++) {
      scanf ("%d", &v);
      arr.push_back(v);
      if (maxElm < v)
        maxElm = v;
    }

    result = getResult (arr, D, maxElm);
    printf ("Case #%d: %d\n", i, result);
  }
  return 0;
}
