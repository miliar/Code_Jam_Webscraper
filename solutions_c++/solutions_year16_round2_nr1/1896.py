#include <iostream>
#include <string>

using namespace std;

// A = 65
// ABCDE FGHIJ KLMNO PQRST UVWXY Z

void doCase() {
	string s;
	cin >> s;
	
	int l[30];
	for (int i=0; i<30; i++) l[i] = 0;
	for (int i=0; i<s.length(); i++) l[s[i] - 65+1]++;
	
	for (int i=0; i<l[26]; i++) cout << 0;
	for (int i=0; i<l[15]-l[26]-(l[6]-l[22]+l[19]-l[24])-l[23]; i++) cout << 1;
	for (int i=0; i<l[23]; i++) cout << 2;
	for (int i=0; i<l[8]-l[7]; i++) cout << 3;
	for (int i=0; i<l[6]-l[22]+l[19]-l[24]; i++) cout << 4;
	for (int i=0; i<l[22]-l[19]+l[24]; i++) cout << 5;
	for (int i=0; i<l[24]; i++) cout << 6;
	for (int i=0; i<l[19]-l[24]; i++) cout << 7;
	for (int i=0; i<l[7]; i++) cout << 8;
	for (int i=0; i<l[9]-l[24]-l[7]-(l[22]-l[19]+l[24]); i++) cout << 9;
	
	return;
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++) {
		cout << "Case #" << i+1 << ": ";
		doCase();
		cout << endl;
	}
	return 0;
}