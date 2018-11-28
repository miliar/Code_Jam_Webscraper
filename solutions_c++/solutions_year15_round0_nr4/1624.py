#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
using namespace std;

int main() {


	int T;
	cin >> T;
	int target[3] = {105, 107, -49};
	for (int t = 1; t <= T; t++) {
		string result;
		int X, R, C;
		cin >> X >> R >> C;
		int r = min(R, C);
		int c = max(R, C);
		int a = r * c;
		if (a % X != 0) {
			result = "RICHARD"; //"GABRIEL" :
		}
		else if (X == 1) {
			result = "GABRIEL";
		}
		else if (X == 2) {
			result = "GABRIEL";
		}
		else if (X == 3) {
			result = (r == 1) ? "RICHARD" : "GABRIEL";
		}
		else if (X == 4) {
			if (r == 1) {
				result =  "RICHARD";
			}
			else if (r == 2) {
				result =  "RICHARD";
			}
			else if (r >= 3) {
				result =  "GABRIEL";
			}
		}


		cout << "Case #" << t << ": " << result << endl;
	}

	return 0;
}
