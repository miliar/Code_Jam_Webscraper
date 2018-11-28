
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
  std::string s;
  std::cin >> s;
  char prev = s[0];
  int diff = 0;
  for (char c : s) {
    if (prev != c) {
      ++diff;
      prev = c;
    }
  }
  if (prev != '+') {
    ++diff;
  }
  printf(" %d\n", diff);
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
