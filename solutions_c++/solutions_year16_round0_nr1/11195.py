#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

#define FORi(m) for( int i = 0; i < (m); ++i )
#define FOR(i, M) for( int i = 0; i < (M); ++i )
#define FOR1(i, M) for( int i = 1; i <= (M); ++i )
#define DEBUGGING 1
#define CERRL() if (DEBUGGING) { std::cerr << '\n'; }
#define EXAM(var) if (DEBUGGING) { std::cerr << #var << ": " << (var) << '\n'; }
#define EXAMARR(var) if (DEBUGGING) { std::cerr << #var << ": "; for (const auto& _var_: var) std::cerr << _var_ << " "; std::cerr << '\n'; }


#define MAX 100000000L

void setbits(long& bits, long v) {
	while (v) {
		bits |= 1 << (v%10);
		v /= 10;
	}
}

void solve(long N) {
	long v = 0;
	long bits = 0;
	while (bits != 0b1111111111) {
		v = (v+N)%MAX;
		setbits(bits, v);
	}
	cout << v;
}

int main() {
	int T;
	cin >> T;
	FOR1(t, T) {
		long N;
		cin >> N;
		cout << "Case #" << t << ": ";
		if (!N) cout << "INSOMNIA";
		else solve(N);
		cout << endl;
	}
}


