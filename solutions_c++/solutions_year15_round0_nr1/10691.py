#include <iostream>
using namespace std;


int main()
{
	int T;


	cin >> T;

	for (int t=0;t < T; ++t) {
		int S;
		cin >> S;

		int clapping = 0;
		int friends = 0;

		for (int s=0; s < (S+1); ++s) {
			char c;
			cin >> c;
			int shy = c - '0';

			if (shy) {
				if (s <= clapping) {
					clapping += shy;
				} else {
					friends += s - clapping;
					clapping += friends + shy;
				}
			}
		}

		cout << "Case #" << t+1 << ": " << friends << endl;
	}

	return 0;
}

