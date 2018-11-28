#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {

  int tests;
  scanf(" %d", &tests);

  for(int test = 0; test < tests; test++) {
    
    int r, t;
    scanf(" %d %d", &r, &t);

    int d, c = 0;
    while(t >= (d = (2 * r) + 1)) {
      t -= d;
      c++;
      r += 2;
    }

    printf("Case #%d: %d\n", test + 1, c);
  }

  return 0;
}
