#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<iostream>

using namespace std;

int main(){
	int testcase_num = 1;
	int srow;
	int x[17];
	cin >> testcase_num;
	for (int tn = 1; tn <= testcase_num; tn++) {
		int input;
		int snum;
		cin >> srow;
		bool cardS = false;
		bool badMgcian = false;

		for (int i = 1; i <= 16; i++){
			x[i] = 0;
		}
		for (int r = 1; r <= 4; r++) {
			for (int c = 1; c <= 4; c++) {
				cin >> input;
				if (r == srow) {
					x[input] = 1;
				}
			}
		}
		cin >> srow;
		for (int r = 1; r <= 4; r++) {
			for (int c = 1; c <= 4; c++) {
				cin >> input;
				if (r == srow) {
					if (x[input] == 1) {
						if (cardS) {
							badMgcian = true;
						}
						snum = input;
						cardS = true;
					}
				}
			}
		}

		cout << "Case #" << tn << ": ";
		if (badMgcian) {
			cout << "Bad magician!";
		}
		else if (cardS) {
			cout << snum;
		}
		else {
			cout << "Volunteer cheated!";
		}
		cout << endl;
	}


	return 0;
}