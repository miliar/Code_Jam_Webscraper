#include <iostream>
#include <string>
 
using namespace std;
 
int solve() {
	int s;
	cin >> s;
	string a;
	cin >> a;
	int result = 0, cur = (int)a[0] - 48;
	for (int i = 1; i <= s; i++) {
		if (i > cur) {
			result += i - cur;
			cur = i;
		}
		cur += (int)a[i] - 48;
	}
	return result;
}
 
int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	return 0;
}