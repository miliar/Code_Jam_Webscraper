#include <limits.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <vector>
#include <deque>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <iterator>
#include <set>
static const int INF = std::numeric_limits<int>::max();

static const int MOD = 1000000007;

char last(const std::string& s)
{
  return s[s.size() - 1];
}

bool possible(std::vector<std::string> v)
{
  std::string s;

  std::sort(std::begin(v), std::end(v), [](const std::string& lhs,
                                           const std::string& rhs)
            {
              return lhs.size() < rhs.size();
            });

  {
    std::vector<int> used(v.size());

    for(int i = 0; i < (int)v.size(); ++i) {
      if(used[i]) {
        continue;
      }
      used[i] = 1;

      std::string a = v[i];

      for(;;) {
        bool found = false;
        for(int j = 0; j < (int)v.size(); ++j) {
          if(used[j]) {
            continue;
          }

          if(last(a) == v[j][0]) {
            used[j] = 1;
            a += v[j];
            found = true;
            break;
          }

          if(last(v[j]) == a[0]) {
            used[j] = 1;
            a = v[j] + a;
            found = true;
            break;
          }
        }

        if(!found) {
          break;
        }
      }

      s += a;
    }
  }

  // std::cout << s << std::endl;

  s.erase(std::unique(std::begin(s), std::end(s)), std::end(s));

  std::vector<int> used(256);

  for(int i = 0; i < (int)s.size(); ++i) {
    if(used[(int)s[i]]) {
      return false;
    }
    used[(int)s[i]] = 1;
  }
  return true;
}

int fmod(int n)
{
  long long res = 1;
  for(int i = 2; i <= n; ++i) {
    res *= i;
    res %= MOD;
  }
  return res;
}

int main()
{
  int T;

  std::cin >> T;

  for(int test = 1; test <= T; ++test) {
    int N;
    std::cin >> N;

    std::vector<std::string> v(N);
    for(int i = 0; i < N; ++i) {
      std::string a;
      std::cin >> a;
      a.erase(std::unique(std::begin(a), std::end(a)), std::end(a));
      v[i] = std::move(a);
    }

    std::sort(std::begin(v), std::end(v));

    // for(auto& k : v) {
    //   std::cout << "ent: " << k << std::endl;
    // }

    if(!possible(v)) {
      std::cout << "Case #" << test << ": " << 0 << std::endl;
      continue;
    }

    std::vector<std::pair<int, std::string>> z;
    {
      std::string prev = v[0];
      int cnt = 1;
      for(int i = 1; i < (int)v.size(); ++i) {
        if(prev == v[i]) {
          ++cnt;
          continue;
        }
        z.emplace_back(fmod(cnt), prev);
        prev = v[i];
        cnt = 1;
      }
      z.emplace_back(fmod(cnt), prev);
    }

    // for(auto& k : z) {
    //   std::cout << k.first << "," << k.second << std::endl;
    // }

    std::sort(std::begin(z), std::end(z), [](const std::pair<int, std::string>& lhs,
                                             const std::pair<int, std::string>& rhs)
              {
                return lhs.second.size() < rhs.second.size();
              });

    std::vector<std::pair<int, std::string>> z2;
    {
      std::vector<int> used(z.size());

      for(int i = 0; i < (int)z.size(); ++i) {
        if(used[i]) {
          continue;
        }
        used[i] = 1;

        int n = z[i].first;
        std::string a = z[i].second;

        for(;;) {
          bool found = false;
          for(int j = 0; j < (int)z.size(); ++j) {
            if(used[j]) {
              continue;
            }

            if(last(a) == z[j].second[0]) {
              used[j] = 1;
              a += z[j].second;
              n = ((long long)n * z[j].first) % MOD;
              found = true;
              break;
            }

            if(last(z[j].second) == a[0]) {
              used[j] = 1;
              a = z[j].second + a;
              n = ((long long)n * z[j].first) % MOD;
              found = true;
              break;
            }
          }

          if(!found) {
            break;
          }
        }

        z2.emplace_back(n, a);
      }
    }

    long long res = 1;

    for(auto& k : z2) {
      res *= k.first;
      res %= MOD;
    }
    res *= fmod(z2.size());
    res %= MOD;

    std::cout << "Case #" << test << ": " << res << std::endl;
  }
}
