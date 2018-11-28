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

int N; 
double V, X;
double R[128], C[128];
int TestNum;
int main(){
  ios_base::sync_with_stdio(false); 
  int T; scanf("%d", &T);
  while (T--) {
    printf("Case #%d: ", ++TestNum);
    scanf("%d %lf %lf", &N, &V, &X);
    for (int i = 0; i < N; i++) {
      scanf("%lf %lf", R + i, C + i);
    }
    if (N == 1) {
      if (C[0] == X) printf("%.09lf", V / R[0]);
      else printf("IMPOSSIBLE");
    } else {
      if (C[0] == X && C[1] == X) {
        printf("%.09lf", V / (R[0] + R[1]));
      } else if (C[0] == X) {
        printf("%.09lf", V / R[0]);
      } else if (C[1] == X) {
        printf("%.09lf", V / R[1]);
      } else if ((C[0] < X && C[1] < X) || (C[0] > X && C[1] > X)) {
        printf("IMPOSSIBLE");
      } else {
        //double V0 = (V * (C[0] - X)) / ( ( C[1] - X) * C[0] - C[1] * (C[0] - X));
        double V1 = -V / ( (C[1] - X) - (C[0] - X))  * (C[0] - X);
        double V0 = V - V1;
        double ans = max(V0 / R[0], V1 / R[1]);
        printf("%.09lf", ans);
      }
    }
    printf("\n");
  }
}

