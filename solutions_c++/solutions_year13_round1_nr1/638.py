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
	ll r, t, consume, result;
    cin >> T;
	FOR(i, 1, T+1) {
		cout << "Case #" << i << ": ";
		cin >> r >> t;
		result = 0;
		consume = 2*r + 1;
		while (consume <= t) {
			++result;
			t -= consume;
			r += 2;
			consume = 2*r + 1;
		}
		cout << result << '\n';
	}

    return 0;
}
