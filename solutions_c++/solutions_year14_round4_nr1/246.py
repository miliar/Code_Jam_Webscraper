#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <cassert>

using namespace std;

void solve()
{
  int N, X;
  map<int,int> S;

  
  cin >> N >> X;
  for (int i = 0; i < N; i++) {
    int x;
    cin >> x;
    S[x]++;
  }

  int disc = 0;
  
  while (!S.empty()) {
    disc++;

    int x = S.begin()->first;
    S[x]--;
    if (S[x] == 0) {
      S.erase(x);
    }

    if (S.empty()) continue;
    int t = X - x;
    map<int,int>::iterator it = S.lower_bound(t);
    if (it == S.end() || (it != S.begin() && it->first > t))
      it--;

    if (x + it->first <= X) {
      t = it->first;
      S[t]--;
      if (S[t] == 0) {
	S.erase(t);
      }
    }
  }
  cout << disc << endl;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }

  return 0;
}
