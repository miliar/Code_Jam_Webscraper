#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <functional>
#include <numeric>
#include <cmath>
#include <string>
#include <cctype>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

#define ALL(x) ((x).begin()),((x).end())
#if __cplusplus >= 201103L
#define FOR(i,c) for(auto i=c.begin(); i!=c.end(); ++i)
#define REP(i,n) for(decltype(n) i=0; i<(n); ++i)
#else
#define FOR(i,c) for(typeof(c.begin()) i=c.begin(); i!=c.end(); ++i)
#define REP(i,n) for(typeof(n) i=0; i<(n); ++i)
#endif

const int infty = 999999999;

const int dx[8] = {  1, 0,-1, 0, 1,-1,-1, 1 };
const int dy[8] = {  0, 1, 0,-1, 1, 1,-1,-1 };

template<class T> void minimize(T &a, T b) { a = min(a,b); }
template<class T> void maximize(T &a, T b) { a = max(a,b); }

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) fprintf(stderr,__VA_ARGS__)
#else
#define debug(...)
#endif

const int maxdigits = 100;
// keep maxdigits < maxint/100 for correct functioning of *(bignum,bignum)

template<int B> class bignum;

template<int B> bignum<B> operator -(bignum<B> a);
template<int B> bignum<B> abs(bignum<B> a);

// Base B bignumber:
template<int B> class bignum {
public:
	vector<unsigned int> d;
	int sign; // -1: negative, 1: positive, 0: zero

	bignum(): d(maxdigits,0), sign(0) {}
	bignum(long long n): d(maxdigits,0), sign(0) {
		if ( n==0 ) return;
		sign = 1;
		if ( n<0 ) {
			sign = -1;
			n = -n;
		}
		for(size_t i=0; i<d.size(); ++i) { d[i] = n%B; n /= B; }
	}

	bignum(string str): d(maxdigits,0), sign(1) { // no error check!
		while ( str[0]=='-' ) {
			sign *= -1;
			str.erase(0,1);
		}
		while ( str.length()>1 && str[0]=='0' ) str.erase(0,1);
		if ( str[0]=='0' ) {
			sign = 0;
			return;
		}
		size_t n = str.length();
		for(int i=int(n)-1; i>=0; --i) d[n-1-i] = str[i]-'0';
	}

	operator long long() { // no overflow check!
		long long res = 0, base = 1;
		for(size_t i=0; i<d.size(); ++i) {
			res += d[i]*base;
			base *= B;
		}
		return sign*res;
	}

	size_t ndigits() const { // does not assume 'sign' variable correct
		int i;
		for(i=int(d.size())-1; (i>=0 && d[i]==0); --i);
		return i+1;
	}

	string str() const {
		if ( sign==0 ) return string("0");
		string res;
		if ( sign==-1 ) res += '-';
		for(int i=int(ndigits())-1; i>=0; --i) res += '0'+d[i];
		return res;
	}

	// shifts digits ndig to the left (like << operator but now base B)
	bignum& shl(int ndig) {
		int i;
		for(i=int(d.size())-1; i>=ndig; --i) d[i] = d[i-ndig];
		for(; i>=0; --i) d[i] = 0;
		return *this;
	}

	// equivalent shift to right as above
	bignum& shr(int ndig) {
		int i;
		for(i=0; i<int(d.size())-ndig; ++i) d[i] = d[i+ndig];
		for(; i<int(d.size()); ++i) d[i] = 0;
		return *this;
	}

	bignum& operator +=(const bignum& a) {
		if ( a.sign==0 ) return *this;
		if ( sign==0 ) return *this = a;
		if ( a.sign!=sign ) { // differing signs
			return *this -= -a;
		}

		int carry = 0;
		for(size_t i=0; i<d.size(); ++i) {
			d[i] += a.d[i] + carry;
			carry = d[i] / B;
			d[i] %= B;
		}
		return *this;
	}

	bignum& operator -=(const bignum& a) {
		if ( a.sign==0 ) return *this;
		if ( sign==0 ) return *this = -a;
		if ( a.sign!=sign ) { // differing signs
			return *this += -a;
		}
		if ( abs(*this)<abs(a) ) { // sign change
			bignum tmp = abs(a) -= abs(*this);
			tmp.sign = -sign;
			if ( tmp.ndigits()==0 ) tmp.sign = 0;
			return *this = tmp;
		}

		int carry = 0;
		for(size_t i=0; i<d.size(); ++i) {
			d[i] += B - a.d[i] - carry;
			carry = d[i]>=B ? 0 : 1;
			d[i] %= B;
		}
		if ( ndigits()==0 ) sign = 0;
		return *this;
	}

	bignum& operator *=(const bignum& a) {
		if ( sign==0 || a.sign==0 ) {
			return *this = bignum(0);
		}

		bignum res;
		int carry = 0;

		for(size_t i=0; i<d.size(); ++i) {
			res.d[i] = carry;
			for(size_t j=0; j<=i; ++j) res.d[i] += d[j] * a.d[i-j];
			carry = res.d[i] / B;
			res.d[i] %= B;
		}
		res.sign = sign*a.sign;
		return *this = res;
	}

	int operator ==(const bignum &a) const {
		if ( sign!=a.sign ) return 0;
		for(size_t i=0; i<d.size(); ++i) if ( d[i]!=a.d[i] ) return 0;
		return 1;
	}

	int operator <(const bignum &a) const {
		if ( sign!=a.sign ) return sign<a.sign;
		if ( sign==0 ) return 0;
		size_t i;
		for(i=d.size()-1; (i>0 && d[i]==a.d[i]); --i);
		return (sign==1) ? (d[i] < a.d[i]) : (d[i] > a.d[i]);
	}

	int operator <=(const bignum &a) const {
		if ( sign!=a.sign ) return sign<=a.sign;
		if ( sign==0 ) return 1;
		size_t i;
		for(i=d.size()-1; (i>0 && d[i]==a.d[i]); --i);
		return (sign==1) ? (d[i] <= a.d[i]) : (d[i] >= a.d[i]);
	}

	int divide(bignum div, bignum &quotient, bignum &remainder) {
		bignum tmp;
		int nshift;

		if ( div.sign==0 ) {
			cerr << "Bignum error: division by zero!" << endl;
			return 1;
		}

		quotient  = bignum(0);
		remainder = abs(*this);

		tmp = abs(div);
		nshift = 0;
		while ( tmp<=remainder && tmp.ndigits()<d.size() ) {
			tmp.shl(1);
			nshift++;
		}
		tmp.shr(1);
		nshift--;

		while ( !(remainder<abs(div)) ) {
			while ( tmp<=remainder ) {
				quotient.d[nshift]++;
				remainder -= tmp;
			}
			tmp.shr(1);
			nshift--;
		}

		quotient.sign  = sign*div.sign;
		remainder.sign = sign;
		if (  quotient.ndigits()==0 )  quotient.sign = 0;
		if ( remainder.ndigits()==0 ) remainder.sign = 0;
		return 0;
	}

	bignum& operator /=(const bignum& a) {
		bignum quot, rem;
		divide(a,quot,rem);
		return *this = quot;
	}

	bignum& operator %=(const bignum& a) {
		bignum quot, rem;
		divide(a,quot,rem);
		return *this = rem;
	}

};

template<int B> bignum<B> operator -(bignum<B> a)
{
	if ( a.sign==0 ) return a;
	a.sign *= -1;
	return a;
}

template<int B> bignum<B> abs(bignum<B> a)
{
	if ( a.sign==-1 ) a.sign = 1;
	return a;
}

template<int B> bignum<B> operator +(bignum<B> a, bignum<B> b) { return a += b; }
template<int B> bignum<B> operator -(bignum<B> a, bignum<B> b) { return a -= b; }
template<int B> bignum<B> operator *(bignum<B> a, bignum<B> b) { return a *= b; }
template<int B> bignum<B> operator /(bignum<B> a, bignum<B> b) { return a /= b; }
template<int B> bignum<B> operator %(bignum<B> a, bignum<B> b) { return a %= b; }

template<int B> ostream &operator <<(ostream &s, const bignum<B> &a)
{
	s << a.str();
	return s;
}

template<int B> istream &operator >>(istream &s, bignum<B> &a)
{
	string str;
	s >> str;
	a = bignum<B>(str);
	return s;
}

VI primes;

template<int B> int cert(bignum<B> n)
{
	for(size_t i=0; i<primes.size() && primes[i]<n; i++)
		if ( n%primes[i]==0 ) return primes[i];

	return 0;
}

int main()
{

	primes.push_back(2);
	for(int i=3; primes.size()<5000000; i+=2) {
		int j=0;
		for(j=0; primes[j]*primes[j]<=i; j++) if ( i%primes[j]==0 ) break;
		if ( primes[j]*primes[j]>i ) primes.push_back(i);
	}

	cerr << "last prime: " << primes.back() << endl;

	cout << "Case #1:\n";

	int nfound = 0;
	int l = 16;
	for(LL i=1<<(l-2); i<(1<<(l-1)); i++) {
		LL n = (i<<1) + 1;
		string s;
		while ( n!=0 ) { s += '0'+(n%2); n>>=1; }
		VI certs;
		int c;
		bignum<2> m2(s); if ( (c=cert(m2)) ) certs.push_back(c); else continue;
		bignum<3> m3(s); if ( (c=cert(m3)) ) certs.push_back(c); else continue;
		bignum<4> m4(s); if ( (c=cert(m4)) ) certs.push_back(c); else continue;
		bignum<5> m5(s); if ( (c=cert(m5)) ) certs.push_back(c); else continue;
		bignum<6> m6(s); if ( (c=cert(m6)) ) certs.push_back(c); else continue;
		bignum<7> m7(s); if ( (c=cert(m7)) ) certs.push_back(c); else continue;
		bignum<8> m8(s); if ( (c=cert(m8)) ) certs.push_back(c); else continue;
		bignum<9> m9(s); if ( (c=cert(m9)) ) certs.push_back(c); else continue;
		bignum<10> m10(s); if ( (c=cert(m10)) ) certs.push_back(c); else continue;

		cout << s;
		for(size_t i=0; i<certs.size(); i++) cout << ' ' << certs[i];
		cout << endl;

		if ( ++nfound>=50 ) break;

	}

	return 0;
}
