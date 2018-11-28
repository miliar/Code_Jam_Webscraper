#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<string>
#include<stdlib.h>
using namespace std;

int main() {

	freopen("C:/Users/HP/Desktop/src.txt", "r", stdin);
	freopen("C:/Users/HP/Desktop/out.txt", "w", stdout);
	int t, x, r, c;

	cin >> t;

	for (int i = 0; i<t; i++){
		cin >> x >> r >> c;

		if ((x == 4 && r == 4 && c == 3) || (x == 4 && r == 3 && c == 4) || (x == 4 && r == 4 && c == 4)){
			cout << "Case #" << i + 1 << ": " << "GABRIEL" << endl;
		}
		else if ((x == 3 && r == 1 && c == 3) || (x == 3 && r == 3 && c == 1)){
			cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
		}
		else if ((r%x == 0 || c%x == 0) && x != 4){
			cout << "Case #" << i + 1 << ": " << "GABRIEL" << endl;
		}

		else {
			cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
		}


	}


	return 0;
}