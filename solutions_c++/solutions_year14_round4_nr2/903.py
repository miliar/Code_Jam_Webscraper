/*
 * b.cpp
 *
 *  Created on: May 31, 2014
 *      Author: istrandjev
 */

#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <functional>
#include <unordered_set>
#include <unordered_map>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;

int helper_merge(vector<int>& b, int from, int len) {
  if (len == 1) {
    return 0;
  }
  if (len == 2) {
    if (b[from] > b[from + 1]) {
      swap(b[from], b[from + 1]);
      return 1;
    }
    return 0;
  }
  int ans = 0;
  ans += helper_merge(b, from, len / 2);
  ans += helper_merge(b, from + len / 2, len - len / 2);
  vector<int> temp(len);
  int idx = 0;
  int ia = from;
  int ea = from + len / 2;
  int ib = ea;
  int eb = from + len;
  while (ia < ea && ib < eb) {
    if (b[ia] <= b[ib]) {
      temp[idx++] = b[ia++];
    } else {
      temp[idx++] = b[ib++];
      ans += ea - ia;
    }
  }
  while (ia < ea) {
    temp[idx++] = b[ia++];
  }
  while (ib < eb) {
    temp[idx++] = b[ib++];
  }
  for (int i = 0; i < len; ++i) {
    b[from + i] = temp[i];
  }
  return ans;
}
int inversions(const vector<int>& a) {
  vector<int> b(a);
  return helper_merge(b, 0, (int)b.size());
}

int solve(const vector<int>& a) {
  int n = (int)a.size();
  int best = -1;
  for (int i = 0; i < n; ++i) {
    vector<int> b = a;
    int bi = i;
    for (int j = 0; j < n; ++j) {
      if (b[j] > b[bi]) {
        bi = j;
      }
    }
    if (bi < i) {
      for (int j = bi; j < i; ++j) {
        swap(b[j], b[j + 1]);
      }
    } else if (bi > i) {
      for (int j = bi; j > i; --j) {
        swap(b[j], b[j - 1]);
      }
    }
    sort(b.begin(), b.begin() + i + 1);
    sort(b.begin() + i, b.end());
    reverse(b.begin() + i, b.end());

    unordered_map<int, int> m;
    for (int i = 0; i < (int)b.size(); ++i) {
      m[b[i]] = i;
    }

    vector<int> c(n);
    for (int i = 0; i < (int)a.size(); ++i) {
      c[i] = m[a[i]];
    }

    int temp = inversions(c);
    if (best == -1 || temp < best) {
      best = temp;
    }
  }
  return best;
}

bool valid(const vector<int>& a) {
  int bi = 0;
  for (int i = 0; i < (int)a.size(); ++i) {
    if (a[i] > a[bi]) {
      bi = i;
    }
  }
  for (int i = 0; i < bi; ++i) {
    if (a[i] > a[i+1]) {
      return false;
    }
  }
  for (int i = bi; i + 1 < (int)a.size(); ++i) {
    if (a[i] < a[i+1]) {
      return false;
    }
  }
  return true;
}
int brute(const vector<int>& a) {
  vector<int> b = a;
  int n = (int)b.size();
  sort(all(b));
  int best = -1;
  do {
    if (!valid(b)) {
      continue;
    }
    unordered_map<int, int> m;
    for (int i = 0; i < (int)b.size(); ++i) {
      m[b[i]] = i;
    }

    vector<int> c(n);
    for (int i = 0; i < (int)a.size(); ++i) {
      c[i] = m[a[i]];
    }
    int temp = inversions(c);
    if (best == -1 || temp < best) {
      best = temp;
    }
  } while (next_permutation(all(b)));
  return best;
}

void test(int n) {
  vector<int> a(n);
  for (int i = 0; i < (int)a.size(); ++i) {
    a[i] = i + 1;
  }
  do {
    int y = solve(a);
    int x = brute(a);
    if (x != y) {
      printf("expected: %d got: %d\n", x, y);
      for (int i = 0; i < (int)a.size(); ++i) {
        printf("%d%c", a[i], ((i + 1) != a.size() ? ' ' : '\n'));
      }
      return;
    }
  } while (next_permutation(all(a)));
}
int main() {
  freopen("google.in", "r", stdin);
  freopen("google.out", "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < (int)a.size(); ++i) {
      scanf("%d", &a[i]);
    }
    cout << "Case #" << it << ": " << brute(a) << endl;
  }
  // test(7);
  return 0;
}

