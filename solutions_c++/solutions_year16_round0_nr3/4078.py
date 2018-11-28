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
#include <boost/multiprecision/gmp.hpp>
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

using bi = boost::multiprecision::mpz_int;

bi gcd(bi a, bi b) {
	if(b == 0) return a;
	return gcd(b, a % b);
}
bi abs2(bi x) {
	return x < 0 ? -x : x;
}
bi pollard_rho(bi r) {
	boost::multiprecision::mpz_int x = 2, y = 2, d = 1;
	for(ll w = 800; d == 1 && w < 1600; ++w) {
		x = (x * x + 1) % r;
		y = (y * y + 1) % r;
		y = (y * y + 1) % r;
		d = gcd(abs2(x-y), r);
	}
	if(d == r) return 0;
	assert(r % d == 0);
	return d;
}

int main() {
	ios::sync_with_stdio(false);
	int T; cin >> T;
	assert(T == 1);
	ll N, J;
	cin >> N >> J;
	ll cur = (1LL << (N-1)) + 1;
	ll cnt = 0;
	cout << "Case #1:" << endl;
	while(cnt != J) {
		//cerr << "cur: " << cur << endl;
		ll c = cur;
		string r;
		vector<bi> factors;
		FOR(i, 2, 10+1) {
			bi res = 0;
			for(ll j = 31; j >= 1; --j) {
				res = res * i;
				if(cur & (1 << j)) {
					res = res + i;
				}
			}
			if(cur & 1) res += 1;
			//cerr << "Testing " << (ll) res << endl;
			bi foo = pollard_rho(res);
			if(foo <= 1) goto fail;
			assert((res % foo) == 0);
			//cerr << "Found factor " << foo << endl;
			factors.pb(foo);
		}
		while(c) {
			if(c & 1) r = "1" + r;
			else r = "0" + r;
			c >>= 1;
		}
		cout << r;
		{
			//cerr << endl << r << endl;
			FOR(i, 2, 10+1) {
				bi foo = 0;
				for(auto w : r) {
					foo = foo * i + (w == '1');
					//cerr << "Adding " << w << endl;
				}
				//cerr << "foo is: " << (ll) foo << endl;
				assert(factors[i-2]!= 1 && factors[i-2] != foo);
				assert(foo % factors[i-2] == 0);
			}
		}
		assert(factors.size() == 9);
		assert(r.size() == N);
		for(auto c : factors)
			cout << " " << c;
		cout << endl;
		cnt++;
fail: ;
		cur += 2;
	}
}
