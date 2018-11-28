#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int ix = 1; ix <= T; ix++) {
		string S;
		cin >> S;
		int count = 0;
		if(S[0] == '-')
			count++;

		for(unsigned int iy = 1; iy < S.length(); iy++) {
			if(S[iy-1] == '+' && S[iy] == '-')
				count += 2;
		}

		cout << "Case #" << ix << ": " << count << "\n";
	}

	return 0;
}
