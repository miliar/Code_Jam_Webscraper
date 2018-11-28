#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <cassert>
#include <set>

using namespace std;

const int MAXM = 2005;

const int64_t mod = 1000002013;

int m;
int a[MAXM];
int b[MAXM];
int64_t p[MAXM];

vector<int> stations;

int64_t available[MAXM * 2];
int64_t needed[MAXM * 2];

int64_t calculate(int64_t n, int64_t a, int64_t b, int64_t p) {
  int64_t d = std::abs(a - b);
  int64_t c = ((d + 1) * n - d * (d + 1) / 2) % mod;
  return (c * p) % mod;
}

void Solve() {
  int64_t n;
  cin >> n >> m;

  int64_t cost = 0;

  stations.clear();

  for (int i = 0; i < m; i++) {
    cin >> a[i] >> b[i] >> p[i];
    cost = (cost + calculate(n, a[i], b[i], p[i])) % mod;
    stations.push_back(a[i]);
    stations.push_back(b[i]);
  }

  sort(stations.begin(), stations.end());
  stations.erase(unique(stations.begin(), stations.end()), stations.end());

  for (int i = 0; i < m; i++) {
    for (int j = 0; j < stations.size(); j++) {
      if (a[i] == stations[j]) {
        a[i] = j;
        break;
      }
    }
    for (int j = 0; j < stations.size(); j++) {
      if (b[i] == stations[j]) {
        b[i] = j;
        break;
      }
    }
  }

  for (int i = 0; i < m; i++) {
    available[a[i]] += p[i];
    needed[b[i]] += p[i];
  }


  for (int station = 0; station < stations.size(); station++) {
    for (int i = station; i >= 0; i--) {
      int64_t delta = std::min(needed[station], available[i]);
      needed[station] -= delta;
      available[i] -= delta;

      cost = (cost - calculate(n, stations[i], stations[station], delta) + mod) % mod;
    }

    for (int i = station; i < stations.size(); i++) {
      int64_t delta = std::min(needed[station], available[i]);
      needed[station] -= delta;
      available[i] -= delta;

      cost = (cost - calculate(n, stations[i], stations[station], delta) + mod) % mod;
    }
  }

  cout << cost << endl;
}

int main() {
  int num_cases;
  cin >> num_cases;
  for (int i = 1; i <= num_cases; i++) {
    cout << "Case #" << i << ": ";
    Solve();
  }
}
