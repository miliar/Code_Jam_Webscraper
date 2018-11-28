/*
 * CountingSheep.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: khanh
 */

#include "CountingSheep.h"

CountingSheep::CountingSheep() {
	in = new ifstream("CountingSheep.in");
	out = new ofstream("CountingSheep.out");
}

CountingSheep::~CountingSheep() {
}

int CountingSheep::counting(int n) {
	int flag = 0;
	int base = n;
	while (!checkFullNumber(flag)) {
		int tmp = n;
		while (tmp>0) {
			int mod = tmp % 10;
			tmp = tmp/10;
			flag = flag | (1<<mod);
		}
		if (checkFullNumber(flag)) break;
		n = n + base;
	}
	return n;
}

bool CountingSheep::checkFullNumber(int flag) {
	return flag==1023;
}

void CountingSheep::addFlag(int num, int& flag) {

}

void CountingSheep::execute() {
	int t;
	*in >> t;
	for (int i = 1; i <= t; ++i) {
		int n;
		*in >> n;
		if (n==0) {
			*out << "Case #" << i << ": " << "INSOMNIA" << endl;
		} else {
			*out << "Case #" << i << ": " << counting(n) << endl;
		}
	}
}
