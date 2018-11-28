#include <bits/stdc++.h>

using namespace std;
#define DEBUG_ON 1

#define INF 0x3f3f3f3f
#define NSYNC ios::sync_with_stdio(false);
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define FOR0(i,b) for(int i=0; i<(b); ++i)
#define TRAV(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define RTRAV(it,c) for(__typeof((c).rbegin()) it=(c).rbegin(); it!=(c).rend(); ++it)
#define DBG(x) if(DEBUG_ON) cout << #x << " == " << x << endl
#define DBGP(x) if(DEBUG_ON) cout << "(" << (x).first << ", " << (x).second << ")" << endl
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define R(x) scanf(" %d",&(x))
#define RR(x,y) scanf(" %d %d",&(x), &(y))
#define RRR(x,y,z) scanf(" %d %d %d",&(x), &(y),&(z))
#define CLR(v) memset(v, 0, sizeof(v))
#define SET(v) memset(v, -1, sizeof(v))

typedef long long ll;
typedef int int_type;
typedef pair<int_type, int_type> pii;
typedef vector<int_type> vi;
typedef vector<vi> vii;

const int N = 100000000;
bool pr[N+10];
int primes[5761555];
ll divs[20];

void crivo(int n) {
	memset(pr, true, sizeof(pr));
	pr[0] = pr[1] = false;
	for(int i=2; i*i<=n; ++i) {
		if(!pr[i] || (!(i&1) && i>2)) continue;
		int k = i*i;
		while(k<=n) {
			pr[k] = false;
			k += i;
		}
	}
}

bool verifier(int val, int n) {
	if(!(val&(1<<(n-1))) || !(val&(1<<(0)))) return false;
}

int main() {
	NSYNC;
	crivo(N);
	int sz = 0;
	FOR0(i,N+1) if(pr[i]) primes[sz++] = i;
	int t;
	cin >> t;
	FOR(tt,1,t+1) {
		cout << "Case #" << tt << ":\n";
		int n,j;
		cin >> n >> j;
		FOR0(i,1<<(n-2)) {
			bool ok = true;
			SET(divs);
			FOR(b,2,10+1) {
				ll val = 1;
				ll pot = b;
				FOR0(j,n-2) {
					val += (i&(1<<j)) ? pot : 0LL;
					pot *= b;
				}
				val += pot;
				FOR0(j,sz) {
					ll p = primes[j];
					if(p*p > val) break;
					if(p<val && val%p == 0) {
						divs[b] = p;
						break;
					}
				}
				if(divs[b]==-1LL) {
					ok = false;
					break;
				}
			}
			if(ok) {
				cout << 1;
				for(int j=n-3; j>=0; --j) cout << ((i&(1<<j)) ? '1' : '0');
				cout << 1;
				FOR(j,2,10+1) {
					cout << " " << divs[j];
				}
				cout << endl;
				if((--j)==0) break;
			} 
		}
	}
	return 0;
}