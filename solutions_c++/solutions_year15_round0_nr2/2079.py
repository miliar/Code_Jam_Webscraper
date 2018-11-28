#include <stdio.h>
#include <algorithm>
#include <vector>
#include <assert.h>
using namespace std;
int value(const vector<int>& n, int k) {
  int sum = k;
  for (int i = 0; i < n.size(); i++) {
    sum += ((n[i]+(k-1))/k)-1;
  }
  return sum;
}
int main(int argc, char const *argv[])
{
  int t = 0;
  scanf("%d\n", &t);
  for (int ii = 0; ii < t; ii++) {
    int d;
    scanf("%d\n", &d);
    vector<int> p(d, 0);
    int maxp = 0, sum = 0;
    for (int i = 0; i < d; i++) {
      scanf("%d ", &p[i]);
      if (p[i] > maxp)
        maxp = p[i];
      sum += p[i];
    }
    if (maxp <= 2) {
      printf("Case #%d: %d\n", ii+1, maxp);
    } else {
      int ans = maxp;
      for (int i = 1; i < maxp; i++) {
        int val = value(p, i);
        if (val < ans)
          ans = val;
      }
      printf("Case #%d: %d\n", ii+1, ans);
    }    
  }
  return 0;
}