#include <algorithm>
#include <bitset>
#include <cassert>
#include <cinttypes>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

using Table = vector<vector<int>>;

struct Item {
  int x, y, z;
};

int Dist2(const Item& a, const Item& b) {
  int dx = a.x - b.x;
  int dy = a.y - b.y;
  int dz = a.z - b.z;

  return dx * dx + dy * dy + dz * dz;
}

void Dfs(int i, int max_dist, vector<char>& used, const Table& D) {
  used[i] = true;
  for (int j = 0; j < D.size(); ++j) {
    if (used[j]) {
      continue;
    }

    if (D[i][j] <= max_dist) {
      Dfs(j, max_dist, used, D);
    }
  }
}

bool Can(int max_dist, const Table& D) {
  int N = D.size();
  vector<char> used(N, false);

  Dfs(0, max_dist, used, D);
  return used[1];
}

void Solve() {
  int N, S;
  cin >> N >> S;

  vector<Item> A(N);
  for (Item& i : A) {
    cin >> i.x >> i.y >> i.z;

    int vx, vy, vz;
    cin >> vx >> vy >> vz;
    assert(vx == 0);
    assert(vy == 0);
    assert(vz == 0);
  }

  vector<vector<int>> D(N, vector<int>(N, 0));
  for (int i = 0; i < N; ++i) {
    for (int j = i + 1; j < N; ++j) {
      D[i][j] = D[j][i] = Dist2(A[i], A[j]);
    }
  }

  int lo = 0, hi = 10000 * 10000;
  while (lo < hi) {
    int med = (lo + hi) / 2;
    if (!Can(med, D)) {
      lo = med + 1;
    } else {
      hi = med;
    }
  }

  cout.precision(10);
  cout << fixed << sqrt(lo) << endl;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/C-small-attempt0.in", "rb", stdin);
  freopen("../Console/C-small-attempt0.out", "wb", stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int tc = 0; tc < T; ++tc) {
    cout << "Case #" << tc + 1 << ": ";
    Solve();
  }

  return 0;
}
