#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>

using namespace std;






int main() {
	int t = 0, stand = 0, si = 0, count = 0;
	string people = "";
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> si >> people;
		for (int j = 0; j < people.length(); j++) {
			if (stand < j) {
				count++;
				stand++;
			}
			stand += people[j] - '0';
		}
		cout << "Case #" << i << ": " << count << endl;
		count = 0;
		stand = 0;
	}


	// for (int i = 1; i <= t; ++i) {
	// 	cout << "Case #" << i << ": " << t << endl;
	// }
 	return 0;
}