#include <bits/stdc++.h>

using namespace std;

const int M = 1000100;

typedef long long ll;

bool u[M];
int p[M], m = 0;
int n, J;

void sito() {
  for (int i = 2; i < M; ++i)
    if (!u[i]) {
      p[m++] = i;
      for (int j = i; j < M; j += i)
        u[j] = true;
    }
}

int div(ll x) {
  for (int i = 0; i < m && p[i] < x; ++i)
    if (x % p[i] == 0) 
      return p[i];
  return -1;
}

ll inBase(ll base, vector<int> s) {
  ll ans = 0;
  for (int x : s) {
    ans = (base * ans + x);
  }
  return ans;
}

void read() {
  cin >> n >> J;

  vector<pair<vector<int>, vector<int>>> ans;

  for (int mask = 0; mask < (1 << (n - 2)) && (int) ans.size() < J; ++mask) {
    vector<int> s(n);
    vector<int> divs;

    s[0] = s[n - 1] = 1;
    for (int j = 0; j < n - 2; ++j)
      s[j + 1] = (mask >> j) & 1;

    bool bad = false;

    for (int base = 2; base <= 10; ++base) {
      ll x = inBase(base, s);
      if (div(x) == -1) {
        bad = true;
        break;
      } else
        divs.push_back(div(x));
    }

    if (!bad)
      ans.emplace_back(s, divs);
  }


  cout << endl;
  for (auto pa : ans) {
    for (int x : pa.first)
      cout << x;
    cout << " ";
    for (int y : pa.second)
      cout << y << " ";
    cout << endl;
  }
}


int main() {
  sito();
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    read();
    cerr << "Case #" << i << " done.\n";
  }
  return 0;
}
