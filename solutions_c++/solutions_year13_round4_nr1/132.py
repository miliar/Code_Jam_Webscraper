#include <map>
#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

typedef long long llint;

const llint MOD = 1000002013;

llint sum(llint n, llint k) {
  return (n + (n - k + 1)) * k / 2 % MOD;
}

int main() {
  int re, n, m, s, t, c;
  map<int, llint> in, out;
  llint ans;

  scanf("%d", &re);
  for (int ri = 1; ri <= re; ++ri) {
    scanf("%d%d", &n, &m);
    ans = 0;
    in.clear();
    out.clear();
    for (int i = 0; i < m; ++i) {
      scanf("%d%d%d", &s, &t, &c);
      ans += sum(n, t - s) * c % MOD;
      in[s] += c;
      out[t] += c;
    }
    for (map<int, llint>::reverse_iterator it = in.rbegin(); it != in.rend(); ++it) {
      while (it->second > 0) {
        map<int, llint>::iterator jt = out.lower_bound(it->first);
        llint d = min(it->second, jt->second);
        it->second -= d;
        jt->second -= d;
        d %= MOD;
        ans -= sum(n, jt->first - it->first) * d % MOD;
        if (jt->second == 0) {
          out.erase(jt);
        }
      }
    }
    ans = (ans % MOD + MOD) % MOD;
    printf("Case #%d: %d\n", ri, (int)ans);
  }

  return 0;
}
