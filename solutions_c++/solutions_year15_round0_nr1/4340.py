#include <iostream>
#include <string>
using namespace std;
int main() {
	int T; cin >> T;
	int t = 1; int smax; 
	string people;
	
	while (t <= T) {
		cout << "Case #" << t++ << ": ";
		cin >> smax; cin >> people;
		
		int required = 0, total = 0;
		for (int level = 0; level <= smax; ++level) {
			if (total < level) {
				required += level-total;
				total = level;
			}
			total += people[level]-'0';
		}
		cout << required << endl;
	}
	return 0;
}
