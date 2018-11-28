#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int i = 1; i <= T; ++i) {
		string p;
		cin >> p;

		char lastChar = 0, cPlus = '+', cMinus = '-';
		auto end = p.end();
		int nb = 0, size = 0;
		for(auto it = p.begin(); it!=p.end(); ++it) {
			if(lastChar == 0)
				lastChar = *it;
			else if(*it != lastChar) {
				if(lastChar == cPlus) {
					lastChar = cMinus;
					nb++;
				} else {
					nb++;
					lastChar = cPlus;
				}
			}
		}

		if(lastChar == cMinus) nb++;

		cout << "Case #" << i << ": " << nb << endl;

	}
}