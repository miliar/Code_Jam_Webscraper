#include<bits/stdc++.h>
using namespace std;

using vi = vector<int>;
using ii = pair<int,int>;
using ll = long long;
using llu = unsigned long long;
const int INF = numeric_limits<int>::max();

const int MAX = 1001;
int p[MAX];

int s(int t) {
  if (t == 1) return 1;
  if (p[t] == 0) return s(t - 1);
  int best = t;
  for (int size = 2; size < t; size++) {
    int n = t / size;
    int cuts = n;
    int b = t % size;
    if (b == 0) {
      cuts--;
      p[size] += n * p[t];
      best = min(best, cuts * p[t] + s(t - 1));
      p[size] -= n * p[t];
      continue;
    }
    p[size] += n * p[t];
    p[b] += p[t];
    best = min(best, cuts * p[t] + s(t - 1));
    p[size] -= n * p[t];
    p[b] -= p[t];
  }
  return best;
}

int main() {
  int tcc;
  cin >> tcc;
  for (int tc = 1; tc <= tcc; tc++) {
    int n; cin >> n;
    fill_n(p, MAX, 0);
    vi v(MAX, 0);
    while (n--) {
      int a; cin >> a;
      p[a]++;
      v[a]++;
    }
    int a = s(MAX - 1);
    printf("Case #%d: %d\n", tc, a);
  }
}
