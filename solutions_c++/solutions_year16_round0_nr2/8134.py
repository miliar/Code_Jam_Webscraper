#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		string stack;
		cin >> stack;
		int pos = 0, neg = 0;
		for (auto c : stack) {
			if (c == '+') {
				pos = min(pos, neg + 1);
				neg = min(neg + 2, pos + 1);
			} else {
				pos = min(neg + 1, pos + 2);
				neg = min(pos + 1, neg);
			}
		}

		cout << "Case #" << i + 1 << ": " << pos << endl;
	}

	return 0;
}

