#pragma GCC optimize ("O2")
#include <bits/stdc++.h>
#include <unistd.h>

using namespace std;

#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
#define fst first
#define snd second

template<typename A, typename B>
ostream& operator <<(ostream& s, const pair<A, B>& p)
{
  return s << "(" << p.first << "," << p.second << ")";
}
template<typename T>
ostream& operator <<(ostream& s, const vector<T>& c)
{
  s << "[ ";
  for (auto it : c) s << it << " ";
  s << "]";
  return s;
}

int main()
{
  IOS;
  int T;
  cin >> T;
  string s;
  int k;
  int ALL = '+' + '-';
  for (int tt = 1; tt <= T; ++tt) {
    cin >> s >> k;
    int cnt = 0;
    for (int i = 0; i < (int)s.length() - k + 1; ++i) {
      if (s[i] == '-') {
        for (int j = 0; j < k; ++j) {
          s[i + j] = ALL - s[i + j];
        }
        cnt++;
      }
    }
    bool result = true;
    for (int i = 0; i < (int)s.length(); ++i) {
      if (s[i] == '-') {
        result = false;
        break;
      }
    }
    cout << "Case #" << tt << ": ";
    if (result)
      cout << cnt << endl;
    else
      cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}
