// testerarea.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <conio.h>
#include <cmath>

using namespace std;


int main()
{
	bool ar[10]{};
	ofstream mf;
	ifstream rf;
	rf.open("test.txt");
	mf.open("output.txt");

	unsigned long int t;
	string s;
	getline(rf, s);
	t = stoi(s, nullptr, 10);
	for (unsigned long int x = 0; x < t;x++) {
		if (x)mf << endl;
		unsigned long int n, flag, temp, c, temp1;
		getline(rf, s);
		n = stoi(s, nullptr, 10);

		flag = 1;
		c = 2;
		if (n == 0) {
			mf << "Case #" << x + 1 << ": " << "INSOMNIA";
			continue;
		}
		temp = n;
		while (flag) {
			temp1 = n;
			while (n) {
				ar[n % 10] = true;
				n /= 10;
			}
			for (int i = 0; i < 10; i++) {
				if (ar[i] == false) {
					flag = 1;
					i = 10;
				}
				else {
					flag = 0;
				}
			}
			if (flag) {
				n = temp*c;
				c++;
			}
			else {
				mf << "Case #" << x + 1 << ": " << temp1;
			}
		}
		for (int i = 0; i < 10; i++) {
			ar[i] = false;
		}
	}
	rf.close();
	mf.close();

	return 0;

}