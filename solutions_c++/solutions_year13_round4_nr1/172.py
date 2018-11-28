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

template<class T> void print(VC < T > v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]\n";}
template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS all; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) all.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) all.PB(s.substr(p)); return all;}

#define MOD 1000002013LL

LL n, m;
LL cost(LL a, LL b) {
	return (n + n + 1 - (b - a)) * (b - a) / 2;
}

#define MAXN 2100
int a[MAXN];
int b[MAXN];
int x[MAXN];

int pos[MAXN];
LL am[MAXN];
int main() {
	int tc;
	cin >> tc;
	FOR(atc,1,tc+1) {
		LL ov = 0;
		LL av = 0;
		cin >> n >> m;
		REP(i,m) {
			scanf("%d%d%d",&a[i],&b[i],&x[i]);
		}
		set<int> st;
		REP(i,m) st.insert(a[i]),st.insert(b[i]);
		map<int, int> mp;
		VI v(ALL(st));
		REP(i, v.S) mp[v[i]] = i, pos[i] = v[i];
		
		ZERO(am);
		REP(i,m) {
			int p0 = mp[a[i]];
			int p1 = mp[b[i]];
			FOR(j,p0,p1) am[j] += x[i];
		}
		
		
		
		REP(i,m) ov = (ov + (LL)x[i] * (cost(pos[mp[a[i]]], pos[mp[b[i]]]) % MOD)) % MOD;
		
		while (true) {
			bool done = true;
			
			// VC < LL > vv(am, am + v.S + 1);
			// print(vv);
			
			REP(i,v.S) if (am[i]) {
				LL mn = 1LL << 60;
				int pp = i;
				while (am[pp]) {
					mn = min(mn, am[pp]);
					pp++;
				}
				FOR(j,i,pp) am[j] -= mn;
				av = (av + mn * (cost(pos[i], pos[pp]) % MOD)) % MOD;
				done = false;
				break;
			}
			if (done) break;
		}
		
		printf("Case #%d: %lld\n", atc, (ov - av + MOD) % MOD);
	}
	return 0;
}