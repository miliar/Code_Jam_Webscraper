#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define INF 0x3f3f3f3f
typedef long long int int64;

int x, y;
int v[2][5][5];

int main() {
  int t;
  scanf("%d", &t);
  REP(k, t) {
    scanf("%d", &x);
    REP(i, 4) {
      REP(j, 4) {
        scanf("%d", &v[0][i][j]);
      }
    }
    scanf("%d", &y);
    REP(i, 4) {
      REP(j, 4) {
        scanf("%d", &v[1][i][j]);
      }
    }
    int res = 0;
    int num;
    x--; y--;
    for (int i = 1; i <= 16; i++) {
      int a = 0;
      REP(j, 4) {
        if (v[0][x][j] == i) a++;
        if (v[1][y][j] == i) a++;
      }
      if (a == 2) {
        res++;
        num = i;
      }
    }
    printf("Case #%d: ", k+1);
    if (res == 0) {
      printf("Volunteer cheated!\n");
    }
    else if (res > 1) {
      printf("Bad magician!\n");
    }
    else {
      printf("%d\n", num);
    }
  }
  return 0;	
}