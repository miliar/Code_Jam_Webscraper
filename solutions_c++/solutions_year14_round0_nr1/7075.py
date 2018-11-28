#include <cstdio>
#include <algorithm>

using namespace std;

int t1[8];

void solve() {
  int x, y, XD, r;
  scanf("%d", &r);
  r--;
  for (y=0; y<4; y++)
    for (x=0; x<4; x++) {
      scanf("%d", &XD);
      if (y==r) t1[x]=XD;
    }
  scanf("%d", &r);
  r--;
  for (y=0; y<4; y++)
    for (x=4; x<8; x++) {
      scanf("%d", &XD);
      if (y==r) t1[x]=XD;
    }
  sort(t1, t1+8);
  int powt=0;
  for (x=1; x<8; x++)
    if (t1[x-1]==t1[x]) {
      powt++;
      y=t1[x];
    }
  switch (powt) {
    case 0:
      puts("Volunteer cheated!");
      break;
    case 1:
      printf("%d\n", y);
      break;
    default:
      puts("Bad magician!");
      break;
  }
}

int main() {
  int n;
  scanf("%d", &n);
  for (int i=1; i<=n; i++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}