#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int Smax;
		cin >> Smax;
		vector<int> people(Smax + 1);
		string s;
		cin >> s;
		for (int i = 0; i < s.size(); ++i) {
			people[i] = s[i] - '0';
		}
		int curStanding = people[0], peopleNeeded = 0;
		for (int i = 1; i <= Smax; ++i) {
			if (curStanding >= i) {
				curStanding += people[i];
			} else {
				int locPeople = (i - curStanding);
				peopleNeeded += locPeople;
				curStanding += (locPeople + people[i]);
			}
		}
		cout << "Case #" << t << ": " << peopleNeeded << "\n";
	}
	return 0;
}