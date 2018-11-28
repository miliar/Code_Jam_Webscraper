
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
#include <fstream>
#include <thread>
#include <assert.h>
#include <sys/mman.h>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <array>
#include <sstream>
#include <set>
#include <map>
#include <list>
#include <time.h>
#include <iomanip>
#include <forward_list>

using namespace std;


unsigned find_val(unsigned n) {
  if (n == 0) {
    return 0;
  }
  bool u[10] = {false};
  unsigned x = n;
  while (true) {
    unsigned k = x;
    while (k) {
      unsigned d = k % 10;
      u[d] = true;
      k = k / 10;
    }
    bool has_false = false;
    for (int i = 0; i < 10; ++i) {
      if (!u[i]) {
        has_false = true;
        break;
      }
    }
    if (!has_false) {
      return x;
    }
    x += n;
  }
}

void solve(int casenum) {
  printf("Case #%d:", casenum);
  unsigned n = 0;
  std::cin >> n;
  unsigned res = find_val(n);
  if (res == 0) {
    printf(" INSOMNIA\n");
  } else {
    printf(" %u\n", res);
  }
}

int main(int argc, const char * argv[]) {
  freopen("file.txt","r",stdin);
  freopen("file.out","w",stdout);

  int t = 0;
  scanf("%d\n", &t);

  for (int i = 1; i <= t; ++i) {
    solve(i);
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
