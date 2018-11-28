#include <cstdint>
#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

void resolver(uint64_t N) {
	string str;
	uint16_t S = 0, atual = N;
	for (int i = 1; i <= 100; ++i) {
		atual = i*N;
		str = to_string(atual);
		for (auto& c: str) {
			S |= (1 << (c - 48));
		}
		if (S == 1023) {
			cout << atual << "\n";
			return;
		}
	}
	cout << "INSOMNIA" << "\n";
}

int main () {
	uint64_t N;
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> N;
		cout << "Case #" << i << ": ";
		resolver(N);
	}
}