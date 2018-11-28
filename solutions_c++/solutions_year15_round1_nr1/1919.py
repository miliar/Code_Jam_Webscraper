#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {
  int t, n, m[10003], i, x, y, c, aux;

  scanf("%d", &t);
  c = 1;
  while (t--) {
    scanf("%d", &n);
    x = y = 0;
    for (i = 0; i < n; i++) {
      scanf("%d", &m[i]);
    }
    aux = 0;
    for (i = 0; i < n - 1; i++) {
      if (m[i] - m[i + 1] > 0) {
	x += (m[i] - m[i + 1]);
	if ((m[i] - m[i + 1]) > aux) {
	  aux = m[i] - m[i + 1];
	}
      }
    }
    for (i = 0; i < n - 1; i++) {
      if (m[i] >= aux) {
	y += aux;
      } else {
	y += m[i];
      }
    }
    printf("Case #%d: %d %d\n", c, x, y);
    c++;
  }
  return 0;
}
