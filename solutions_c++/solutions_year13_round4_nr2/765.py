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

void testcase() {
	int n;
	LL p;
	scanf("%d%lld", &n, &p);

	LL wszystkich = (1LL << n);
	// znajdz tego ktory MOZE wygrac
	LL beg = 0, end = (1LL << n) - 1;
	LL res = 0;
	while (beg <= end) {
		LL mid = (beg + end) / 2; // mid - kandydat
		LL ilu_wiekszych = wszystkich - mid - 1;
		LL koles = 0;

		LL dla_niego = (1<<n) - 1;
		int zdjac = (n-1);

		int odjemniki = 0;
		while (ilu_wiekszych - (1LL << odjemniki) >= 0) {
			dla_niego = dla_niego - (1LL << zdjac);
			--zdjac;
			ilu_wiekszych -= (1LL << odjemniki);
			++odjemniki;
		}
		if (dla_niego < p) {
			res = mid;
			beg = mid+1;
		} else {
			end = mid - 1;
		}
	}

	LL moze = res;

	// znajdz tego ktory MUSI wygrac
	beg = 0, end = (1LL << n) - 1;
	res = 0;
	while (beg <= end) {
		LL mid = (beg + end) / 2; // mid - kandydat
		LL ilu_mniejszych = mid;
		LL koles = 0;

		LL dla_niego = 0;
		int zdjac = n-1;

		int odjemniki = 0;
		while (ilu_mniejszych - (1LL << odjemniki) >= 0) {
			dla_niego = dla_niego + (1LL << zdjac);
			--zdjac;
			ilu_mniejszych -= (1LL << odjemniki);
			++odjemniki;
		}
		if (dla_niego < p) {
			res = mid;
			beg = mid+1;
		} else {
			end = mid - 1;
		}
	}

	LL musi = res;
	printf("%lld %lld\n", musi, moze);
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(i,1,t) {
  	printf("Case #%d: ", i);
  	testcase();
  }
}
