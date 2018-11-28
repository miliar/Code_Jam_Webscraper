#include <iostream>
#include <sstream>
using namespace std;

stringstream ss;

typedef long long ll;

ll gcd(ll a, ll b) {
	if ( b == 0 ) return a;
	return gcd(b,a%b);
}

bool isPowOf2(ll z) {
	return ((z&(z-1))==0);
}

void getnum(ll &a, const char *t) {
	ll ret = 0;
	char c;
	do {
		c = *(t++);
		if ( c >= '0' && c <= '9' ) {
			ret *= 10;
			ret += (c-'0');
		}
	} while ( c >= '0' && c <= '9' );
	a = ret;
}

void testcase() {
	char temp[20];
	ll p, q;
	cin.getline(temp,20,'/');
	getnum(p,temp);
	cin.getline(temp,20,'\n');
	getnum(q,temp);
	ll g = gcd(p,q);
	p /= g;
	q /= g;
  if ( !isPowOf2(q) ) {
		ss << "impossible";
	} else {
		int z = 0;
		for ( int i = q ; i > p ; i/=2 ) {
			z++;
		}
		ss << z;
	}
}

int main() {
	int t;
	cin >> t;
	cin.ignore();
	for ( int i = 0 ; i < t ; i++ ) {
		ss << "Case #" << (i+1) << ": ";
		testcase();
		ss << endl;
	}
	cout << ss.str();
	return 0;
}
