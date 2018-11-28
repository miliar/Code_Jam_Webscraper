#include <iostream>

using namespace std;

const int MAX_AUDIENCE = 2000;

int toInt(char c) {
	return (c - '0');
}

int main() 
{
	int T;

	cin >> T;

	for(int t = 1; t <= T; t++) {
		int smax;
		char audiences[MAX_AUDIENCE];

		cin >> smax >> audiences;

		int standing = 0, invite = 0;

		for(int i = 0; i <= smax; i++) {
			int n = toInt(audiences[i]);
			if (n > 0 && i > standing) {
				invite += (i - standing);
				standing += (i - standing);
			}
			standing += n;
		}

		cout << "Case #" << t << ": " << invite << endl;
	}

	return 0;
}
