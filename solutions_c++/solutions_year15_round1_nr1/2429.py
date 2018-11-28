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


int main() {

#if defined(M_H_HOME) && (0)
    ifstream ___ifs("a.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

    int T;
    cin >> T;
	FORN(casen, T) {
		int N;
		cin >> N;
		vector<ll> m(N);
		FORN(i, N) cin >> m[i];
		ll way1 = 0;
		for (int i = 1; i < N; ++i) {
			if (m[i] < m[i-1]) way1 += m[i-1] - m[i];
		}
		ll way2 = 0, q = 0;
		for (int i = 1; i < N; ++i) {
			if (m[i] < m[i-1]) q = max(q, m[i-1] - m[i]);
		}
		for (int i = 0; i < N-1; ++i) {
			way2 = way2 + min(m[i], q);
		}
		cout << "Case #" << casen+1 << ": " << way1 << " " << way2 << endl;
	}

    return 0;
}
