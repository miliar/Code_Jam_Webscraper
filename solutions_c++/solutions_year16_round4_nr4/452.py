#define NDEBUG
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

template <typename T> inline T set_bit(const T &x, int index) {
  return x | ((T)1 << index);
}
template<typename T, typename U> inline bool makemin(T &res, const U &x) {
  if (x < res) {
    res = x;
    return true;
  }
  return false;
}
template <typename T> inline int get_bit(const T &x, int index) {
  return int((x >> index) & 1);
}
template <typename T> int bitcount(T x) {
  int ret;
  for (ret=0; x!=0; ++ret, x -= x&-x) ;
  return ret;
}
#define MINUSONE(v) memset((v), -1, sizeof (v))

int n;
bool mat[4][4];
int memo[1<<4][1<<4];
int calc(int wm, int mm) {
  int& ret = memo[wm][mm];
  if (ret != -1) {
    return ret;
  }
  ret = true;
  for (int w=0; w<n; ++w) {
    if (get_bit(wm, w)) {
      continue;
    }
    bool knows_one = false;
    bool sub_ok = true;
    for (int m=0; m<n; ++m) {
      if (get_bit(mm, m) || !mat[w][m]) {
        continue;
      }
      knows_one = true;
      sub_ok &= calc(set_bit(wm, w), set_bit(mm, m));
    }
    ret &= knows_one && sub_ok;
  }
  return ret;
}

int solve() {
  cin >> n;
  vector<string> origmat(n);

  int optionmask = 0;
  for (int i=0; i<n; ++i) {
    cin >> origmat[i];
    for (int j=0; j<n; ++j) {
      if (origmat[i][j] == '0') {
        optionmask = set_bit(optionmask, i*n + j);
      }
    }
  }

  int ans = n*n;
  for (int mask=optionmask;; mask=(mask-1)&optionmask) {
    int cost = bitcount(mask);
    for (int i=0; i<n; ++i) {
      for (int j=0; j<n; ++j) {
        mat[i][j] = origmat[i][j] == '1' || get_bit(mask, i*n + j);
      }
    }
    MINUSONE(memo);
    if (calc(0, 0)) {
      makemin(ans, cost);
    }

    if (mask == 0) {
      break;
    }
  }
  return ans;
}

int main() {
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    cout << "Case #" << tt << ": " << solve() << endl;
  }
}
