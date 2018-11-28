#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	
	cin >> t;

	for(int i = 0; i < t; i++) {
		int sMax;

		cin >> sMax;

		string data;

		cin >> data;

		int p = 0;
		int add = 0;

		for(int s = 0; s <= sMax; s++) {
			if((p + add) < s) {
				add += s - (p + add);
			}

			p += (int) data[s] - 48;
		}

		cout << "Case #" << i + 1 << ": " << add << endl;
	}
}
