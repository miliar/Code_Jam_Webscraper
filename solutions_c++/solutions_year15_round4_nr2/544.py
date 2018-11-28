#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <tuple>
#include <vector>
using namespace std;

using LD = long double;

struct Item {
  int64_t R, C;
};

const int kMul = 10000;
int64_t ReadDouble() {
  string value;
  cin >> value;

  int a, b;
  sscanf(value.c_str(), "%d.%d", &a, &b);

  return 1LL * a * kMul + b;
}

void Solve() {
  int N;
  cin >> N;

  int64_t V = ReadDouble();
  int64_t X = ReadDouble();

  vector<Item> S(N);
  for (Item& s : S) {
    s.R = ReadDouble();
    s.C = ReadDouble();
  }

  assert(N <= 2);
  cout.precision(20);

  if (N == 1) {
    if (X != S[0].C) {
      cout << "IMPOSSIBLE";
    } else {
      cout << fixed << ((LD) V / S[0].R);
    }
    return;
  }

  if (S[0].C == S[1].C) {
    if (X * V != V * S[1].C) {
      cout << "IMPOSSIBLE";
      return;
    }

    LD t = (LD) V / (S[0].R + S[1].R);
    cout << fixed << t;
  } else {
    int64_t up = X * V - V * S[1].C;
    int64_t down = S[0].C - S[1].C;
    if (down < 0) {
      up = -up;
      down = -down;
    }
    if (up < 0 || up > V * down) {
      cout << "IMPOSSIBLE";
      return;
    }
    LD V1 = (LD) up / down;

    LD t = max(V1 / S[0].R, (V - V1) / S[1].R);
    cout << fixed << t;
  }
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/B-small-attempt3.in", "rb", stdin);
  freopen("../Console/B-small-attempt3.out", "wb", stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int tc = 0; tc < T; ++tc) {
    cout << "Case #" << tc + 1 << ": ";
    Solve();
    cout << endl;
  }

  return 0;
}
