#include <iostream>
#include <string>

using namespace std;
int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		int smax;
		cin >> smax;
		string scnt;
		cin >> scnt;
		
		int needed = 0;
		int current = 0;
		for (int i=0;i<scnt.length();i++) {
			int cnt = scnt[i] - '0';
			if (current < i) {
				needed += (i - current);
				current += (i - current);
			}
			current += cnt;
		}
		cout << "Case #" << t << ": " << needed << endl;
	}
	return 0;
}
