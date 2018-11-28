#include <iostream>
#include <string>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; cas++) {
		string s;
		int smax;
		cin >> smax >> s;
		int people_standing = 0, friends_needed = 0;
		for (int i = 0; i <= smax; i++) {
			int people_with_shyness_i = s[i] - '0';
			if (people_standing < i) {
				friends_needed += i - people_standing;
				people_standing = i;
			}
			people_standing += people_with_shyness_i;
		}
		cout << "Case #" << cas << ": " << friends_needed << endl;
	}
	return 0;
}
