/// Header - C++ 11                             
/* ============== Makefile =====================  ======= ~/.vimrc ========
   CXXFLAGS += -O0 -Wall -Wextra -std=gnu++0x -g  set sw=4 ts=4 ru nu ai si
   debug: -ftrapv -D_GLIBCXX_DEBUG                ab #d #define
          -D_GLIBCXX_EXTERN_TEMPLATE=0            syn on
          -fsanitize=address
   (alternativ z.B. __gnu_debug::string)
   ============== python =================
   from math import *                                                        **/
#include <bits/stdc++.h>                 // [PRIMES]               1777 ~2^10.80
using namespace std;                     //                       10333 ~2^13.33
using ll = long long;                    // seq 1 128 | factor   100333 ~2^16.61
using vl = vector<ll>;                   //   | grep -v ' .* '  1300111 ~2^20.31
using vvl = vector<vl>;                  //                    10300777 ~2^23.30
using pll = pair<ll,ll>;                 //                   100400999 ~2^26.58
using vb = vector<bool>;                 //                  1300400999 ~2^30.28
const ll oo = 0x3f3f3f3f3f3f3f3fLL;      //                 10200500333 ~2^33.25
const double eps = 1e-9;                 //                100200400777 ~2^36.54
#define sz(c) ll((c).size())             //               1200300700111 ~2^40.13
#define all(c) begin(c),end(c)           //              10200300500777 ~2^43.21
#define mp make_pair                     //             100200300400777 ~2^46.51
#define mt make_tuple                    //            1200300400600999 ~2^50.09
#define pb push_back                     //           10200300400600111 ~2^53.18
#define eb emplace_back                  //          100200300400600333 ~2^56.48
#define xx first                         //         1200300400500800999 ~2^60.06
#define yy second                       
#define has(c,i) ((c).find(i) != end(c))
#define FOR(i,a,b) for (int i=(a); i<(b); i++)       
#define FORD(i,a,b) for (int i=int(b)-1; i>=(a); i--)
/// ({ ... }) avoids some problems: http://kernelnewbies.org/FAQ/DoWhile0
/// In non-contest code it is probably better to use: do { ... } while(0)
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })
int main() {
	ios::sync_with_stdio(false);
	int T; cin >> T;
	FOR(TC, 1, T+1) {
		ll N; cin >> N;
		cout << "Case #" << TC << ": ";
		if(N == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		ll cnt = 0;
		set<int> seen;
		do {
			cnt++;
			ll NN = N * cnt;
			while(NN) {
				seen.insert(NN % 10);
				NN /= 10;
			}
		} while(seen.size() != 10);
		cout << cnt * N << endl;
	}
}
