#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int ans = 0, x = 0, totalPeople = 0, curAddition = 0;
		string s;
		cin >> x;
		cin >> s;

		for (int j = 0; j < s.size(); j++) {
			if (j <= totalPeople) {
				totalPeople += (s[j] - '0');
			}
			else {
				curAddition = j - totalPeople;
				totalPeople += (s[j] - '0') + curAddition;
				ans += curAddition;
			}
		}

		cout << "Case #" << i + 1 << ": " << ans << "\n";
	}
	
	return 0;
}