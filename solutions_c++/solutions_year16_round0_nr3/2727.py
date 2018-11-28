#include <bits/stdc++.h>

#define FR(i,en) for(ll i=0; i<(en); i++)
#define FRR(i,en) for(int i=(en-1); i>=0; i--)
#define FOR(i,st,en) for(int i=(st); i<(en); i++)
#define FORR(i,st,en) for(int i=(en-1); i>=(st); i--)
#define FRI(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

#define ALL(c) (c).begin(), (c).end()
#define SZ(i) i.size()
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define PI 3.1415926535897932384626433832795

typedef long long ll;
using namespace std;

ll stoll(string s, int base) {
	ll l = 0;
	ll b = 1;
	FORR (i,0,s.length()) {
		if ( s[i] == '1' ) l+=b;
		b*=base;
	}
	return l;
}

ll prime(ll num) {
	ll max = sqrt(num);
	for (ll i=2; i<max; i++) {
		if ( num % i == 0 ) return i;
	}
	return -1;
}

int main(int argc, char **argv)
{
	cout << setiosflags(ios::fixed) << setprecision(16);  //correct double
	FILE *istream, *ostream  ;
	if (argc>1) {
		string infilename=argv[1], outfilename=argv[1];
		infilename+=".in";
		outfilename+=".out";
		if((istream = freopen(infilename.c_str(), "r", stdin)) == NULL) cout << "Wrong input file." ,exit(-1);
		if((ostream = freopen(outfilename.c_str(), "w", stdout)) == NULL) cout << "Wrong output file.", exit(-1);
	}
	cout << "Case #1:\n";
	int i=0;
	ll num=32769;
	do {
		string s;
		ll b=num;
		while (b>0)
		{
		  s = b%2 ? "1" + s : "0" + s;
		  b = b/2;
		}
		vector <ll> v;
		bool ok = true;
		for (int j=2; j<11 && ok;j++) {
			ll a=prime(stoll(s,j));
			if ( a == -1) ok = false;
			else v.push_back(a);
		}
		if ( ok ) {
			cout << s << " ";
			FR(j,9) cout << v[j] << " ";
			cout << "\n";
			i++;
		}
		num+=2;
	} while ( i<50 );
}
