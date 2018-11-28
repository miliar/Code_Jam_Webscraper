#include <algorithm>
#include <cassert>
#include <cstdio>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#define ASSERT_ for (;;) {}
#define PII pair<int, int>

#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)
using namespace std;

int lawn[101][101];

int clear_columns[101];
int clear_rows[101];

void clear(){
  REP(i,101){
    clear_columns[i] = 0;
    clear_rows[i] = 0;
  }
}

bool solve(int n, int m) {
    bool retval = false;

    clear();

    REP(j,m){
      bool is_clear = true;
      REP(i,n) {
        if (lawn[i][j] == 2){
          is_clear = false;
          break;
        }
      }
      if (is_clear)
        clear_columns[j] = 1;
    }

    REP(i,n) {
      bool is_clear = true;
      REP(j,m) {
        if (lawn[i][j] == 2){
          is_clear = false;
          break;
        }
      }
      if (is_clear)
        clear_rows[i] = 1;
    }

    REP(i,n) {
      REP(j,m) {
        if (lawn[i][j] == 1 && !clear_rows[i] && !clear_columns[j]) {
          return false;
        } 
      }
    }
    return true;
}

int main() {
  int ntestcase;
  scanf("%d\n", &ntestcase);
  REP(i,101)
    REP(j,101)
      lawn[i][j] = 0;
  for (int test_id = 1; test_id <= ntestcase; test_id++) {
    int res;
  
    int n,m;
    scanf("%d%d\n", &n, &m);
  
    int dummy;
    REP(i, n) {
      REP(j, m) {
        scanf("%d", &dummy);
        lawn[i][j] = dummy;
      }scanf("\n");
    }

    bool possible = solve(n,m);

    string answer = "NO";
    if (possible)
      answer = "YES";

    printf("Case #%d: %s\n", test_id, answer.c_str());
  }

  return 0;
}
