#include <iostream>
#include <map>
#include <algorithm>
using namespace std;
map<tuple<int, int, int>, string> res[3];
const string IMPOSSIBLE = "IMPOSSIBLE";
pair<int, int> winning(int out) {
  if (out == 0) return {0,2};
  else if (out == 1) return {0,1};
  else return {1,2};
}
int who_loses_to(int x) {
  if (x == 0) return 2;
  if (x == 1) return 0;
  if (x == 2) return 1;
}
using Triple = tuple<int, int, int>;
Triple sum(const Triple &a, const Triple &b) {
  return make_tuple(get<0>(a)+get<0>(b), get<1>(a)+get<1>(b), get<2>(a)+get<2>(b));
}
Triple req[13][3];
string c[] = {"R", "P", "S"};
string f(int n, int o) {
  if (n == 0) return c[o];
  string a = f(n-1, o);
  string b = f(n-1, who_loses_to(o));
  return (a < b ? a+b : b+a);
}
int main() {
  // ios_base::sync_with_stdio(0);
  req[0][0] = make_tuple(1, 0, 0);
  req[0][1] = make_tuple(0, 1, 0);
  req[0][2] = make_tuple(0, 0, 1);
  for (int n=1; n<=12; n++)
    for (int i=0; i<3; i++)
      req[n][i] = sum(req[n-1][i], req[n-1][who_loses_to(i)]);
  int T, N, R, P, S;
  cin >> T;
  for (int t=1; t<=T; t++) {
    cout << "Case #" << t << ": ";
    cin >> N >> R >> P >> S;
    Triple tr = make_tuple(R, P, S);
    string ans = "Z";
    for (int i=0; i<3; i++)
      if (req[N][i] == tr)
        ans = min(ans, f(N, i));
    if (ans == "Z") ans = IMPOSSIBLE;
    cout << ans << "\n";
  }
  return 0;
}
