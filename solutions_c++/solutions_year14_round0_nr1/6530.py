#include <iostream>
#include <sstream>
#include <string>

using namespace std;

string solve() {
	int R1, R2;
	int temp;
	int c1[4];
	int c2[4];

	int r, rc=0;

	cin >> R1;
	for(int i=0;i<4;i++) {
		for(int j=0;j<4;j++) {
			cin >> temp;
			if(R1 - 1 == i) 
				c1[j] = temp;
		}
	}

	cin >> R2;
	for(int i=0;i<4;i++) {
		for(int j=0;j<4;j++) {
			cin >> temp;
			if(R2 - 1 == i) 
				c2[j] = temp;
		}
	}

	for(int i=0;i<4;i++) {
		for(int j=0;j<4;j++) {
			if(c1[i] == c2[j]) {
				r = c1[i];
				rc++;
			}
		}
	}
	if(0 == rc)
		return "Volunteer cheated!";
	if(rc > 1)
		return "Bad magician!";

	ostringstream ss;
    ss << r;
	return ss.str();
}

int main() {
	int T;
	cin >> T;
	for (int p = 1; p <= T; p++) {
		cout << "Case #" << p << ": " << solve() << endl;
	
	}
}