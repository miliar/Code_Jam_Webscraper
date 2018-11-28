#include <algorithm>
#include <cmath>
#include <climits>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;

typedef long long int64;
//typedef __int128_t int128;
typedef vector<int> veci;
typedef vector<string> vecs;

#define VAR(a, b) __typeof(b) a=(b)
#define FOREACH(it, c) for (VAR(it, (c).begin()); it != (c).end(); ++it)
#define TRACE(x) cout << #x << endl
#define DEBUG(x) cout << #x " = " << (x) << endl
#define DEBUGA(a, n) VAR(__p, a); cout << #a " = {"; for (int __i = 0; __i < n; ++__i, ++__p) cout << (__i == 0 ? "" : ", ") << *(__p); cout << "}" << endl
#define CLR(a, val) memset(a, val, sizeof(a))

template<class T1, class T2> ostream& operator << (ostream &o, const pair<T1, T2> &p)
{
  return o << "(" << p.first << ", " << p.second << ")";
}

template<class T> ostream& operator << (ostream &o, const vector<T> &v)
{
  o << '{';
  FOREACH(it, v) o << (it == v.begin() ? "" : ", ") << *it;
  return o << '}';
}

set<vector<int>> visited;
int N;
bool search(const vector<vector<int>> &chests, vector<int> &state, vector<int> &sol) {
  if (sol.size() == N)
    return true;
  if (visited.find(state) != visited.end())
    return false;
  visited.insert(state);
  for (int i = 0; i < N; i++) {
    if (!state[i] && state[N+chests[i][0]]) {
      sol.push_back(i+1);
      state[N+chests[i][0]]--;
      for (int j = 1; j < chests[i].size(); j++)
        state[N+chests[i][j]]++;
      state[i] = 1;
      if (search(chests, state, sol))
        return true;
      sol.pop_back();
      state[N+chests[i][0]]++;
      for (int j = 1; j < chests[i].size(); j++)
        state[N+chests[i][j]]--;
      state[i] = 0;
    }
  }
  return false;
}

void run(int tc)
{
  int K;
  cin >> K >> N;
  vector<int> Ks(K);
  int maxk = 0;
  for (int i = 0; i < K; i++) {
    cin >> Ks[i];
    maxk = max(Ks[i], maxk);
  }
  vector<vector<int>> chests(N);
  for (int i = 0; i < N; i++) {
    int k, t;
    cin >> t >> k;
    maxk = max(t, maxk);
    chests[i].push_back(t-1);
    for (int j = 0; j < k; j++) {
      int kj;
      cin >> kj;
      maxk = max(kj, maxk);
      chests[i].push_back(kj-1);
    }
  }

  vector<int> state(N + maxk);
  for (int i = 0; i < K; i++)
    state[N+Ks[i]-1]++;

  vector<int> sol;
  visited.clear();
  bool found = search(chests, state, sol);

  cout << "Case #" << (tc + 1) << ":";
  if (found)
    for (int i = 0; i < N; i++)
      cout << " " << sol[i];
  else
    cout << " IMPOSSIBLE";
  cout << endl;
}

int main()
{
  int T = 0, tc = 0;
  for (cin >> T; tc < T; tc++) run(tc);
  return 0;
}
