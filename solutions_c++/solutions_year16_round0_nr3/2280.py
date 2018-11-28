#include <cassert>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <numeric>
#include <bitset>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <functional>
#include <cstring>
#include <ctime>
#include <memory.h>

#define y1 AAA_BBB
#define y0 AAA_AAA

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define for1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef vector<int> vi;
typedef vector<i64> vi64;
typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef vector<vi64> vvi64;

template <class T> T inline sqr(T x) {
    return x * x;
}

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;

const int N = 32;
int J = 500;

const int mxprime = 1e6;//>=100
vector<int> primes; bitset<mxprime/2> is_prime;
void init_primes(int n = mxprime) {
    is_prime.set(); is_prime.reset(0); primes.pb(2);
    int bi = sqrt(n), bj = (n-1)/2;//i21=2*i+1,sj=2*i*(i+1
    for(int i=1,i21=3,sj=4,dsj=8;i21<bi;i+=1,i21+=2,sj+=dsj,dsj+=4)
        if( is_prime.test(i) ) for(int j=sj;j<bj;j+=i21)
            is_prime.reset(j);
    for(int i = 1; i < bj; ++i) if( is_prime.test(i) )
        primes.pb(i*2+1);
}
bool check_prime(int x) {
    if( primes.empty() ) init_primes();
    assert( x >= 0 && x < mxprime );
    return (x&1) ? is_prime[(x-1)/2] : (x==2);
}
bool isprime(__int128 n, bool check_little = false) {
    if( n < 2 ) return false;
    if( n < mxprime ) return check_prime(n);
    if( check_little ) for(int x: primes) if( x <= 800 ) {
        if( n % x == 0 ) return false;
    } else break;
    //for(int i: {2,3,5,7,11,13}) if( miller(n, i) ) return false;
    return true;
}
int main()
{
#ifdef HOME
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	init_primes();
	cout << "Case #1:" << endl;
    ios::sync_with_stdio(false);
    forn (_msk, (1 << (N-2))) {
		i64 msk = (1LL << (N - 1)) + 1 + _msk * 2LL;
		bool ok = 1;
		vector<__int128> el;
		for (int m = 2; m <= 10; m++) {
			__int128 x = 0;
			ford(t, N){
				x = x * m + ((msk >> t) & 1);
			}
			if (isprime(x, 1)) {
				ok = 0;
				break;
			}
			el.pb(x);
		}
		if (ok) {
			J--;
			ford (i, N)
				cout << ((msk >> i) & 1); 
			
			for (auto x: el) {
				bool ok = 0;
				for (i64 i = 2; i * i <= x; i++)
					if (x % i == 0) {
						ok = 1;
						cout << " " << i;
						break;
					}	
				//if (!ok) cerr << msk << " " << x << endl;	
				assert(ok);
			}
			cout << endl;
			if (!J) break;
		}
	}
    return 0;
}
