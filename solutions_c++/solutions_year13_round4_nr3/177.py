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

int a[40];
int b[40];
int v[40];
int u;
int n;

void go(int l = 0) {
	bool ok = (l == 0 || a[l-1] == 1);
	REP(i, l-1) if (v[i] < v[l-1] && a[l-1] == a[i]+1) ok = true;
	if (!ok) return;
	REP(i, l-1) if (v[i] < v[l-1] && a[l-1] < a[i]+1) return;
	REP(i, l-1) if (v[i] > v[l-1] && b[i] < b[l-1]+1) return;
	
	// cout << l << ' ' << ok << ' ' << v[0] << ' ' << v[1] << ' ' << v[2] << endl;
	if (l == n) {
		REP(i, n) {
			if (b[i] == 1) continue;
			bool ok = false;
			FOR(j, i+1, n) if (v[i] > v[j] && b[i] == b[j]+1) ok = true;
			if (!ok) return;
		}
		throw 1;
	}
	REP(i,n) if (!(u & (1 << i))) {
		u ^= 1 << i;
		v[l] = i+1;
		go(l+1);
		u ^= 1 << i;
		v[l] = 0;
	}
}

int main() {
	int tc;
	cin >> tc;
	FOR(atc,1,tc+1) {
		cin >> n;
		REP(i,n) cin >> a[i];
		REP(i,n) cin >> b[i];
		u = 0;
		try {
			go(0);
		} catch (int e) {}
		printf("Case #%d:", atc);
		REP(i,n) cout << " " << v[i];
		cout << endl;
	}
	return 0;
}