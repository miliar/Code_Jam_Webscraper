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

map<string, int> dict;
int L = 1;
vector<int> split(string line) {
  stringstream ss(line);
  vector<int> words;
  string w;
  while (ss >> w) {
    if (!dict.count(w)) dict[w] = L++;
    words.push_back(dict[w]);
  }
  return words;
}
vector<vector<int> > sens;
bool isIn[2][1023*1027];
int solve() {
  dict.clear();
  L = 0;
  int ans = 0x3f3f3f3f;
  int N; cin >> N;
  sens.clear();

  string tmp; getline(cin, tmp);
  for (int i = 0; i < N; i++) {
    getline(cin, tmp);
    sens.push_back(split(tmp));
  }
  for (int mask = 0; mask < (1 << N); mask++) {
    if ((mask & 1) != 0) continue;
    if ((mask & 2) == 0) continue;
    memset(isIn[0], false, L);
    memset(isIn[1], false, L);
    for (int i = 0; i < N; i++) {
      int idx = ((mask & (1 << i)) != 0)? 0 : 1;
      for (auto t: sens[i]) isIn[idx][t] = true;
    }
    int tot = 0;
    for (int i = 0; i < L; i++) {
      if (isIn[0][i] && isIn[1][i]) tot++;
    }
    //cout << tot << endl;
    ans = min(ans, tot);
  }
  return ans;
}
int TestNum;
int main(){
  ios_base::sync_with_stdio(false); 
  int T; cin >> T;
  while (T--) {
    cout << "Case #" << ++TestNum << ": " << solve() << endl;
  }
}

