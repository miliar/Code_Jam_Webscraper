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
    ifstream ___ifs("b.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

    int T;
	cin >> T;
	for (int casen = 1; casen <= T; ++casen) {
		int A, B, K;
		cin >> A >> B >> K;
		int count = 0;
		for (int a = 0; a < A; ++a) 
			for (int b = 0; b < B; ++b) 
				if ((a & b) < K) ++count;
			
		cout << "Case #" << casen << ": " << count << '\n';
	}

	return 0;
}
