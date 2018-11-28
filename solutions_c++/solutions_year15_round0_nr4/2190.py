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

string FILENAME = "D-small-attempt1";


vector<int> read(string s){
  vector<int> ret;
  int n;
  istringstream sin(s);
  while(sin>>n)
    ret.push_back(n);
  return ret;
}

int main () {
  setvbuf(stdout, NULL, _IONBF, 0);
  freopen((FILENAME + ".in").c_str(), "r", stdin);
  freopen((FILENAME + ".out").c_str(), "w", stdout);
  int testcases;
  scanf("%d", &testcases);
  for (int case_id = 1; case_id <= testcases; case_id++) {
    printf("Case #%d: ", case_id);
    int x, r, c;
    scanf("%d %d %d", &x, &r, &c);
    if (c > r) {
      swap(r, c);
    }
    if (x >= 7) {
      printf("RICHARD\n");
    } else {
      if (x == 1) {
        printf("GABRIEL\n");
      } else if (x == 2) {
        if ((r * c) % 2 == 0) {
          printf("GABRIEL\n");
        } else {
          printf("RICHARD\n");
        }
      } else if (x == 3) {
        if ((r == 3 && c == 2) || (r == 3 && c == 3) || (r == 4 && c == 3)) {
          printf("GABRIEL\n");
        } else {
          printf("RICHARD\n");
        }
      } else if (x == 4) {
        if (r == 4 && c == 4 || r == 4 && c == 3) {
          printf("GABRIEL\n");
        } else {
          printf("RICHARD\n");
        }
      }
    }
  }
  fflush(stdout);
}
