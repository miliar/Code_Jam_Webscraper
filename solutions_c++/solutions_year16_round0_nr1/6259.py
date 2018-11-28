#include <iostream>
#include <cstring>
#include <string>

using namespace std;

bool digit[10];

bool check() {
	for(int i=0; i<10; i++) {
		if(digit[i] == false)
			return false;
	}
	return true;
}

int main() {
	int t, u, count;
	long int n;
	
	cin >> t;
	u = t;
	while(t--) {
		memset(digit, false, 10);
		cin >> n;

		count = 1;
		if(n == 0) {
			cout << "Case #" << u-t << ": INSOMNIA" << endl;
		}
		else {
			long int no = n;
			while(1) {
				string s = to_string(no);
				//cout << s << endl;
				for(int j=0; j<s.length(); j++)
					digit[s.at(j)-48] = true;

				bool c = check();
				if(c == true)
					break;
				else
					no = n*(count++);
			}
			cout << "Case #" << u-t << ": " << no << endl; 
		}
	}

	return 0;
}