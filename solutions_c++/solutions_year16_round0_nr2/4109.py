#include <iostream> 
#include <stdlib.h>

using namespace std;

int main() {
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		string str;
		cin >> str;

		int c = 0;
		int size = str.size();
		if (size == 1 && str[0] == '-') {
			c = 1;
		}
		for (int j = 1; j < size; j++) {
			if (str[j] != str[j - 1]) {
				++c;
			}
		}
		if (size > 1 && str[size - 1] == '-') {
			++c;
		}
		

		cout << "Case #" << i + 1 << ": " << c << "\n";
	}
	return 0;
}