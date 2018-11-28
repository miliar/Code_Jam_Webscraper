#include<iostream>
#include <string>
#include <cstdio>
#include <fstream>

using namespace std;

int main() {

	freopen("D-small-attempt3.in", "r", stdin);
	freopen("output2.txt", "w", stdout);
	int t = 0;
	string str;
	cin >> t;
	int i=1;
	while (t--) {
		

		int R, C, X;
		cin >> X >> R >> C;
		if (R > C) {
			int temp = C;
			C = R;
			R = temp;
		}
		bool ans = false;
		if (R * C % X != 0) {
			ans = false;
		} else {
			if (X < 3) {
				ans = true;
			} else if ((X == 3) && (R == 2) && (C == 3)
					|| (X == 3) && (R == 3) && (C == 3)
					|| (X == 3) && (R == 3) && (C == 4)
					|| (X == 4) && (R == 3) && (C == 4)
					|| (X == 4) && (R == 4) && (C == 4))
				ans = true;
			
		}
		
		if (ans){
			
			cout <<"Case #"<< i <<": "<< "GABRIEL" << endl;
			i += 1;
		}
		else{
			cout << "Case #"<< i <<": "<< "RICHARD" << endl;
		i += 1;
		}
	}
	return 0;
}