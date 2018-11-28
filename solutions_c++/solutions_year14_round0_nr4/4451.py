#include <stdio.h>
#include <algorithm>
#include <set>
using namespace std;
#define MAXN 1100

int n;
double a[MAXN], b[MAXN];
int used[MAXN];

int main () {
  int teste;
  scanf ("%d", &teste);
  for (int t = 0; t < teste; t++) {
    scanf ("%d", &n);
    for (int i = 0; i < n; i++) 
      scanf ("%lf", &a[i]);
    for (int i = 0; i < n; i++) 
      scanf ("%lf", &b[i]);
    sort (a, a + n);
    sort (b, b + n);
    int ret1 = 0;
    for (int k = 1; k <= n; k++) {
      int flag = 1;
      for (int i = 0; i < k; i++) 
	if (b[i] > a[n - k + i])
	  flag = 0;
      if (flag) 
	ret1 = k;
    }
    for (int i = 0; i < n; i++) 
      used[i] = 0;
    int ret2 = 0;
    for (int i = 0; i < n; i++) {
      int use = -1;
      for (int j = 0; j < n; j++) {
	if (used[j] || b[j] < a[i])
	  continue;
	if (use == -1 || b[use] > b[j])
	  use = j;
      }
      if (use != -1) {
	used[use] = 1;
      }
      else {
	for (int j = 0; j < n; j++) 
	  if (used[j] == 0) {
	    used[j] = 1;
	    break;
	  }
	ret2++;
      }
    }
    printf ("Case #%d: %d %d\n", t + 1, ret1, ret2);
  }
  return 0;
}
