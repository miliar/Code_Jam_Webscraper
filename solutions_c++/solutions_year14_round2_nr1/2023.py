#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdlib>

#define phb push_back
#define sz(x) int((x).size())
#define all(x) (x).begin(), (x).end()
using namespace std;

int Z, N;
string S[110];
vector< int > v[110];

void read();
void solve(int);

bool check();
void find_ans();

int main() {
  cin >> Z;
  for (int zi = 1; zi <= Z; ++zi)
    read(), solve(zi);

  return 0;
}

void read() {
  cin >> N;
  for (int i = 0; i < N; ++i)
    cin >> S[i];
}

void solve(int zi) {
  cout << "Case #" << zi << ": ";
  if (!check())
    cout << "Fegla Won\n";
  else
    find_ans();
}

bool check() {
  string T[110];

  for (int i = 0; i < N; ++i)
    T[i] = S[i], T[i].resize(int(unique(all(T[i])) - T[i].begin()));

  for (int i = 1; i < N; ++i)
    if (T[0] != T[i])
      return false;
  return true;
}

void find_ans() {
  for (int i = 0; i < N; ++i)
    v[i].clear();

  for (int i = 0; i < N; ++i)
    for (int j = 0, k = 0; j < sz(S[i]); j = k) {
      k = j + 1;
      while (k < sz(S[i]) && S[i][j] == S[i][k])
        ++k;

      v[i].phb(k - j);
    }

  int res = 0;

  for (int i = 0; i < sz(v[0]); ++i) {
    int tmn = 1000;

    for (int j = 0; j < N; ++j) {
      int cnt = 0;

      for (int k = 0; k < N; ++k)
        cnt += abs(v[j][i] - v[k][i]);
      tmn = min(tmn, cnt);
    }

    res += tmn;
  }

  cout << res << "\n";
}
