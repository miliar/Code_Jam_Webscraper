#include <iostream>
#include <stdlib.h>
using namespace std;
int main() {
	int t;
	int i;
	int k;
	int j;
	int n;
	int left;
	int tempn;
	int array[10];
	int carry;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
			continue;
		}
		for (k=0; k< 10; k++) {
			array[k] = 0;
		}
		left = 10;
		for (k=1; k<=100; ++k) {
			j = k*n;
			tempn = k*n;
			while (1) {
			carry = tempn % 10;
			if (array[carry] == 0) {
				array[carry] = 1;
				left--;
			}
			if (tempn != 0) {
				tempn = tempn/10;
			}
			if (tempn == 0) {
				break;
			}
			}
			if (left == 0) {
				/*	
				cout << n << endl;
				for (k = 0; k< 10; ++k) {
					cout << "Array " << k << ": " << array[k] << endl;
				}
				*/
				cout << "Case #" << i << ": " << j << endl;
				break;
			}
			if (left != 0 && k >= 100) {
				cout << "Case #" << i << ": " << "INSOMNIA" << endl;
			}
	
		}
	
	}
	return 0;
}
