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

// Seconds to reach what_to_reach
inline double timeToReach(double cookies_to_reach, double per_sec, double cookies_now) {
	return (cookies_to_reach - cookies_now) / per_sec;
}

int main() {

#if defined(M_H_HOME) && (0)
    ifstream ___ifs("b.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

   	int T, casen;
	cin >> T;
	for (casen = 1; casen <= T; ++casen) {
		double C, // farm cost
			   F, // farm extra cookies
			   X; // required to win
		cin >> C >> F >> X;

		double time_now = 0, cookies_now = 0, per_sec_now = 2.0;
		double best_time = timeToReach(X, 2, 0);
		double cand_time = time_now + timeToReach(C, per_sec_now, cookies_now) + timeToReach(X, per_sec_now + F, 0);
		while (cand_time < best_time - 1e-9) {
			best_time = cand_time;
			time_now = time_now + timeToReach(C, per_sec_now, cookies_now);
			cookies_now = 0;
			per_sec_now += F;
		    cand_time = time_now + timeToReach(C, per_sec_now, cookies_now) + timeToReach(X, per_sec_now + F, 0);
		}

		cout << "Case #" << casen << ": " << setprecision(7) << fixed << best_time << '\n';
	}

    return 0;
}
