//Clibrary:
#include<cassert>
#include<cctype>
#include<cerrno>
//#include<cfenv>
#include<cfloat>
//#include<cinttypes>
#include<ciso646>
#include<climits>
#include<clocale>
#include<cmath>
#include<csetjmp>
#include<csignal>
#include<cstdarg>
//#include<cstdbool>
#include<cstddef>
//#include<cstdint>
#include<cstdio>
#include<cstdlib>
#include<cstring>
//#include<ctgmath>
#include<ctime>
//#include<cuchar>
#include<cwchar>
#include<cwctype>
//Containers:
//#include<array>
#include<bitset>
#include<deque>
//#include<forward_list>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
//#include<unordered_map>
//#include<unordered_set>
#include<vector>
//Input/Output:
#include<fstream>
#include<iomanip>
#include<ios>
#include<iosfwd>
#include<iostream>
#include<istream>
#include<ostream>
#include<sstream>
#include<streambuf>
//Other:
#include<algorithm>
//#include<chrono>
//#include<codecvt>
#include<complex>
#include<exception>
#include<functional>
//#include<initializer_list>
#include<iterator>
#include<limits>
#include<locale>
#include<memory>
#include<new>
#include<numeric>
//#include<random>
//#include<ratio>
//#include<regex>
#include<stdexcept>
#include<string>
//#include<system_error>
//#include<tuple>
//#include<typeindex>
#include<typeinfo>
//#include<type_traits>
#include<utility>
#include<valarray>
using namespace std;

typedef long long i64;
typedef unsigned long long u64;

typedef long long               ll;
typedef long double             ld;
typedef vector<int>             vi;
typedef vector<vi>              vvi;
typedef pair<int, int>          pii;
typedef vector<pii>             vii; // vector of integer pairs
typedef set<int>                si;
typedef map<string, int>        msi;

const double PI = acos(-1);

/*
 * __builtin_ffs  __builtin_clz  __builtin_ctz __builtin_popcount  __builtin_parity
 * sizeof CLOCKS_PER_SEC
 * (1 << (31 - __builtin_clz(100) ) == 64;
 * decltype // deprecated
 */
vector<string> words = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

double EPS = 1e-6;
double a[128][128];
double ans[128];
bool l[128];
string solve(string S) {
  memset(a, 0, sizeof(a));
  memset(ans, 0, sizeof(ans));
  memset(l, 0, sizeof(l));
  for (size_t i = 0; i < 10; i++) {
    for (char c: words[i]) {
      a[c-'A'][i] += 1;
    }
  }
  for (char c: S) {
    a[c-'A'][10] += 1;
  }
  int res = 0, r = 0;
  for (int i = 0; i < 26; i++) {
    for (int j = r; j < 26; j++) {
      if (fabs(a[j][i]) > EPS ) {
        for (int k = i; k <= 10; k++) {
          swap(a[j][k], a[r][k]);
        }
        break;
      }
    }
    if (fabs(a[r][i]) < EPS) {
      ++res;
      continue;
    }
    for (int j = 0; j < 26; j++) {
      if (j != r && fabs(a[j][i]) > EPS) {
        double tmp = a[j][i] / a[r][i];
        for (int k = i; k <= 10; k++) {
          a[j][k] -= tmp * a[r][k];
        }
      }
    }
    l[i] = true, ++r;
  }
  for (int i = 0; i < 26; ++i) {
    if (l[i]) {
      for (int j = 0; j < 10; j++) {
        if (fabs(a[j][i]) > EPS) ans[i] = a[j][10] / a[j][i];
      }
    }
  }
  string result;
  for (int i = 0; i < 10; i++) {
    int t = ans[i] + 0.5;
    //cout << i << ": " << t << endl;
    while (t--) result += (char)(i + '0');
  }
  return result;
}

int TestNum;
int main(){
  ios_base::sync_with_stdio(false); 
  int T; cin >> T;
  while (T--) {
    string S; cin >> S;
    cout << "Case #" << ++TestNum << ": " << solve(S) << endl;
  }
}

