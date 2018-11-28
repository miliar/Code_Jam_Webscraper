#include <stdio.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>
#include <stack>
#include <string>

using namespace std;

#define inf 1000000007
#define rep(i, n) for(int i = 0; i < n; i++)

typedef long long ll;

string dfs(int w, int n) {
  if(n == 0) {
    if(w == 0) {
      return "R";
    }
    else if(w == 1) {
      return "P";
    }
    else {
      return "S";
    }
  }
  else {
    string a = dfs(w, n - 1);
    string b;
    if(w == 0) {
      b = dfs(2, n - 1);
    }
    else if(w == 1) {
      b = dfs(0, n - 1);
    }
    else {
      b = dfs(1, n - 1);
    }
    return min(a, b) + max(a, b);
  }
}

int main() {
  int t;
  scanf("%d",&t);
  rep(k, t) {
    int n;
    scanf("%d", &n);
    int r, p, s;
    scanf("%d%d%d",&r,&p,&s);
    rep(i, n) {
      int rw = (r + s - p) / 2;
      int pw = (r + p - s) / 2;
      int sw = (s + p - r) / 2;
      r = rw;
      p = pw;
      s = sw;
      if(r < 0 || p < 0 || s < 0) {
        printf("Case #%d: IMPOSSIBLE\n", k + 1);
        goto aa;
      }
    }
    int w;
    if(r == 1) {
      w = 0;
    }
    else if(p == 1) {
      w = 1;
    }
    else {
      w = 2;
    }
    printf("Case #%d: %s\n", k + 1, dfs(w, n).c_str());
    aa:;
  }
}
