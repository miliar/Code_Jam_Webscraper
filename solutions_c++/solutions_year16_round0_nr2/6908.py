#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
using namespace std;

string S;
int valid() {
	for (int i = S.size(); i >= 0; --i) {
		if (S[i] == '-')
			return i;
	}

	return -1;
}

void turn(int p) {
	for (int i = p; i >= 0; --i) {
		if (S[i] == '-')
			S[i] = '+';
		else
			S[i] = '-';
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T, len;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		cin >> S;
		len = S.size();

		int n = 0;
		while (true) {
			int p = valid();
			if (p < 0) break;

			turn(p);
			++n;
		}

		cout << "Case #" << i << ": " << n << endl;
	}

	return 0;
}
