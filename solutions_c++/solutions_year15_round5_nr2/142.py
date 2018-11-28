#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
#include<assert.h>
using namespace std;
#define FOR(i,a,b) for(int i = a; i <= b; ++i)
#define FORD(i,a,b) for(int i = a; i >= b; --i)
#define RI(i,n) FOR(i,1,n)
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
bool debug;
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const ll INF = (ll) inf * inf;
const int nax = 1e6 + 5;

int r[nax], t[nax], low[nax], dow[nax];

void te() {
	int n, k;
	scanf("%d%d", &n, &k);
	REP(i, n - k + 1) scanf("%d", &t[i]);
	/*if(n - k + 1 <= 5) {
		printf("%d %d\n", n, k);
		REP(i, n - k + 1) printf("%d ", t[i]);
		puts("");
	}
	else {
		puts("");
		return;
	}*/
	REP(i, n - k) r[i] = t[i+1]-t[i];
	//REP(i, n - k) printf("%d ", r[i]);
	//puts("");
	int res = 0;
	int MA = -1, MI = -1;
	REP(i, k) {
		int mi = 0, ma = 0;
		int a = 0;
		for(int j = i; j < n - k; j += k) {
			a += r[j];
			maxi(ma, a);
			mini(mi, a);
		}
		if(ma - mi >= res) {
			MA = ma;
			MI = mi;
		}
		maxi(res, ma - mi);
	}
	//REP(i, max(n - k, k)) low[i] = dow[i] = 0;
	REP(i, k) {
		int mi = 0, ma = 0;
		int a = 0;
		for(int j = i; j < n - k; j += k) {
			a += r[j];
			maxi(ma, a);
			mini(mi, a);
		}
		dow[i] = (MA-MI) - (ma-mi);
		low[i] = -mi;
		//high[i] = low[i] + dow;
	}
	int cel = t[0] % k;
	if(t[0] < 0) {
		cel = (k - (-t[0])%k)%k;
	}
	int ja = 0;
	REP(i, k) ja = (ja + low[i]) % k;
	int DO = 0;
	REP(i, k) DO += dow[i];
	//DO %= k;
	//if(n - k + 1 <= 5) printf("%d\n", n - k + 1);
	//return;
//	printf("%d + %d  %d  %d\n", ja, DO, cel, k);
//	printf("%d\n", res);
	if(ja <= cel && cel <= ja + DO)
		printf("%d\n", res);
	else if(ja <= cel + k && cel + k <= ja + DO)
		printf("%d\n", res);
	else
		printf("%d\n", res + 1);
}

int main(int argc, char *argv[])
{
	debug = argc > 1;
	int zz;
	scanf("%d", &zz);
	RI(nr, zz) {
		printf("Case #%d: ", nr);
		te();
	}
	return 0;
}
