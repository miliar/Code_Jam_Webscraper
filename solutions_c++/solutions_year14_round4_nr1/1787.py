#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;
int N, X;

int go(const vector<int> & data, vector<bool> & used)
{
  int sol = 0;
  for (int i = 0; i < N; ++i) {
    for (int j = i + 1; j < N; ++j) {
      if (used[i] or used[j]) continue;
      if (data[i] + data[j] <= X) {
        used[i] = used[j] = true;
        sol = max(sol, 1 + go(data, used));
        used[i] = used[j] = false;
      }
    }
  }
  return sol;
}

int main()
{
  int T; cin >> T;
  for (int tc = 1; tc <= T; ++tc) {
    cin >> N >> X;
    vector<int> data(N);
    for (int i = 0; i < N; ++i) cin >> data[i];
    sort(data.begin(), data.end(), greater<int>());
    
    vector<bool> matches(N, false);
    for (int i = 0; i < N; ++i) {
      if (matches[i]) continue;
      for (int j = i + 1; j < N; ++j) {
        if (matches[j]) continue;
        if (data[i] + data[j] <= X) {
          matches[i] = matches[j] = true;
          break;
        }
      }
    }


    int sol = 0;
    for (int i = 0; i < N; ++i) if (matches[i]) sol++;
    sol /= 2;
    for (int i = 0; i < N; ++i) if (not matches[i]) sol++;


    //matches = vector<bool>(N, false);
    //int sol2 = go(data, matches);
    //cerr << sol2 << endl;
    //sol2 += N - (sol2 * 2);
    //if (sol != sol2) {
    //  cout << sol <<  " " << sol2 << endl;
    //  assert(false);
    //}
    cout << "Case #" << tc << ": " << sol << endl;
  }
}
