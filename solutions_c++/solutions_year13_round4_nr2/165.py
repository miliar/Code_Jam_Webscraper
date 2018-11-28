#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
//#include <emmintrin.h>

using namespace std;

#define FORE(it,c)  for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define ZERO(m)    memset(m,0,sizeof(m))
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S          size()
#define LL          long long
#define ULL        unsigned long long
#define LD          long double
#define MP          make_pair
#define X          first
#define Y          second
#define VC          vector
#define PII        pair <int, int>
#define VI          VC < int >
#define VVI        VC < VI >
#define VD          VC < double >
#define VVD        VC < VD >
#define VS          VC < string >
#define DB(a)      cerr << #a << ": " << (a) << endl;

template<class T> void print(VC < T > v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]n";}
template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS all; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) all.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) all.PB(s.substr(p)); return all;}


PII bf(int n, int p) {
	LL t = 1 << n;
	VI order;
	REP(i, t) order.PB(i);
	int b1 = t - 1;
	int b2 = 0;
	do {
		VVI v, nv;
		v.PB(order);
		while (v.S != t) {
			nv.clear();
			
			REP(i, v.S) {
				VI v1,v2;
				for (int j = 0; j < v[i].S; j += 2) {
					v1.PB(min(v[i][j],v[i][j+1]));
					v2.PB(max(v[i][j],v[i][j+1]));
				}
				nv.PB(v1);
				nv.PB(v2);
			}
			v = nv;
		}
		FOR(i, p, t) b1 = min(b1, v[i][0]-1);
		REP(i, p) b2 = max(b2, v[i][0]);
	} while (next_permutation(ALL(order)));
	return MP(b1,b2);
}

int main() {
	// FOR(i, 1, 9) {
		// PII p = bf(3, i);
		// cout << p.X << ' ' << p.Y << endl;
	// }
	
	int tc;
	cin >> tc;
	
	FOR(atc,1,tc+1) {
		LL n, p;
		LL t;
		cin >> n >> p;
		t = 1LL << n;
		
		LL r0 = -1, r1 = -1;
		REP(i, n) if (p > t - (t >> i)) r0 = (1LL << (i+1)) - 2;
		REP(i, n+1) if (p >= (t >> i)) {
			r1 = t - ((1LL << i));
			break;
		}
		
		if (p == t) r0 = t-1;
		
		printf("Case #%d: %lld %lld\n", atc, r0, r1);
	}
}