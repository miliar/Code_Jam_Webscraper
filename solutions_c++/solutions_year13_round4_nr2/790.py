#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <bitset>
#include <queue>
using namespace std;

//conversion
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//typedef
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long ll;

//container util
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)

//constant
const double EPS = 1e-10;
const int MAXI = 1234567890;

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

ll solveX(int N, int P) {
  if (P == 0) return 0;
  if (P == (1 << N) - 1) return (1 << N) - 1;

  ll t_prize = 0;
  ll t_num = 0;
  ll ans = t_num;
  for (int i = 0; i < N + 1; i++) {
    if (t_prize > P) {
      return ans;
    } else {
      ans = t_num;
      t_prize += (1 << (N - i - 1));
      t_num += (1 << (i + 1));
    }
  }
  return 0;
}

ll solveY(int N, int P) {
  if (P == 0) return 0;
  if (P == (1 << N) - 1) return (1 << N) - 1;

  ll t_prize = 0;
  ll t_num = 0;
  ll ans = t_num;
  for (int i = 0; i < N + 1; i++) {
    if (t_prize > P) {
      return ans;
    } else {
      ans = t_num;
      t_prize += (1 << i);
      t_num += (1 << (N - i - 1));
    }
  }

  return 0;
}

pair<ll, ll> solve(int N, int P) {
  pair<ll, ll> ans;
  ans.first = solveX(N, P - 1);
  ans.second = solveY(N, P - 1);
  return ans;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int N, P;
    cin >> N >> P;
    pair<ll, ll> ans = solve(N, P);
    cout << "Case #" << i + 1 << ": " << ans.first << " " << ans.second << endl;
  }
  return 0;
}
