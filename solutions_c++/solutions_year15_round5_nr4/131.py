/* 
  2014.03.26 15:10
  http://codeforces.ru/gym/100289/
*/


#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <memory.h>
#include <cmath>
#include <string> 
#include <ctime>

using namespace std;

// #undef Fdg_Home


void solveTest(int CS) {
  printf("Case #%d: ", CS);
  int n;
  scanf("%d", &n);
  vector<pair<long long, long long>> v(n);
  for (int i = 0; i < n; ++i) {
    scanf("%lld", &v[i].first);
  }
  for (int i = 0; i < n; ++i) {
    scanf("%lld", &v[i].second);
  }
  vector<long long> ans;
  while (true) {
    sort(v.begin(), v.end());
    int sz = 0;
    for (int i = 0; i < v.size(); ++i) {
      if (v[i].second == 0) continue;
      if (i > 0 && v[i].first == v[sz - 1].first) {
        v[sz - 1].second += v[i].second;
      } else {
        v[sz++] = v[i];
      }
    }
    if (sz == 0) break;
    v.resize(sz);
    // neg
    bool found = false;
    // for (int i = (int)v.size() - 1; i > 0; --i) {
    //   long long d = v[0].first - v[i].first;
    //   bool ok = true;
    //   vector<pair<long long, long long>> tmp = v, nx;
    //   int ptr = 0;
    //   for (int i = 0; i < tmp.size(); ++i) {
    //     while (ptr < tmp.size() && tmp[i].first - tmp[ptr].first > d) ++ptr;
    //     if (tmp[i].second == 0) continue;
    //     if (ptr == tmp.size() || tmp[ptr].second < tmp[i].second
    //       || tmp[i].first - tmp[ptr].first != d) {
    //       ok = false;
    //       break;
    //     }
    //     if (ptr == i) {
    //       if (tmp[ptr].second % 2 == 0) {
    //         tmp[ptr].second /= 2;
    //         nx.push_back(tmp[ptr]);
    //       } else {
    //         ok = false;
    //         break;
    //       }
    //       continue;
    //     }
    //     tmp[ptr].second -= tmp[i].second;
    //     nx.push_back({tmp[ptr].first, tmp[i].second});
    //     tmp[i].second = 0;
    //   }
    //   // cout << d << endl;
    //   if (ok) {
    //     // cout << d << endl;
    //     ans.push_back(d);
    //     v = nx;
    //     found = true;
    //     break;
    //   }
    // }
    for (int i = (int)v.size() - 1; !found && i >= 0; --i) {
      long long d = v.back().first - v[i].first;
      bool ok = true;
      vector<pair<long long, long long>> tmp = v, nx;
      int ptr = v.size() - 1;
      for (int i = (int)tmp.size() - 1; i >= 0; --i) {
        while (ptr >= 0 && tmp[i].first - tmp[ptr].first < d) --ptr;
        if (tmp[i].second == 0) continue;
        if (ptr < 0 || tmp[ptr].second < tmp[i].second
            || tmp[i].first - tmp[ptr].first != d) {
          ok = false;
          break;
        }
        if (ptr == i) {
          if (tmp[ptr].second % 2 == 0) {
            tmp[ptr].second /= 2;
            nx.push_back(tmp[ptr]);
          } else {
            ok = false;
            break;
          }
          continue;
        }
        tmp[ptr].second -= tmp[i].second;
        nx.push_back({tmp[ptr].first, tmp[i].second});
        tmp[i].second = 0;
      }
      // cout << d << endl;
      if (ok) {
        // cout << d << endl;
        ans.push_back(d);
        v = nx;
        found = true;
        break;
      }
    }
    if (!found) break;
  }
  for (int i = 0; i < ans.size(); ++i) {
    printf("%lld ", ans[i]);
  }
  printf("\n");
}

int main() {
  freopen("output.txt", "w", stdout);
  int T;
  scanf("%d\n", &T);
  for (int test = 1; test <= T; ++test) {
    solveTest(test);
  }
  return 0;
}

