//============================================================================
// Name        : sidesjamcoin.cpp
// Author      : Abhidnya
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <cmath>
#include <stack>
#include <vector>

using namespace std;
stack <int> st;

long long int conv_base(long long int x, int b1, int b2)
{
	long long int out = 0, in, i;
	for (i = 0; x; i++) {
		in = x % b1;
		out += (in * pow(b2, i));
		x /= b1;
	}
	return out;
}

long long int is_prime(long long int n)
{
	long long int i = 0, flag = 0, sq = sqrt(n);
	for (i = 2; i < sq; i++) {
		if (n % i == 0) {
			flag = 1;
			break;
		}
	}
	if (flag == 0)
		return 0;
	if (flag == 1)
		return i;
}

int main()
{
	long long int t, n, j;
	long long int in, start, end, num, out;
	long long int i, k, l, m, flag;
	vector <long long int> vec;

	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	cin >> t;

	for (l = 0; l < t; l++) {

	    	cin  >> n >> j;
	    	in = 0; start = pow(2, n - 1) + 1; end = pow(2, n);
	    	num = 0; out = 0;
		flag = 0;
		for (in = start, i = 0; i < j; in += 2, i++) {
			//cout << "NUM" << conv_base(in, 2, 10) << endl;
			for (k = 2; k <= 10; k++ ) {
				num = conv_base(in, 2, k);
				//cout << "num " << num << "in base" << k << endl;
				out = is_prime(num);
				if (out > 0) {
					//cout << "Not prime: "<< out << endl;
					vec.push_back(out);
				} else {
					vec.clear();
				    	break;
				}
			}
			if (vec.size() == 9) {
				if (flag == 0) {
					cout << "Case #" << i + 1 << ":" <<endl;
					flag = 1;
				}
				cout << num;
				vector<long long int>::iterator v = vec.begin();
				do {
					cout << " " << *v;
					v++;
				} while( v != vec.end());
				cout << endl;
			} else {
				i--;
			}
		}
	}
	return 0;
}
