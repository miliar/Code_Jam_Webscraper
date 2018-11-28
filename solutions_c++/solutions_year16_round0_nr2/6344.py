#include <iostream>
#include <string>

using namespace std;

int main() {

	int t, u, count;
	string s;
	char cur;

	cin >> t;
	u = t;
	while(t--) {
		cin >> s;

		cur = s.at(0);
		count = 0;
		for(int i=1; i<s.length(); i++) {
			if(cur != s.at(i)) {
				cur = s.at(i);
				count++;
			}
		}
		if(cur == '-')
			count++;
		cout << "Case #" << u-t << ": " << count << endl; 
	}

	return 0;
}