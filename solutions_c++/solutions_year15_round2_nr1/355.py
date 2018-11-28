#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<assert.h>
using namespace std;
#define FOR(i,a,b) for(int i = a; i <= b; ++i)
#define FORD(i,a,b) for(int i = a; i >= b; --i)
#define RI(i,n) FOR(i,1,n)
#define REP(i,n) FOR(i,0,(n)-1)
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define sz(w) (int)w.size()
bool debug;
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const int nax = 25;

ll pot[nax];

void te() {
	ll n;
	scanf("%lld", &n);
	ll res = 0;
	if(n >= 10) res++;
	if(n >= 10) res += 9;
	if(n >= 100) res += 19;
	if(n >= pot[3]) res +=  109;
	if(n >= pot[4]) res +=  199;
	if(n >= pot[5]) res +=  1099;
	if(n >= pot[6]) res +=  1999;
	if(n >= pot[7]) res +=  10999;
	if(n >= pot[8]) res +=  19999;
	if(n >= pot[9]) res +=  109999;
	if(n >= pot[10]) res += 199999;
	if(n >= pot[11]) res += 1099999;
	if(n >= pot[12]) res += 1999999;
	if(n >= pot[13]) res += 10999999;
	if(n >= pot[14]) res += 19999990;
	
	bool spec = false;
	REP(i, 16) if(n == pot[i]) spec = true;
	bool flag = false;
	if(spec == false && n % 10 == 0) {
		flag = true;
		n--;
	}
		vi w;
		ll pom = n;
		while(pom) {
			w.pb(int(pom%10));
			pom /= 10;
		}
		#define pom gowno
		int d = sz(w);
		int half = (d + 1) / 2;
		REP(i, half) if(w[i]) res += pot[i] * w[i];
		bool trzeba = false;
		FOR(i, half, sz(w) - 2) if(w[i]) trzeba = true;
		if(w.back() > 1 && sz(w)-1 >= half) trzeba = true;
		if(trzeba) res++;
		FOR(i, half, sz(w) - 2) res += pot[sz(w)-1-i] * w[i];
		if(sz(w)-1 >= half) res += pot[0] * (w.back() - 1);
	
	if(flag) ++res;
	
	printf("%lld\n", res);
}

int main(int argc, char * argv[]) { 
	debug = argc > 1;
	
	pot[0] = 1;
	RI(i, nax - 1) pot[i] = pot[i-1] * 10;
	
	int zz;
	scanf("%d", &zz);
	RI(nr, zz) {
		printf("Case #%d: ", nr);
		te();
	}
	
	return 0;
}
