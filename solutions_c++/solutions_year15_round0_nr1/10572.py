#include <iostream>
#include <algorithm>
using namespace std;

int calculate() {
	int sMax, v;
	int s[1002];

	memset(s, 0, sizeof(s));
	cin >> sMax >> v;
	for (int i=0; i<=sMax; ++i) {
		s[sMax-i] = v % 10;
		v /= 10;
	}

	int need = 0;
	int stand = s[0];
	for (int i=1; i<=sMax; ++i) {
		if (stand < i && s[i] > 0) {
			need += i - stand;
			stand += i - stand;
		}
		stand += s[i];
	}

	return need;
}

int main() {
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i) {
		printf("Case #%d: %d\n", i, calculate());
	}
}

