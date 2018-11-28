#include <iostream>  
using namespace std;

int pancake(string& num) {
	char sign;
	int cnt = 1;
	if (num.size() == 1) return num[0] == '+' ? 0 : 1;
	sign = num[0];
	for (int i = 1; i < num.size(); i++) {
		while (i < num.size() && num[i] == num[i - 1]) i++;
		if (i < num.size()) {
			sign = num[i];
			cnt++;
		}
	}
	if (sign == '+') cnt--;
	return cnt;
}

int main() {
	int t;
	string n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n and then m.
		cout << "Case #" << i << ": " << pancake(n) << endl;
	}
}