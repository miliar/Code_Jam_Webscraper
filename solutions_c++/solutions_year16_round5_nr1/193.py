#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long lint;

const int MAX_N = 20010;

char s[MAX_N];

int solve() {
  scanf("%s", s);
  int n = strlen(s);
  string stk;
  int ans = 0;
  REP (i, n) {
    if (stk.empty() || stk.back() != s[i]) {
      stk.push_back(s[i]);
    } else {
      stk.pop_back();
      ans += 10;
    }
  }
  return ans + SZ(stk) / 2 * 5;
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: %d\n", index, solve());
  }
  return 0;
}
