#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int z = 1; z <= t; ++z) {
		int smax;
		string s;
		cin >> smax >> s;
		int total = 0, fr = 0;
		for (int shy = 0; shy <= smax; ++shy) {
			if (total + fr < shy) fr = shy - total;
			total += s[shy] - '0';
		}
		cout << "Case #" << z << ": " << fr << endl;
	}
}