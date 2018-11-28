#include <iostream>
#include <vector>
using namespace std;

string trysleep(int num) {
	if (num == 0) return "INSOMNIA";
	vector<bool> digit(10, false);
	int count = 0;
	int mul = 2;
	int n = num;
	while (1) {
		string s = to_string(n);
		for(int i = 0; i < s.size(); i++) {
			if (digit[s[i] - '0'] == false) {
				count++;
				digit[s[i] - '0'] = true;
			}
		}
		if (count == 10) {
			break;
		}
		n = mul * num;
		mul++;
	}
	return to_string(n);
}

int main() {
	int t;
	int n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n and then m.
		cout << "Case #" << i << ": " << trysleep(n) << endl;
	}
}