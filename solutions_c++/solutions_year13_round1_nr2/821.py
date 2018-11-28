#pragma comment(linker, "/STACK:12000000")

#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <iterator>
#include <cmath>
#include <cassert>
#include <iomanip>

using namespace std;

// --------------------- Template ---------------------------------------------

#define FOR(i, f, t) for (int i = (int)(f); i < (int)(t); ++i)
#define FORN(i, n) for (int i = 0; i < (int)(n); ++i)

template <class T, class IT>
inline void PRINT(IT i1, IT i2) {
    cout << '['; copy(i1, i2, ostream_iterator<T>(cout, ", ")); cout << "]\n";
}

#if defined(M_H_HOME) && (0)
#define DBG(x) (x)
#else
#define DBG(x)
#endif

typedef long long ll;
typedef long double ld;

// ------------------ Template end --------------------------------------------

const int MAX_N = 10;


int main() {

#if defined(M_H_HOME) && (0)
    ifstream ___ifs("b.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

    int T;
	ll E, R, N;
	ll v[MAX_N];
    cin >> T;
	FOR(i, 1, T+1) {
		cout << "Case #" << i << ": ";
		cin >> E >> R >> N;
		FORN(j, N) cin >> v[j];

		ll possibleE[6]; // only for easy
		ll possibleE_[6]; // only for easy
		FORN(j, 6) possibleE[j] = -1;
		possibleE[E] = 0;
		FORN(j, N) {
			FORN(j, 6) possibleE_[j] = -1;
			FORN(p0, 6) 
				if (possibleE[p0] != -1) {
					for (int spend = 0; spend <= p0; ++spend) {
						int after = min(E, p0 - spend + R);
						int gain = spend * v[j];
						possibleE_[after] = max(possibleE_[after], possibleE[p0] + gain);
					}
				}
			FORN(j, 6) possibleE[j] = possibleE_[j];
		}
		ll maxv = -1;
		FORN(j, 6) maxv = max(maxv, possibleE[j]);
		cout << maxv << '\n';
	}

    return 0;
}
