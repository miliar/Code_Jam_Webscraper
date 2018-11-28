#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <iterator>

#if DEBUG
#include "prettyprint.hpp"
#define print_container(c) cout << c << endl;
#endif

using namespace std;

bool flag = false;
string FILENAME = "B-small-attempt2";

vector<int> read(string s){
  vector<int> ret;
  int n;
  istringstream sin(s);
  while(sin>>n)
    ret.push_back(n);
  return ret;
}

int decrement(int i) {
  return i - 1;
}

map<vector<int>, int> memo;

int solve(vector<int> pancakes, int depth) {
  pancakes.erase(remove(pancakes.begin(), pancakes.end(), 0), pancakes.end());
  if (pancakes.size() == 0) {
    return 0;
  }
  if (depth >= 10) {
    return 100000;
  }
  sort(pancakes.begin(), pancakes.end(), std::greater<int>());

  int best = 1000000;
  for (int i = 2; i < pancakes[0]; i++) {
    vector<int> pancakes_copy(pancakes);
    pancakes_copy[0] -= i;
    pancakes_copy.push_back(i);
    best = min(best, 1 + solve(pancakes_copy, depth + 1));
  }
  vector<int> pancakes_copy(pancakes);
  for (int i = 0; i < pancakes.size(); i++) {
    pancakes_copy[i]--;
  }
  best = min(best, 1 + solve(pancakes_copy, depth + 1));
  memo[pancakes] = best;
  return best;
}

int main () {
  setvbuf(stdout, NULL, _IONBF, 0);
  freopen((FILENAME + ".in").c_str(), "r", stdin);
  freopen((FILENAME + ".out").c_str(), "w", stdout);
  int testcases;
  scanf("%d", &testcases);
  for (int case_id = 1; case_id <= testcases; case_id++) {
    printf("Case #%d: ", case_id);
    int d;
    scanf("%d", &d);
    vector<int> pancakes;
    for (int i = 0; i < d; i++) {
      int a;
      scanf("%d", &a);
      pancakes.push_back(a);
    }
    if (case_id == 87) {
      flag = true;
    }
    printf("%d\n", solve(pancakes, 0));
    flag = false;
  }
  fflush(stdout);
}
