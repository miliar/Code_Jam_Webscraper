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
    set<int> st0, st1;
    int ans;
    fin >> ans;
    vector<vector<int>> stt0(4, vector<int>(4));
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        fin >> stt0[i][j];
        if (i + 1 == ans) {
          st0.insert(stt0[i][j]);
        }
      }
    }
    fin >> ans;
    vector<vector<int>> stt1(4, vector<int>(4));
    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
        fin >> stt1[i][j];
        if (i + 1 == ans) {
          st1.insert(stt1[i][j]);
        }
      }
    }
    set<int> st;
    set_intersection(st0.begin(), st0.end(), st1.begin(), st1.end(),
                     inserter(st, st.begin()));
    if (st.size() == 1) {
      fout << "Case #" << tt << ": " << *st.begin() << endl;
    } else if (st.size() > 1) {
      fout << "Case #" << tt << ": " << "Bad magician!" << endl;
    } else {
      fout << "Case #" << tt << ": " << "Volunteer cheated!" << endl;
    }
  }
  return 0;
}
