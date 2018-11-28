#include <iostream>
using namespace std;

int main() {
	int t, odp, k;
	string s;
	cin >> t;
	for(int i = 1; i <= t; i ++) {
		cin >> odp >> s;
		odp = 0;
		k = 0;
		for(int j = 0; j < s.length(); j ++) {
			s[j] -= '0';
			if(s[j]) {
				odp += max(0, j - k - odp);
				k += s[j];
			}
		}
		cout << "Case #" << i << ": " << odp << endl;
	}
}
