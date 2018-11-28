#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

#define mset(a, v) memset(a, v, sizeof(a));
#define mset0(a) mset(a, 0);

const int maxint = 0x7f7f7f7f, mod = 1000000007;
const double eps = 1e-8, pi = acos(-1.0);
 
void read() { }
template<typename... T> void read(int &h, T &... t) { scanf("%d", &h); read(t...); }
template<typename... T> void read(LL &h, T &... t) { scanf("%lld", &h); read(t...); }
template<typename... T> void read(double &h, T &... t) { scanf("%lf", &h); read(t...); }

const int maxN = 10001;
int tests, n;
vector<int> numbers;
int e[maxN];
map<int, int> m;

int main() {
  freopen("D-small-attempt0.in", "r", stdin);
  freopen("D-small-attempt0.out", "w", stdout);
  read(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    int n;
    read(n);
    numbers.clear();
    for (int i = 1; i <= n; ++i) {
      read(e[i]);
      m[e[i]] = 0;
    }
    for (int i = 1; i <= n; ++i) {
      int f;
      read(f);
      m[e[i]] += f;
    }
    --m.begin()->second;
    while (!m.empty()) {
      auto top = m.begin();
      if (top->second == 0) {
        m.erase(m.begin()); 
        continue;
      }
      int n = top->first;
      int size = numbers.size();
      for (int j = 0; j < (1 << size); ++j) {
        int sum = 0;
        for (int k = 0; k < size; ++k) {
          if ((j >> k) & 1) {
            sum += numbers[k];
          }
        }
        sum += n;
        auto it = m.find(sum);
        if (--it->second == 0) {
          m.erase(it);
        }
      }
      numbers.push_back(n);
    }
    printf("Case #%d: ", tt);
    for (int i = 0; i < numbers.size(); ++i) {
      printf("%d%c", numbers[i], i + 1 == numbers.size() ? '\n' : ' ');
    }
  }
  return 0;
}
