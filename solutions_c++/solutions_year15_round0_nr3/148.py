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
const int nax = 5e6 + 5;
typedef pair<int, bool> P;

char sl[nax];

P multi(P p, P q) {
	int a = p.first, b = q.first;
	swap(a,b);
	int pom;
	if(a == 0) pom = b;
	if(a == 1) {
		if(b == 0) pom = 1;
		if(b == 1) {
			pom = 0;
			p.second = !p.second;
		}
		if(b == 2) {
			pom = 3;
			p.second = !p.second;
		}
		if(b == 3) pom = 2;
	}
	if(a == 2) {
		if(b == 0) pom = 2;
		if(b == 1) pom = 3;
		if(b == 2) {
			pom = 0;
			p.second = !p.second;
		}
		if(b == 3) {
			pom = 1;
			p.second = !p.second;
		}
	}
	if(a == 3) {
		if(b == 0) pom = 3;
		if(b == 1) {
			pom = 2;
			p.second = !p.second;
		}
		if(b == 2) pom = 1;
		if(b == 3) {
			pom = 0;
			p.second = !p.second;
		}
	}
	return make_pair(pom, !(p.second ^ q.second));
}

void wypisz(P p) {
	printf("(%d, ", p.first);
	if(p.second) printf("true)\n");
	else printf("false)\n");
}

int f(char a) {
	if(a == 'i') return 1;
	if(a == 'j') return 2;
	if(a == 'k') return 3;
	assert(false);
}

P t[nax];

bool te() {
	int n;
	ll times;
	scanf("%d%lld", &n, &times);
	scanf("%s", sl);
	if(times > 200) times = 64 + times % 64;
	REP(i, n * (int) times)
		sl[i] = sl[i % n];
	n *= (int) times;
	if(n < 3) return false;
	P p = mp(0, true);
	REP(i, n) {
		p = multi(p, mp(f(sl[i]), true));
		t[i] = p;
		//if(p.first == 1 && p.second)
			//printf("%d ", i);
	}
	if(t[n-1] != mp(0, false)) return false;
	int jeb = 0;
	while(t[jeb] != mp(1, true)) {
		++jeb;
		if(jeb == n) return false;
	}
	int two = n - 1;
	while(t[two] != mp(3, true)) {
		--two;
		if(two < jeb) return false;
	}
	return true;
}

#include<iostream>
int main(int argc, char *argv[])
{
	debug = argc > 1;
	
	int T;
	scanf("%d", &T);
	RI(test, T) {
		cerr << test << "\n";
		printf("Case #%d: ", test);
		puts(te() ? "YES" : "NO");
	}
	
	return 0;
}
