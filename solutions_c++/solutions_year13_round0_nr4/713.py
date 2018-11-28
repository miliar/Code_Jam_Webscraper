#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
#include <cstring>
using namespace std;


#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair


typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;

const int MAXN = 200 + 10;

int n;
vector<int> chest[MAXN];

int have[MAXN], key[MAXN];


int memo[1<<20];
int pick[1<<20];
bool go(int mask) {
	int& res = memo[mask];
	if (res != -1) return res;

	if (mask == ((1<<n)-1) ) return res = true;

	res = false;
	forn(i,n) if (!(mask & (1<<i)) && have[key[i]]) {
		have[key[i]]--;
		forn(j,si(chest[i])) have[chest[i][j]]++;
		if (go(mask ^ (1<<i))) {
			res = true;
			pick[mask] = i;
		}
		forn(j,si(chest[i])) have[chest[i][j]]--;
		have[key[i]]++;
		if (res) break;
	}
	return res;
}


void init() {
	fill(have, have+MAXN, 0);
	forn(i,n) chest[i].clear();
	memset(memo, -1, sizeof memo);
	memset(pick, -1, sizeof pick);
}

int main() {
        #ifdef LOCAL
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
        #endif

		int ncas; cin >> ncas;
        forn(cas,ncas) {
        	cout << "Case #" << cas+1 << ": ";
        	init();

        	int k; cin >> k >> n;
        	forn(_,k) {
        		int x; cin >> x;
        		have[x]++;
        	}

        	forn(i,n) {
        		cin >> key[i];
        		int k; cin >> k;
        		forn(_,k) {
        			int x; cin >> x;
        			chest[i].pb(x);
        		}
        	}

        	if (!go(0)) cout << "IMPOSSIBLE" << endl;
        	else {
        		vi res; int mask = 0;
        		while (pick[mask] != -1) {
        			int x = pick[mask];
        			mask ^= (1<<x);
        			res.pb(x);
        		}
        		forn(i,si(res)) {
        			if (i) cout << ' ';
        			cout << res[i]+1;
        		}
        		cout << endl;
        	}
		}

        return 0;
}
