#include <algorithm>
#include <bitset>
#include <cctype>
#include <cerrno>
#include <clocale>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cwchar>
#include <cwctype>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <ostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,m,n) for(long long i = m; i < n; ++i)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define eps 1e-7
#define FOR(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef vector<vll> vvll;
typedef vector<vii> vvii;

int main() {
  ios_base::sync_with_stdio(false);
  ofstream fout("submission.out");
  int T;
  cin >> T;
  for (int TAT = 1; TAT < T + 1; ++TAT) {
    ll A;
    int N;
    cin >> A >> N;
    vll st;
    rep(i,0,N)
    {
      ll tem;
      cin >> tem;
      st.pb(tem);
    }
    sort(all(st));
    ll res = 1e18, cur = 0;
    if (A == 1) {
      res = N;
    } else {
      for (ll i = 0; i < N; ++i) {
        if (A > st[i]) {
          A += st[i];
          if (i == N - 1)
            res = min(res, cur);
        } else {
          ll plu = 0;
          while (A <= st[i]) {
            A = 2 * A - 1;
            ++plu;
          }
          A += st[i];
          if (plu > N - i) {
            res = min(res, cur + N - i);
            break;
          }
          res = min(res, cur + N - i);
          cur += plu;
        }
      }
    }
    fout << "Case #" << TAT << ": " << res << endl;
  }
  return 0;
}
