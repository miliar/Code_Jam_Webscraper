#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main () {
	int cases;
	cin >> cases;

	for (int tc = 1; tc <= cases; tc ++) {
		int Smax;
		string S;
		cin >> Smax >> S;

		int extra = 0;
		int now = 0;
		for (int i = 0; i < Smax + 1; i ++) {
			if (S[i] != '0') {
				extra += max(0, i - now);
				now += max(0, i - now);
				//cout << i << " " << extra << endl;
			}
			now += S[i] - '0';
		}
		cout << "Case #" << tc << ": " << extra << endl;
	}
}