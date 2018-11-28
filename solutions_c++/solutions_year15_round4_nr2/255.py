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
const int nax = 500123;

const ld eps = 1e-11;

bool equal(ld a, ld b) { return abs(a-b) < eps; }

struct P {
	ld rate, temp;
	P(){}
	void wczytaj() { scanf("%Lf%Lf", &rate, &temp); }
	bool operator < (const P & b) const { return temp < b.temp; }
};

P t[nax];

void te() {
	int n;
	ld V, TEMP;
	scanf("%d%Lf%Lf", &n, &V, &TEMP);
	REP(i, n) t[i].wczytaj();
	
	bool spoko = false;
	REP(i, n) if(equal(TEMP, t[i].temp)) spoko = true;
	if(!spoko) {
		REP(i, n) if(t[i].temp < TEMP) spoko = true;
		if(spoko) {
			spoko = false;
			REP(i, n) if(t[i].temp > TEMP) spoko = true;
		}
	}
	if(!spoko) {
		puts("IMPOSSIBLE");
		return;
	}
	
	ld res = INF;
	
	REP(_, 2) {
		sort(t, t + n);
		int two = 0;
		while(two < n && t[two].temp + eps < TEMP) ++two;
		assert(two < n);
		int one = 0;
		
		ld suma_rate = 0;
		ld prawo = 0;
		ld lewo = 0;
		int memo_two = two;
		if(equal(t[two].temp, TEMP)) {
			suma_rate += t[two].rate;
			mini(res, V / suma_rate);
			++two;
		}
		FOR(i, two, n - 1) {
			suma_rate += t[i].rate;
			prawo += t[i].rate * (t[i].temp - TEMP);
			while(one < memo_two) {
				if(lewo + t[one].rate * (TEMP - t[one].temp) <= prawo + eps) {
					suma_rate += t[one].rate;
					lewo += t[one].rate * (TEMP - t[one].temp);
					++one;
				}
				else {
					ld brak = prawo - lewo;
					ld pom = brak / (TEMP - t[one].temp);
					mini(res, V / (suma_rate + pom));
					break;
				}
			}
			if(equal(prawo, lewo)) mini(res, V / suma_rate);
		}
		REP(i, n) t[i].temp = 2 * TEMP - t[i].temp;
	}
	REP(_, 2) {
		sort(t, t + n);
		int two = 0;
		while(two < n && t[two].temp + eps < TEMP) ++two;
		assert(two < n);
		int one = 0;
		
		ld suma_rate = 0;
		ld prawo = 0;
		ld lewo = 0;
		int memo_two = two;
		if(equal(t[two].temp, TEMP)) {
			suma_rate += t[two].rate;
			mini(res, V / suma_rate);
			++two;
		}
		FOR(i, 0, memo_two - 1) {
			suma_rate += t[i].rate;
			lewo += t[i].rate * (TEMP - t[i].temp);
			while(two < n) {
				if(prawo + t[two].rate * (t[two].temp  - TEMP) <= lewo + eps) {
					suma_rate += t[two].rate;
					prawo += t[two].rate * (t[two].temp - TEMP);
					++two;
				}
				else {
					ld brak = lewo - prawo;
					ld pom = brak / (t[two].temp - TEMP);
					mini(res, V / (suma_rate + pom));
					break;
				}
			}
			if(equal(prawo, lewo)) mini(res, V / suma_rate);
		}
		
		REP(i, n) t[i].temp = 2 * TEMP - t[i].temp;
	}
	assert(res < INF - 5);
	printf("%.12Lf\n", res);
}

int main(int argc, char *argv[])
{
	debug = argc > 1;
	
	int z;
	scanf("%d", &z);
	RI(nr, z) {
		printf("Case #%d: ", nr);
		te();
	}
	
	return 0;
}
