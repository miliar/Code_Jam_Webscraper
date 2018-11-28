#include <iostream>
#include <cstdio>
#include <set>
#include <iterator>
#include <cassert>
#include <functional>
#include <algorithm>
#include <vector>
using namespace std;

auto predict = [](auto v, auto b) {
  assert(b.size());
  auto iter = b.upper_bound(v);
  return iter == b.end() ? b.begin() : iter;
};

auto war2 = [](auto a, auto b) {
  assert(a.size() == b.size());
  int result = 0;
  auto copya = a;
  for (auto i = copya.rbegin(); i != copya.rend(); ++i) {
    {
      auto iter = a.upper_bound(*b.begin());
      if (iter != a.end()) {
        a.erase(iter);
        b.erase(b.begin());
        result++;
        continue;
      }
    }
    auto iter = predict(*i, b);
    if (*i > *iter)
      result++;
    assert(iter != b.end());
    assert(b.count(*iter));
    a.erase(*i);
    b.erase(*iter);
  }
  return result;
};


auto war = [](auto a, auto b) {
  assert(a.size() == b.size());
  int result = 0;
  for (auto i = a.rbegin(); i != a.rend(); ++i) {
    auto iter = predict(*i, b);
    if (*i > *iter)
      result++;
    assert(iter != b.end());
    assert(b.count(*iter));
    b.erase(*iter);
  }
  return result;
};

auto work = [](auto a, auto b) {
  assert(a.size() == b.size());
  int allwar = war(a, b);
  int s = war2(a, b);
  auto copya = a;
  for (auto v : copya) {
    a.erase(v);
    b.erase(prev(end(b)));
    s = max(s, war2(a, b));
  }
  return make_pair(s, allwar);
};

int main() {
  freopen("D-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  set<double> a, b;
  int kase;
  cin >> kase;
  for (int i = 0; i < kase; i++) {
    a.clear(), b.clear();
    int n;
    cin >> n;
    for (int j = 0; j < n; j++) {
      double k;
      cin >> k;
      a.insert(k);
    }
    for (int j = 0; j < n; j++) {
      double k;
      cin >> k;
      b.insert(k);
    }
    auto result = work(a, b);
    cout << "Case #" << i + 1 << ": " << result.first << " " << result.second
         << endl;
  }
}
