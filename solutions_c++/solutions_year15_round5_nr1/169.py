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
const int nax = 4e6 + 5;
int pot;

int s[nax], ojc[nax];
vi syn[nax];
int T;
int in[nax];
int out[nax];
int h[nax];
int tr[16 * 1024 * 1024];

void dfs(int a) {
	in[a] = T++;
	for(auto b : syn[a]) {
		h[b] = h[a] + 1;
		dfs(b);
	}
	out[a] = T++;
}

void dodaj(int a, int b, int co) {
	a += pot;
	b += pot;
	tr[a] += co;
	if(a != b) tr[b] += co;
	while(a < b - 1) {
		if(a % 2 == 0) tr[a+1] += co;
		if(b % 2 == 1) tr[b-1] += co;
		a /= 2;
		b /= 2;
	}
}

bool spoko[nax];

void sprawdz(int a, int & licz) {
	int pom = 0;
	for(int x = pot + in[a]; x; x /= 2) pom += tr[x];
	if(pom == 0 && spoko[a]) return;
	if(pom && !spoko[a]) return;
	if(spoko[a]) {
		spoko[a] = false;
		licz--;
	}
	else {
		spoko[a] = true;
		licz++;
	}
	for(auto b : syn[a]) sprawdz(b, licz);
}

void te() {
	int n, d;
	scanf("%d%d", &n, &d);
	pot = 1;
	while(pot <= n) pot *= 2;
	pot *= 2;
	REP(i, 2 * pot) tr[i] = 0;
	int as, cs, rs, am, cm, rm;
	scanf("%d%d%d%d", &s[0], &as, &cs, &rs);
	scanf("%d%d%d%d", &ojc[0], &am, &cm, &rm);
	RI(i, n - 1) s[i] = (s[i-1] * (ll) as + cs) % rs;
	RI(i, n - 1) ojc[i] = (ojc[i-1] * (ll) am + cm) % rm;
	RI(i, n - 1) ojc[i] %= i;
	vector<pair<int, pii> > w;
	REP(i, n) {
		w.pb(mp(s[i], mp(0, i)));
		w.pb(mp(s[i]+d, mp(1,i)));
	}
	sort(w.begin(), w.end());
	REP(i, n) syn[i].clear();
	RI(i, n - 1) syn[ojc[i]].pb(i);
	T = 0;
	h[0] = 0;
	dfs(0);
	//REP(i, n) printf("%d ", t[i]);
	REP(i, n) tr[pot + in[i]] = h[i] + 1;
	int licz = 0, res = 0;
	REP(i, n) spoko[i] = false;
	for(pair<int, pii> e : w) {
		int rodz = e.nd.st;
		int i = e.nd.nd;
		if(rodz == 0) dodaj(in[i], out[i], -1);
		else dodaj(in[i], out[i], 1);
		sprawdz(i, licz);
		maxi(res, licz);
	}
	printf("%d\n", res);
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
