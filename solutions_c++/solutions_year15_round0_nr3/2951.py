/*
 * problem-C-small.cpp
 *
 *  Created on: Apr 11, 2015
 *  Author: Karim Mostafa
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <math.h> 
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ext/numeric>
#include <memory.h>
#include <valarray>
#include <limits>
using namespace std;

const int INF = numeric_limits<int>::max();

int is[10001];
int ks[10001];

char c;
int sign = 1;

void check(char c1, char c2) {
	if (c1 == 'i' && c2 == 'i') {		////////////////// i
		c = '1';
		sign *= -1;
	} else if (c1 == 'i' && c2 == 'j') {
		c = 'k';
	} else if (c1 == 'i' && c2 == 'k') {
		c = 'j';
		sign *= -1;
	} else if (c1 == 'i' && c2 == '1') {
		c = 'i';
	} else if (c1 == 'j' && c2 == 'i') {	///////////////// j
		c = 'k';
		sign *= -1;
	} else if (c1 == 'j' && c2 == 'j') {
		c = '1';
		sign *= -1;
	} else if (c1 == 'j' && c2 == 'k') {
		c = 'i';
	} else if (c1 == 'j' && c2 == '1') {
		c = 'j';
	} else if (c1 == 'k' && c2 == 'i') {	////////////////// k
		c = 'j';
	} else if (c1 == 'k' && c2 == 'j') {
		c = 'i';
		sign *= -1;
	} else if (c1 == 'k' && c2 == 'k') {
		c = '1';
		sign *= -1;
	} else if (c1 == 'k' && c2 == '1') {
		c = 'k';
	} else if (c1 == '1' && c2 == 'i') {	////////////////// 1
		c = 'i';
	} else if (c1 == '1' && c2 == 'j') {
		c = 'j';
	} else if (c1 == '1' && c2 == 'k') {
		c = 'k';
	} else if (c1 == '1' && c2 == '1') {
		c = '1';
	}

}

int main() {
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	int l, x;
	string str;
	string input;

	cin >> t;
	bool found = false;

	for (int z = 1; z <= t; z++) {
		cin >> l >> x;
		cin >> str;
		input = "";
		found = false;
		memset(is, false, sizeof is);
		memset(ks, false, sizeof ks);

		for (int i = 0; i < x; i++)
			input += str;

		int sz = input.size();
		if (sz < 3) {
			cout << "Case #" << z << ": " << "NO" << endl;
			continue;
		}

		sign = 1;					///////////// check is
		c = input[0];
		if (c == 'i')
			is[0] = true;

		for (int i = 1; i < sz - 2; i++) {
			check(c, input[i]);

			if (c == 'i' && sign == 1)
				is[i] = true;
		}
		sign = 1;					////////////// check ks
		c = input[sz - 1];
		if (c == 'k')
			ks[sz - 1] = true;

		for (int i = sz - 2; i > 1; i--) {
			check(input[i], c);

			if (c == 'k' && sign == 1)
				ks[i] = true;
		}

		for (int i = 0; i < sz - 2; i++) {			//////// main loop
			if (!is[i])
				continue;
			sign = 1;
			int j = i + 1;
			c = input[j++];

			if (c == 'j' && sign == 1 && ks[i+2]) {
				found = true;
				break;
			}
			for (int k = i + 3; k < sz; k++) {
				check(c, input[j++]);

				if (!ks[k])
					continue;

				if (c == 'j' && sign == 1) {
					found = true;
					break;
				}

			}

			if (found)
				break;

		}

		if (found)
			cout << "Case #" << z << ": " << "YES" << endl;
		else
			cout << "Case #" << z << ": " << "NO" << endl;

	}

	return 0;
}
