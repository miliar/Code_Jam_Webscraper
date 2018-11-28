#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int Smax;
		vector<int> Si;
		string str;
		int numStand = 0;
		int numInvite = 0;

		cin >> Smax >> str;
		for (int j = 0; j < Smax+1; j++) Si.push_back(str[j] - '0');
		for (int j = 0; j < Smax+1; j++) {
			if (j <= numStand) numStand += Si[j];
			else if (Si[j] != 0) {
				while (j > numStand + numInvite) {
					numInvite++;
				}
				numStand += Si[j];
			}
		}
		cout << "Case #" << i+1 << ": " << numInvite << endl;
	}
}