#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
const int Nmax = 1333;

int n;
int P[Nmax];

int get_under(int x) {
  int ret = 0;
  for (int i = 0; i < n && x < P[i]; i++)
    ret += (P[i] - 1) / x;
  return ret;
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> n;
    for (int i = 0; i < n; i++)
    {
      cin >> P[i];
    }
    sort(P, P+n, greater<int>());
    int ans = P[0];
    for (int x = 1; x < P[0]; x++) {
      int m = x + get_under(x);
      if (m < ans)
        ans = m;
    }
    cout << "Case #" << t << ": " << ans << '\n';
  }
  
  return 0;
}
