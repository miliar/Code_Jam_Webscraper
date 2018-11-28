#include <iostream>
#include <math.h>
#include <string>
#include <sstream>

using namespace std;

bool isPali(int num) {
	stringstream a;
	string b;
	a << num;
	b = a.str();
	for (int i=0; i<b.size()/2; i++) {
		if (b.at(i)!=b.at(b.size()-i-1)) {
			return false;
		}
	}
	return true;
}

int main() {
	int t;
	cin >> t;
	for (int T=1; T<=t; T++) {
		int a, b, count(0);
		cin >> a >> b;
		for (int i=a; i<=b; i++) {
			if (sqrt(double(i))==int(sqrt(double(i))) && isPali(i) && isPali(int(sqrt(double(i))))) {
				count++;
			}
		}
		cout << "Case #" << T << ": " << count << endl;
	}
	return 0;
}
