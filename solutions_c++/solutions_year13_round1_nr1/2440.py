#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <complex>
#include <algorithm>
using namespace std;

const int BUFFER_SIZE = 1 * 1024;
const double EPS      = 10e-6;
const int MAX         = 100;
const int INF         = 1 << 30;

double pi = M_PI;

char buffer[BUFFER_SIZE];

char* read_line() 
{
  int ch, size = 0;
  while ((ch = getchar()) != '\n') buffer[size++] = ch;
  buffer[size] = '\0';
  return buffer;
}


int main(int argc, char *argv[])
{
  int T, tc, ans;
  long long r, t;

  scanf("%d", &T);

  for (tc = 1; tc <= T; tc++) {
    scanf("%lld %lld", &r, &t);
    ans = 0;

    while (t > 0) {
      t -= ((r + 1) * (r + 1)) - (r * r);
      r += 2;
      if (t >= 0)
        ans++;
    }

    printf("Case #%d: %d\n", tc, ans);
  }
  return 0;
}
