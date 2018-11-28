#pragma comment(linker, "/STACK:12000000")

#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <iterator>
#include <cmath>
#include <cassert>
#include <iomanip>
#include <queue>
#include <functional>

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
    ifstream ___ifs("b.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

    int T;
	cin >> T;
	FORN(casen, T) {
		int D;
		cin >> D;
		vector<int> s(D);
		int absmax = -1;
		FORN(i, D) {
			int P;
			cin >> P;
			s[i] = P;
			absmax = max(absmax, s[i]);
		}
		int result = absmax;
		for (int mx = absmax; mx > 0; --mx) {
			int mx_result = 0;
			FORN(i, D) {
				ldiv_t dv = ldiv(s[i], mx);
				mx_result += (dv.rem == 0) ? (dv.quot - 1) : dv.quot;
			}
			result = min(result, mx + mx_result);
		}
		cout << "Case #" << casen+1 << ": " << result << endl;
	}

    return 0;
}
