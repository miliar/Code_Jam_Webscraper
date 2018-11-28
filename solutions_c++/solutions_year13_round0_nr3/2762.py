#include <iostream>
using namespace std;

int amount(int min, int max);
bool inInterval(int num, int min, int max);

int main() {
	int cases;
	cin >> cases;
	for(int i = 0; i < cases; i++) {
		cout << "Case #" << (i+1) << ": ";
		int min;
		int max;
		cin >> min >> max;
		cout << amount(min,max) << endl;
	}
}

int amount(int min, int max) {
	int am = 0;
	if(inInterval(1,min,max)) am++;
	if(inInterval(4,min,max)) am++;
	if(inInterval(9,min,max)) am++;
	if(inInterval(121,min,max)) am++;
	if(inInterval(484,min,max)) am++;
	return am;
}

bool inInterval(int num, int min, int max) {
	if(num >= min && num <= max) return true;
	return false;
}