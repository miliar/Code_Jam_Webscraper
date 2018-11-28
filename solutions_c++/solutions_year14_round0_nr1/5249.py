#include <bits/stdc++.h>

#define each(i, c) for (auto& i : c)
#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    const int N = 4;
    int ans;
    set<int> s[2];
    for (int k = 0; k < 2; ++k) {
      cin >> ans;
      for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
          int n;
          cin >> n;
          if (i == ans - 1) {
            s[k].insert(n);
          }
        }
      }
    }
    vector<int> v;
    for (int i = 1; i <= 16; ++i) {
      if (s[0].count(i) && s[1].count(i)) v.push_back(i);
    }
    static int cnt = 0;
    if (v.size() == 0) cout << "Case #" << ++cnt << ": Volunteer cheated!" << endl;
    if (v.size() == 1) cout << "Case #" << ++cnt << ": " << v[0] << endl;
    if (v.size() >= 2) cout << "Case #" << ++cnt << ": Bad magician!" << endl;
  }
  return 0;
}
