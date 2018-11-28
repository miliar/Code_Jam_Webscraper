#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <cstring>

using namespace std;

int main() {
	freopen("counting_sheep.txt", "w", stdout);
	int T;
	cin >> T;


	long long x,y;
	set<int> s;
	long long temp;
	int it;
	for (int t = 1; t <= T; t++) {
		cin >> x;
		if (x == 0) {
			cout << "Case #" << t << ": " << "INSOMNIA\n";
			continue;
		}
		it = 1;
		//Iterate all digit
		while (s.size() < 10) {
			y = it * x;
			temp = y;
			while (temp > 0) {
				s.insert(temp%10);
				temp /= 10;
			}
			it++;
		}

		cout << "Case #" << t << ": " << y << "\n";
		s.clear();
	}


	return 0;
}