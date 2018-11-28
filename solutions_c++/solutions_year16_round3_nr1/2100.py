/*
 * SenateEvacuation.cpp
 *
 *  Created on: May 8, 2016
 *      Author: khanhtm
 */

#include "SenateEvacuation.h"

SenateEvacuation::SenateEvacuation() {
	// TODO Auto-generated constructor stub
	in = new ifstream("SenateEvacuation.in");
	out = new ofstream("SenateEvacuation.out");
}

SenateEvacuation::~SenateEvacuation() {
	// TODO Auto-generated destructor stub
}

void SenateEvacuation::execute() {
	int t;
	*in >> t;
	for (int i = 1; i <= t; ++i) {
		int n;
		*in >> n;
		int p[n];
		int sum = 0;
		for (int j = 0; j < n; ++j) {
			*in >> p[j];
			sum += p[j];
		}
		int curSum = sum;
		*out << "Case #" << i << ": ";
		while (curSum > 2) {
			int maxj = 0;
			for (int j = 0; j < n; ++j) {
				if (p[maxj] < p[j]) {
					maxj = j;
				}
			}
			p[maxj] -= 1;

			int maxj2 = 0;
			for (int j = 0; j < n; ++j) {
				if (p[maxj2] < p[j]) {
					maxj2 = j;
				}
			}
			p[maxj2] -= 1;
			int maxj3 = 0;
			for (int j = 0; j < n; ++j) {
				if (p[maxj3] < p[j]) {
					maxj3 = j;
				}
			}
			if (p[maxj3] <= curSum - 2 && curSum > 3) {
				*out << char('A' + maxj) << char('A' + maxj2) << " ";
				curSum -= 2;
			} else {
				*out << char('A' + maxj) << " ";
				p[maxj2] += 1;
				curSum -= 1;
			}
		}
		for (int j = 0; j < n; ++j) {
			if (p[j] > 0)
				*out << char('A' + j);
		}
		*out << endl;
	}
}
