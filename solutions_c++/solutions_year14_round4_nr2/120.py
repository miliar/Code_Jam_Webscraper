#include <cassert>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <set>
#include <bitset>

using namespace std;

#define REP(i, n) FOR(i, 0, n)
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

struct S {
  int val;

  int val_idx;
  int idx;
};

typedef bitset<1000> BS;
int n;
vector<S> A; 

int eval(const BS& state) {
  int cnt_left = state.count();
  int val = 0;

  REP(i, cnt_left) val -= i;
  REP(i, n-1) {
    int is = state.test(i);
    if (is == 1) val += A[i].idx;
    if (is == 0) if (A[i].idx < A[n-1].idx) ++val;
  }
  REP(b, n-1) REP(a, b) {
    int bs = state.test(b), as = state.test(a);
    if (as == 1 && bs == 1) {
      val += (A[a].idx > A[b].idx);
    } else if (as == 0 && bs == 0) {
      val += (A[a].idx < A[b].idx);
    }
  }

  return val;
}


int main(void)
{
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    scanf("%d", &n);
    A.clear();

    REP(i, n) {
      int val; scanf("%d", &val);
      A.push_back({val, -1, i});
    }

    sort(A.begin(), A.end(), [](S a, S b) {
        return a.val < b.val;
      });
    REP(i, n) A[i].val_idx = i;
    vector<S> byidx = A;
    sort(byidx.begin(), byidx.end(), [](S a, S b) {
        return a.idx < b.idx;
      });

    bitset<1000> state;
    int ans = eval(state);
    int curr = ans;

    REP(i, n) {
      if (byidx[i].val_idx == n-1) continue;
      int val_idx = byidx[i].val_idx;
      state.flip(val_idx);
      int new_val = eval(state);
      if (new_val < curr) {
        curr = new_val;
        ans = min(ans, curr);
      } else {
        state.flip(val_idx);
        assert(curr == eval(state));
      }
    }

    printf("Case #%d: %d\n", tc+1, ans);
    fflush(stdout);
  }
  return 0;
}
