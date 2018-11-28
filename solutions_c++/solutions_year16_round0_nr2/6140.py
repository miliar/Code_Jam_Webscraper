#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;
int main() {
	int t;
	cin >> t;
	string s;
	for(int i = 1; i <= t; i++) {
		cin >> s;
		int j = s.length() - 1, res = 0;
		while(j >= 0 && s[j] == '+') j--;
		while(j >= 0) {
			res += 1;
			j--;
			while(j >= 0 && s[j] == s[j + 1]) j--;
		}
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}