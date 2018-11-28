#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int cases;
	cin >> cases;
	for(int c = 1; c <= cases; c++) {
		int cnt = 0;
		int standing = 0;
		int S;
		string str;
		cin >> S >> str;
		for(int i = 0; i < S + 1; i++) {
				if(str[i] == '0') continue; 
				if(standing >= i) {
					standing += (str[i] - '0');
				} else {
					cnt += (i - standing);
					standing += ( i - standing);
					standing += (str[i] - '0');
				}

		}

		cout << "Case #" << c<<": " << cnt << endl;
	}

	return 0;
}
