#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define INF 0x3f3f3f3f
typedef long long int int64;

double c, f, x;

int main() {
  int t;
  scanf("%d", &t);
  REP(k, t) {
    scanf("%lf %lf %lf", &c, &f, &x);
    double res = 1e100;
    int y = 0;
    while (1) {
      if (x*f <= 2*c + (y+1)*f*c) {
        break;
      }
      y++;
    }
    res = x/(2.0+y*f);
    REP(i, y) {
      res += c / (2.0+i*f);
    } 
    printf("Case #%d: %.10lf\n", k+1, res);
  }
	return 0;
}