
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

void printv(const std::vector<int>& v) {
  for (int i : v) {
    printf(" %d", i);
  }
  printf("\n");
}

void solve(int casenum) {
  printf("Case #%d:", casenum);
  int k = 0;
  int c = 0;
  int s = 0;
  std::cin >> k;
  std::cin >> c;
  std::cin >> s;
  if (c == 1) {
    if (s < k) {
      printf(" IMPOSSIBLE\n");
    } else {
      for (int i = 1; i <= s; ++i) {
        printf(" %d", i);
      }
      printf("\n");
    }
    return;
  }
  int pos = 2;
  int block = 0;
  vector<int> poses;
  while (s > 0) {
    pos = min(k, pos);
    block = min(k, block);
    poses.push_back(block * k + pos);
    if (pos == k) {
      printv(poses);
      return;
    }
    block += 2;
    pos += 2;
    --s;
  }
  printf(" IMPOSSIBLE\n");
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
