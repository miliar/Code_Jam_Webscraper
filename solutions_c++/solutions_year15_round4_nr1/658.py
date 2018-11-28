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
int R, C;
vector<string> grid;
bool isValid(int x, int y) {
  return 0 <= x && x < R && 0 <= y && y < C;
}
map<char, int> M = {{'^', 0}, {'>', 1}, {'v', 2}, {'<', 3}};
bool isWalkOut(int x, int y, int dx, int dy) {
  x += dx, y += dy;
  while (isValid(x, y) && grid[x][y] == '.') {
    x += dx, y += dy;
  }
  //cout << x << ", " << y << endl;
  return !isValid(x, y);
}
int dx[] = {-1, 0, 1, 0};
int dy[] = {0,  1, 0,-1};
string solve() {
  int tot = 0;
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      if (grid[i][j] == '.') continue;
      int idx = M[grid[i][j]];
      //cout << i << ", " << j << ": " << idx << endl;
      if (!isWalkOut(i, j, dx[idx], dy[idx])) continue;
      bool isExistValid = false;
      for (int k = 0; k < 4; k++) {
        if (!isWalkOut(i, j, dx[k], dy[k])) {
          isExistValid = true; 
          break;
        }
      }
      if (isExistValid) tot++;
      else return "IMPOSSIBLE";
    }
  }
  return to_string(tot);
}
int TestNum;
int main(){
  ios_base::sync_with_stdio(false); 
  int T; cin >> T;
  while (T--) {
    cin >> R >> C;
    grid.resize(R);
    for (auto &s: grid) cin >> s;
    cout << "Case #" << ++TestNum << ": " << solve() << endl;
  }
}

