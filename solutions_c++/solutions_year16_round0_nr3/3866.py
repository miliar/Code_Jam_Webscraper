#include <bits/stdc++.h>
using namespace std;

int get_divisor(long long num) {
  if (num <= 1) {
    return -1;
  } else {
    for (long long i = 2; i * i <= num; ++i) {
      if (num % i == 0) {
        return i;
      }
    }
    return -1;
  }
}

long long to_sys(string s, long long base) {
  long long res = 0;
  for (int i = 0; i < s.size(); ++i) {
    res *= base;
    res += s[i] - '0';
  }
  return res;
}

inline long long to_long(string s) {
  long long res = 0;
  for (int i = 0; i < s.size(); ++i) {
    res *= 2;
    res += s[i] - '0';
  }
  return res;
}

string to_str(long long val) {
  string res;
  while (val) {
    res += (val & 1) + '0';
    val >>= 1;
  }
  return res;
}

inline string random_string(int len) {
  string res(1, '1');
  for (int i = 1; i < len - 1; ++i) {
    res += (rand() & 1) + '0';
  }
  res += '1';
  return res;
}

vector<pair<string, vector<int>>> solve() {
  int N, J;
  cin >> N >> J;

  vector<pair<string, vector<int>>> res;
  set<string> s;
  while (res.size() < J) {
    string str = random_string(N);
    while (s.count(str)) {
      str = random_string(N);
    }
    vector<int> cur;
    for (int i = 2; i <= 10; ++i) {
      cur.push_back(get_divisor(to_sys(str, i)));
    }
    if (find(cur.begin(), cur.end(), -1) == cur.end()) {
      res.push_back({str, cur});
    }
    s.insert(str);
  }
  sort(res.begin(), res.end());
  return res;
}

int main() {
  srand(937);
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int test = 1; test <= T; test++) {
    cout << "Case #" << test << ":" << endl;
    vector<pair<string, vector<int>>> v = solve();
    for (const auto& x : v) {
      cout << x.first << " ";
      for (int t : x.second) {
        cout << t << " ";
      }
      cout << endl;
    }
  }
}
