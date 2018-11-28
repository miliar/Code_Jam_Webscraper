/*
 * Q1.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: Neil
 */

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <iomanip>

using namespace std;

#define EPS 1e-7

int test;

#define LL long long

double C;
double F;
double X;
double R;

int main() {


	freopen("test.in","r", stdin);
	freopen("Q2.out","w",stdout);

	cin >> test;

	for(int t = 0; t < test; t++) {
		cout << "Case #" << t + 1 << ": ";

		cin >> C >> F >> X;
		R = 2;

		double prev = 0;

		while(1) {
			double option1 = prev + X/R;

			double option2 = prev + C/R + X/(R + F);


			if(option2 + EPS < option1) {
				prev += C/R;
				R += F;
			} else {
				cout << fixed << setprecision(7) << option1 << endl;
				break;
			}

		}


	}

	return 0;
}


