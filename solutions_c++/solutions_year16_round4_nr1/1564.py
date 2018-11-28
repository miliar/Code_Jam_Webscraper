#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

#define MAXN 2000
#define INF 1000000000

using namespace std;

typedef long long ll;
typedef long double ld;

int x[MAXN], y[MAXN];

int n, r, p, s;

bool bf(string& curr, int k) {
  if(k >= n) {
    cerr << "testing " << curr << endl;

    string run = curr, next;
    while(run.size() > 1) {
      for(int i = 0; i < run.size(); i += 2) {
        if(run[i] == run[i + 1]) return false;
        if((run[i] == 'S' && run[i + 1] == 'P') ||
          (run[i] == 'P' && run[i + 1] == 'R') ||
          (run[i] == 'R' && run[i + 1] == 'S')) {

          next.push_back(run[i]);
        } else {
          next.push_back(run[i + 1]);
        }
      }
      run = next; next = "";
      cerr << "  - " << run << endl;
    }
    return true;
  }

  if(p > 0) {
    curr.push_back('P'); p--;
    if(bf(curr, k + 1)) return true;
    curr.pop_back(); p++;
  }

  if(r > 0) {
    curr.push_back('R'); r--;
    if(bf(curr, k + 1)) return true;
    curr.pop_back(); r++;
  }

  if(s > 0) {
    curr.push_back('S'); s--;
    if(bf(curr, k + 1)) return true;
    curr.pop_back(); s++;
  }

  return false;
}

int main() {
  int t; scanf("%d", &t);
  for(int tc = 1; tc <= t; tc++) {
    scanf("%d %d %d %d", &n, &r, &p, &s);
    n = 1 << n;

    string sol; bf(sol, 0);

    printf("Case #%d: ", tc);
    if(sol.empty()) printf("IMPOSSIBLE\n");
    else printf("%s\n", sol.c_str());
  }
  return 0;
}
