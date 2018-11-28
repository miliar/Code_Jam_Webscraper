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
//#include <tuple>
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
const long long MOD = 1e9 + 7;
const long long N = 1e5 + 10;

int main() {
  ios_base::sync_with_stdio(false);
  ifstream fin("submission.in");
  ofstream fout("submission.out");
  int T;
  fin >> T;
  for (int tt = 1; tt <= T; ++tt) {
    int N;
    fin >> N;
    vector<double> naomi(N), ken(N);
    rep(i,0,N)
    {
      fin >> naomi[i];
    }
    rep(i,0,N)
    {
      fin >> ken[i];
    }
    sort(all(naomi), greater<double>());
    sort(all(ken), greater<double>());
    int y = 0;
    for (int j = 0, i = 0; j < N; ++j) {
      if (naomi[i] > ken[j]) {
        ++y;
        ++i;
      }
    }
    int z = 0;
    for (int i = 0, j = 0; i < N; ++i) {
      if (naomi[i] > ken[j]) {
        ++z;
      } else {
        ++j;
      }
    }
    fout << "Case #" << tt << ": " << y << ' ' << z << endl;
  }
  return 0;
}
