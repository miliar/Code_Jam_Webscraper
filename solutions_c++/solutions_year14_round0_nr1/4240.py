#pragma comment(linker, "/STACK:12000000")

#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <iterator>
#include <cmath>
#include <cassert>
#include <iomanip>
#include <set>

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

	int T, casen;
	cin >> T;
	for (casen = 1; casen <= T; ++casen) {
		int r1, r2, b;
		cin >> r1;
		set<int> row1, row2;
		FORN(i, 4) FORN(j, 4) {
			cin >> b;
			if (i + 1 == r1) row1.insert(b);
		}
		cin >> r2;
		FORN(i, 4) FORN(j, 4) {
			cin >> b;
			if (i + 1 == r2) row2.insert(b);
		}

		int cand, count = 0;
		FOR(i, 1, 17) {
			if (row1.find(i) != row1.end() && row2.find(i) != row2.end()) {
				cand = i;
				++count;
			}
		}

		if (count == 1) {
			cout << "Case #" << casen << ": " << cand << '\n';
		} else if (count == 0) {
			cout << "Case #" << casen << ": Volunteer cheated!\n";
		} else {
			cout << "Case #" << casen << ": Bad magician!\n";
		}

	}

    return 0;
}
