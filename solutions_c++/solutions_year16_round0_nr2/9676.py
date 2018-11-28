#include <bits/stdc++.h>

#define each(i, c) for (auto& i : c)
#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

template<typename P, typename Q>
ostream& operator << (ostream& os, pair<P, Q> p)
{
  os << "(" << p.first << "," << p.second << ")";
  return os;
}

string flip(string s, int idx)
{
  reverse(s.begin(), s.begin() + idx + 1);
  for (int i = 0; i <= idx; ++i) {
    s[i] = (s[i] == '-') ? '+' : '-';
  }
  return s;
}

int solve_small(string src)
{
  queue<string> q;
  map<string, int> cost;
  cost[src] = 0;
  for (q.push(src); q.size(); q.pop()) {
    string s = q.front();
    for (int i = 0; i < s.size(); ++i) {
      string t = flip(s, i);
      if (!cost.count(t)) {
        cost[t] = cost[s] + 1;
        q.push(t);
      }
    }
  }
  return cost[string(src.size(), '+')];
}

int main(int argc, char *argv[])
{
  // flip("-+--+", 0);
  // flip("-+--+", 1);
  // flip("-+--+", 2);
  // flip("-+--+", 3);
  // flip("-+--+", 4);

  int tc;
  cin >> tc;
  while (tc--) {
    string s;
    cin >> s;
    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << solve_small(s) << endl;
  }
  return 0;
}
