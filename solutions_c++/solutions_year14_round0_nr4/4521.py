#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int cmp(const void *px, const void *py)
{
  double xx = *(double*) px, yy= *(double*) py;
  if (xx < yy) return -1;
  if (xx > yy) return 1;
  return 0;
}

int main() {
  freopen("d.in", "r",stdin);
  freopen("d.out", "w",stdout);
  int t;
  cin >> t;
  int caset = 0;
  while (caset < t) {
    caset ++;
    cout << "Case #" << caset << ": ";
    int n;
    cin >> n;
    double a[2005], b[2005];
    for (int i = 0; i < n; ++i)
      cin >> a[i];
    for (int j = 0; j < n; ++j)
      cin >> b[j];
    qsort(a, n, sizeof(double), cmp);
    qsort(b, n, sizeof(double), cmp);
    int pointx = 0;
    int pointy = 0;
    int ans1 = 0, ans2 = 0;
    while (pointx < n) {
      while (a[pointx] > b[pointy] && pointy < n) {
        pointy ++;
      }
      if (a[pointx] < b[pointy] && pointy < n)
        ans1 ++;
      pointx ++;
      pointy ++;
    }
    pointx = 0;
    pointy = 0;
    while (pointx < n) {
      while (b[pointx] > a[pointy] && pointy < n) {
        pointy ++;
      }
      if (b[pointx] < a[pointy] && pointy < n)
        ans2 ++;
      pointx++;
      pointy++;
    }
    cout << ans2 << " " << n -ans1 <<endl;
  }
  return 0;
}
