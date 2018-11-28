#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof__(V.begin()) it = V.begin(); it != V.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long LL;

const LL mod = 1000002013;

struct trojka {
	int beg, end, ilu;
	trojka(int _beg, int _end, int _ilu): beg(_beg), end(_end), ilu(_ilu) {}
};

bool przecina(trojka &a, trojka &b) {
	if (!a.ilu || !b.ilu) { return false; }
	return a.beg < b.beg && b.beg <= a.end && a.end < b.end;
}

LL koszt_dlugosc(int x, int n) {
	LL res = 0;
	int minus = 0;
	REP(i,x) {
		res = res + (n - minus);
		res %= mod;
		++minus;
	}
	return res;
}

LL koszt(vector<trojka> &kolesie, int n) {
	LL koszt = 0;
	REP(i,kolesie.size()) {
		koszt = koszt + (koszt_dlugosc(kolesie[i].end - kolesie[i].beg, n) * kolesie[i].ilu) % mod;
		koszt %= mod; 
	}
	return koszt;
}

void testcase() {
	int n, m;
	scanf("%d%d", &n, &m);
	vector<trojka> trojki;
	REP(i,m) {
		int beg, end, ilu;
		scanf("%d%d%d", &beg, &end, &ilu);
		trojki.PB(trojka(beg, end, ilu));
	}
	LL koszt_przed = koszt(trojki, n);
	bool ok = true;
	while(ok) {
		ok = false;
		int ilu_ich = trojki.size();
		REP(i,ilu_ich) REP(j,ilu_ich) {
			if (przecina(trojki[i], trojki[j])) {
				ok = true;
				int do_wymiany = min(trojki[i].ilu, trojki[j].ilu);
				trojki[i].ilu -= do_wymiany; trojki[j].ilu -= do_wymiany;
				trojki.PB(trojka(trojki[i].beg, trojki[j].end, do_wymiany));
				trojki.PB(trojka(trojki[j].beg, trojki[i].end, do_wymiany));
			}
		}
	}
	LL koszt_po = koszt(trojki, n);

	printf("%lld\n", (mod + koszt_przed - koszt_po)%mod);
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(i,1,t) {
  	printf("Case #%d: ", i);
  	testcase();
  }
}
