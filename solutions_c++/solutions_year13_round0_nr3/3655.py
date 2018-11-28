/*
 * main.cpp
 *
 *  Created on: 12/04/2013
 *      Author: Eden
 */
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int digitsNum(int x) {
	if (x == 0)
		return 1;
	int i = 0;
	while (x != 0) {
		x = x / 10;
		i++;
	}
	return i;
}
int iThDigit(int num, int i) {
	for (int j = 0; j < i; j++)
		num = num / 10;
	return num % 10;
}
bool palindrome(int x) {
	int digits = digitsNum(x);
	for (int i = 0; i < digits / 2; i++) {
		if (iThDigit(x, i) != iThDigit(x, digits - 1 - i))
			return false;
	}
	return true;
}

int main() {
	ifstream myfile("C:\\users\\eden\\C-small-attempt0.in");
	ofstream output("C:\\users\\eden\\out.txt");
	if (!myfile || !output) {
		cout << "FAIL";
		return 0;
	}
	int T, low, high, lowRoot, highRoot, sum;
	double res;
	myfile >> T;
	for (int i = 1; i <= T; i++) {
		sum = 0;
		output << "Case #" << i << ": ";
		myfile >> low >> high;
		res = sqrt(low);
		lowRoot = (int) res;
		if (lowRoot != res)
			lowRoot++;
		res = sqrt(high);
		highRoot = (int) res;
		for (int j = lowRoot; j <= highRoot; j++) {
			if (palindrome(j) && palindrome(j * j))
				sum++;
		}

		output << sum << endl;
	}
	myfile.close();
	output.close();
	return 0;
}

