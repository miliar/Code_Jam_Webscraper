#include <bits/stdc++.h>

using namespace std;
#define DEBUG_ON 1

#define INF 0x3f3f3f3f
#define NSYNC ios::sync_with_stdio(false)
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define FOR0(i,b) for(int i=0; i<(b); ++i)
#define TRAV(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define RTRAV(it,c) for(__typeof((c).rbegin()) it=(c).rbegin(); it!=(c).rend(); ++it)
#define DBG(x) if(DEBUG_ON) cout << #x << " == " << x << endl
#define DBGP(x) if(DEBUG_ON) cout << "(" << (x).first << ", " << (x).second << ")" << endl
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define CLR(v) memset(v, 0, sizeof(v))
#define SET(v) memset(v, -1, sizeof(v))

typedef long long ll;
typedef int int_type;
typedef pair<int_type, int_type> pii;
typedef vector<int_type> vi;
typedef vector<vi> vii;

const int MAXN = 11000;
int n;
char v[MAXN];
unordered_map<int,bool> lmp;
unordered_map<int,bool> rmp;
pair<char, int> prod[500][500];

void preproc() {
	prod['1']['1'] = {'1',0};
	prod['1']['i'] = {'i',0};
	prod['1']['j'] = {'j',0};
	prod['1']['k'] = {'k',0};

	prod['i']['1'] = {'i',0};
	prod['i']['i'] = {'1',1};
	prod['i']['j'] = {'k',0};
	prod['i']['k'] = {'j',1};

	prod['j']['1'] = {'j',0};
	prod['j']['i'] = {'k',1};
	prod['j']['j'] = {'1',1};
	prod['j']['k'] = {'i',0};

	prod['k']['1'] = {'k',0};
	prod['k']['i'] = {'j',0};
	prod['k']['j'] = {'i',1};
	prod['k']['k'] = {'1',1};
}

bool solve() {
	// cout << "\n\n\n";
	lmp.clear();
	char aux = '1';
	int neg = 0;
	FOR0(i,n) {
		pair<char, int> auxprod = prod[aux][v[i]];
		aux = auxprod.first;
		neg = (neg+auxprod.second)%2;
		if(aux=='i' && !neg) lmp[i] = true;
	}
	if(lmp.empty()) return false;
	rmp.clear();
	aux = '1';
	neg = 0;
	for(int i = n-1; i>=0; --i) {
		pair<char, int> auxprod = prod[v[i]][aux];
		aux = auxprod.first;
		neg = (neg+auxprod.second)%2;
		if(aux=='k' && !neg) rmp[i] = true;		
	}
	if(rmp.empty()) return false;
	// TRAV(it,lmp) cout << it->first << " ";
	// cout << "\n";
	// TRAV(it,rmp) cout << it->first << " ";
	// cout << "\n";

	FOR(i, 1, n-1) {
		aux = '1';
		neg = 0;
		FOR(j, i, n-1) {
			pair<char, int> auxprod = prod[aux][v[j]];
			aux = auxprod.first;
			neg = (neg+auxprod.second)%2;
			if(aux=='j' && !neg && lmp.count(i-1) && rmp.count(j+1))
				return true;
		}		
	}
	return false;
}

int main() {
	preproc();
	int tests;
	scanf(" %d",&tests);
	FOR(t, 1, tests+1) {
		int l, x;
		scanf(" %d %d",&l,&x);
		FOR0(i,l) scanf(" %c",v+i);
		n = l;
		FOR0(cop,x-1) {
			FOR0(j,l) v[n++] = v[j];
		}
		printf("Case #%d: ",t);
		if(solve()) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}