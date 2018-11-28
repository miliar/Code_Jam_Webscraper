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

const int N = 1000005;

const int inf = 1 << 29;

vector<int> f(int n)
{
  char buff[100];
  sprintf(buff, "%d", n);
  string s(buff);
  reverse(s.begin(), s.end());
  int m;
  sscanf(s.c_str(), "%d", &m);
  return (m < N) ? vector<int>({n + 1, m}) : vector<int>({n});
}

int main(int argc, char *argv[])
{
  int cost[N];
  fill(cost, cost + N, inf);
  cost[1] = 1;

  priority_queue<pair<int, int>> q;
  q.push(make_pair(-1, 1));

  while (q.size()) {
    pair<int, int> p = q.top();
    int curr = p.second;
    q.pop();
    if (cost[curr] != -p.first) continue;
    each (next, f(curr)) {
      if (cost[curr] + 1 < cost[next]) {
        cost[next] = cost[curr] + 1;
        q.push(make_pair(-cost[next], next));
      }
    }
  }

  int tc;
  cin >> tc;
  while (tc--) {
    int n;
    cin >> n;
    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << cost[n] << endl;
  }

  return 0;
}
