
#include <algorithm>
#include <cstdio>
using namespace std;

int a[1000], n;

int l[1001], r[1001];

int main(){
  int Z;
  scanf("%d",&Z);
  for (int z=1;z<=Z;++z) {
    scanf("%d",&n);
    for (int i=0;i<n;++i)
      scanf("%d",&a[i]);
    int res = 0;
    int left = 0, right = n;
    while (left < right) {
      int best = left;
      for (int i=left;i<right;++i)
        if (a[i] < a[best]) best=i;
      if (best - left < right - 1 - best) {
        res += best - left;
        for (int i=best; i>left; --i)
          a[i] = a[i-1];
        left++;
      } else {
        res += right - 1 - best;
        for (int i=best; i<right-1; ++i)
          a[i] = a[i+1];
        right--;
      }
    }
   printf("Case #%d: %d\n", z,res);
  }
}

