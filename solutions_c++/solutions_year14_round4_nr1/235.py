#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 10000;
int a[MAXN];
int n, X;

int main() {
  int totCas;
  scanf("%d", &totCas);
  for (int cas = 1; cas <= totCas; cas++) {
    scanf("%d%d", &n, &X);
    for (int i = 0; i < n; i++) {
      scanf("%d", &a[i]);
    }
    sort(a, a + n);
    int ans = 0;
    int used = 0;
    for (int i = n - 1; i >= used; i--) {
      if (a[used] + a[i] > X) {
        ans++;
      } else {
        int pos = upper_bound(a + used, a + i, X - a[i]) - a;
        swap(a[pos - 1], a[used]);
        used++;
        ans++;
      }
    }
    printf("Case #%d: %d\n", cas, ans);
  }
	return 0;
}

