#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int a,b;
		vector<int> poss;
		cin >> a;
		for (int j = 1; j <= 4; j++) {
			int w,x,y,z;
			cin >> w >> x >> y >> z;
			if (j == a) 
				poss.push_back(w),poss.push_back(x),poss.push_back(y),poss.push_back(z);
		}
		cin >> b;
		int found = 0;
		for (int j = 1; j <= 4; j++) {
			int w,x,y,z;
			cin >> w >> x >> y >> z;
			if (j == b) {
				for (int k = 0; k < 4; k++) {
					if (poss[k] == w && found) {
						found = -1;
					} else if (poss[k] == x && found) {
						found = -1;
					} else if (poss[k] == y && found) {
						found = -1;
					} else if (poss[k] == z && found) {
						found = -1;
					} else if (poss[k] == w) {
						found = w;
					} else if (poss[k] == x) {
						found = x;
					} else if (poss[k] == y) {
						found = y;
					} else if (poss[k] == z) {
						found = z;
					}
				}
			}
		}
		if (found && found != -1)
			cout << "Case #" << i << ": " << found << endl;
		else if (found != -1)
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		else
			cout << "Case #" << i << ": Bad magician!" << endl;
	}
	return 0;
}
