#include <iostream>
#include <vector>
#include <map>
using namespace std;

#define FORi(m) for( int i = 0; i < (m); ++i )
#define FOR(i, M) for( int i = 0; i < (M); ++i )
#define FOR1(i, M) for( int i = 1; i <= (M); ++i )
#define DEBUGGING 1
#define CERRL() if (DEBUGGING) { std::cerr << '\n'; }
#define EXAM(var) if (DEBUGGING) { std::cerr << #var << ": " << (var) << '\n'; }
#define EXAMARR(var) if (DEBUGGING) { std::cerr << #var << ": "; for (const auto& _var_: var) std::cerr << _var_ << " "; std::cerr << '\n'; }


int T;

void solve(int t) {
	int Sm;
	cin >> Sm;
	vector<int> shyness(Sm+1);
	for (int i = 0; i <= Sm; ++i) {
		char c;
		cin >> c;
		shyness[i] = c - '0';
	}
	
	int count = 0;
	int friends = 0;
	for (int i = 0; i <= Sm; ++i) {
		int miss = 0;
		if (count < i) friends += (miss = i - count);
		count += miss + shyness[i];
	}
	cout << "Case #" << t << ": " << friends << endl;
}

int main() {
	cin >> T;
	FOR1(t, T) {
		solve(t);
		cin.ignore(200, '\n');
	}
}


