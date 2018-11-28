#include <stdio.h>
#include <algorithm>

using namespace std;

void print_array(double* arr, int n)
{
  for (int i = 0; i < n; i++) {
    printf("%f ", arr[i]);
  }
  printf("\n");
}

int main()
{
  int T;

  freopen("D-large.in", "r", stdin);
  freopen("D-large.out", "w", stdout);

  scanf("%d", &T);

  double naomi[1000], ken[1000];

  for (int cn = 1; cn <= T; cn++) {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
      scanf("%lf", &naomi[i]);
    }
    for (int i = 0; i < n; i++) {
      scanf("%lf", &ken[i]);
    }
    sort(naomi, naomi + n);
    sort(ken, ken + n);

    //print_array(naomi, n);
    //print_array(ken, n);

    int ans1 = 0;
    int l = 0, r = n - 1;
    for (int i = 0; i < n; i++) {
      if (naomi[i] < ken[l]) {
        r--;
      } else {
        l++;
        ans1++;
      }
    }
    int ans2 = 0;
    int j = 0;
    for (int i = 0; i < n; i++) {
      while (j < n && ken[j] < naomi[i]) {
        j++;
      }
      if (j >= n) {
        ans2 = n - i;
        break;
      }
      j++;

    }
    printf("Case #%d: %d %d\n", cn, ans1, ans2);
  }
  return 0;
}