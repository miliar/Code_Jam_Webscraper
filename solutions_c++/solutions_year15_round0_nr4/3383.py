#include <iostream>
#include <vector>
using namespace std;

#define FORi(m) for( int i = 0; i < (m); ++i )
#define FOR(i, M) for( int i = 0; i < (M); ++i )
#define FOR1(i, M) for( int i = 1; i <= (M); ++i )
#define DEBUGGING 1
#define CERRL() if (DEBUGGING) { std::cerr << '\n'; }
#define EXAM(var) if (DEBUGGING) { std::cerr << #var << ": " << (var) << '\n'; }
#define EXAMARR(var) if (DEBUGGING) { std::cerr << #var << ": "; for (const auto& _var_: var) std::cerr << _var_ << " "; std::cerr << '\n'; }

// false: RICHARD
// true: GABRIEL

bool solve() {
	int X, R, C;
	cin >> X >> R >> C;
	if (X == 1) return true;
	int M = max(R,C), m = min(R,C);
	if (X == 2) {
		if (M == 3 && m == 3) return false;
		if (M == 3 && m == 1) return false;
		if (M == 1) return false;
		return true;
	}
	if (X == 3) {
		if (M == 4 && m == 3) return true;
		if (M == 3 && m >= 2) return true;
		return false;
	}
	if (X == 4) {
		if (M == 4 && m >= 3) return true;
		return false;
	}
}

int main() {
	int T;
	cin >> T;
	FOR1(t, T) {
		cout << "Case #" << t << ": ";
		if (solve()) cout << "GABRIEL";
		else cout << "RICHARD";
		cout << endl;
	}
}

