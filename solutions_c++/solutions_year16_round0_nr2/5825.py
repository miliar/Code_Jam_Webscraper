#include <iostream>

using namespace std;

void flipStack(string& s, int n) {
	for (int i = 0; i < n / 2; i++) {
		//reverse the first n
		char temp = s.at(0);
		s.at(0) = s.at(n - 1);
		s.at(n - 1) = temp;
	}
	for (int i = 0; i < n; i++) {
		//flip the first n
		if (s.at(i) == '-') s.at(i) = '+';
		else s.at(i) = '-';
	}
}

bool happyStack(string& s) {
	if (s.find('-') == string::npos) return true;
	return false;
}

int main() {

	int n;
	
	cin >> n;
	for (int i = 1; i <= n; i++) {
		string pancakes;
		int y = 0;
		cin >> pancakes;

		while (!happyStack(pancakes)) {
			//cout << pancakes << " ";

			if (pancakes.find('+') == string::npos) {
				y++; break;
			}
			for (int z = 1; z < pancakes.size(); z++) {
				if (pancakes.at(z) == pancakes.at(z - 1)) {
					pancakes.erase(z, 1);
					z -= 1;
				}
			}
			if (pancakes.substr(0, 2) == "-+") {
				flipStack(pancakes, 1);
			}
			else if (pancakes.substr(0, 2) == "+-") {
				flipStack(pancakes, 1);
			}

			y++;
			//cout << pancakes << endl;
		}

		cout << "Case #" << i << ": " << y << endl;
	}

	return 0;
}