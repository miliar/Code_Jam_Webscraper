#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

class Lawn {
  static const int N = 102;
  public:
  void read() {
    scanf("%d%d", &n_, &m_);
    for (int i = 0; i < n_; ++i)
      for (int j = 0; j < m_; ++j)
        scanf("%d", lawn_[i] + j);
  }

  bool check() const {
    for (int i = 0; i < n_; ++i) 
      row_[i] = *max_element(lawn_[i], lawn_[i] + m_);
    for (int i = 0; i < m_; ++i) {
      column_[i] = 0;
      for (int j =0 ; j < n_; ++j)
        column_[i] = max(column_[i], lawn_[j][i]);
    }

    for (int i = 0; i < n_; ++i)
      for (int j = 0; j < m_; ++j)
        if (lawn_[i][j] != min(row_[i], column_[j])) return false;

    return true;
  }

  private:
  int lawn_[N][N];
  int n_, m_;
  mutable int row_[N], column_[N];
};

int main() {
  int t;
  Lawn lawn;
  scanf("%d", &t);
  for (int tc=1; tc <= t; ++tc) {
    lawn.read();
    printf("Case #%d: %s\n", tc, lawn.check() ? "YES" : "NO");
  }
  return 0;
}
