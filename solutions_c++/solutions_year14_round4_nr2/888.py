#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <deque>
#include <algorithm>

using namespace std;

struct Solve
{
  int N;
  vector<int> A;

  map<vector<int>, int> ans;

  Solve()
  {
  }

  void load()
  {
    cin >> N;
    for (int i = 0; i < N; i++) {
      int x;
      cin >> x;
      A.push_back(x);
    }

  }

  int solve()
  {
    vector<vector<int> > q;
    ans[A] = 1;
    q.push_back(A);

    for (int answer = 0; ; answer++) {
      vector<vector<int> > newq;
      for (auto qi = q.begin(); qi != q.end(); qi++) {
        if (check(*qi)) return answer;
        for (int i = 0; i < N - 1; i++) {
          vector<int> x = *qi;
          swap(x[i], x[i+1]);
          auto f = ans.find(x);
          if (f == ans.end()) {
            newq.push_back(x);
            ans[x] = 1;
          }
        }
      }
      q.swap(newq);
    }
    return -1;
  }

  bool check(const vector<int>& pm) {
    int i;
    for (i = 1; i < N; i++) {
      if (pm[i-1] > pm[i]) break;
    }
    for (; i < N; i++) {
      if (pm[i-1] < pm[i]) return false;
    }
#if 0
    for (i = 0; i < N; i++) {
      cout << pm[i] << " ";
    }
    cout << endl;
#endif
    return true;
  }

};


int main()
{
  int T;

  cin >> T;

  for (int cas = 1; cas <= T; cas++) {
    Solve solve;
    solve.load();
    int n = solve.solve();
    cout << "Case #" << cas << ": " << n << endl;
  }

  return 0;
}
