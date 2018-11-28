#include <iostream>

using namespace std;


void init() {
	
}

void solvecase() {
	unsigned S;
	cin >> S;
	char c;
	unsigned total = 0;
	unsigned to_invite = 0;
	for (int i = 0; i <= S; ++i) {
		cin >> c;
		unsigned sm = (unsigned)(c - '0');
		if (i > total) {
			to_invite += i - total;
			total += i - total;
		}
		total += sm;
	}

	cout << to_invite << endl;
}

int N;
int main() {
	init();
	cin >> N;
	for (int t = 1; t <= N; ++t) {
		cout << "Case #" << t << ": ";
		solvecase();
	}

	return 0;
}