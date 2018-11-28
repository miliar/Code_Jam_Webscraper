#include <iomanip>
#include <algorithm>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

template<class T>
ostream& operator<< (ostream& fout, const vector<T>& vec) {
  for (size_t i = 0; i < vec.size(); ++i) {
    fout << vec[i] << ' ';
  }
  return fout;
}

template <class T>
istream& operator>> (istream& fin, vector<T>& vec) {
  for (size_t i = 0; i < vec.size(); ++i) {
    cin >> vec[i];
  }
  return fin;
}

uint64_t check(uint64_t arg) {
  for (uint64_t i = 2; i*i <= arg; ++i) {
    if (arg % i == 0) {
      return i;
    }
  }
  return -1;
}

uint64_t to_base(uint64_t arg, int base) {
  uint64_t res = 0;
  for (int i = 64; i--; ) {
    res *= base;
    res += ((arg >> i) & 1);
  }
  return res;
}

bool big_check(uint64_t arg) {
  vector<uint64_t> res;
  for (int i = 2; i <= 10; ++i) {
    uint64_t in_base = to_base(arg, i);
    uint64_t diviser = check(in_base);
    if (diviser == -1) {
      return false;
    } else {
      res.push_back(diviser);
    }
  }
  cout << to_base(arg, 10);
  for (const uint64_t cert : res) {
    cout << ' ' << cert;
  }
  cout << '\n';
  return true;
}

int main() {
#ifndef LOCAL
  //freopen("input.txt", "rt", stdin);
  //freopen("output.txt", "wt", stdout);
#endif
#ifdef LOCAL
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);
#endif

  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  int N, J;
  cin >> N >> J;
  --N;
  int count = 0;
  for (uint64_t el = (1 << N) + 1;; ++el) {
    if ((el & 1) == 0) {
      continue;
    }
    cerr << count << endl;
    if (count == J) {
      break;
    }
    if (big_check(el)) {
      ++count;
    }
}
  return 0;
}
