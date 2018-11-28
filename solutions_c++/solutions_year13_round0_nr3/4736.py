/*
 * codejam_qual_C.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: leo
 */

#include <iostream>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <fstream>

using namespace std;

int ten[10];
int cnt = 0;
typedef long long ll;
int tc;
ll max_num, min_num;

inline int digit_cnt(int i) {
	int cnt = 1;
	while ((i /= 10) > 0)
		cnt++;
	return cnt;
}

inline bool is_palindrome(ll n) {
	stringstream ss;
	ss << n;
	string s = ss.str();
	int i = 0, j = s.length() - 1;
	while (i < j && s[i] == s[j])
		i++,j--;

	return i >= j;
}

inline void check(ll i) {
	ll temp = (ll) (i) * i;

//	if (temp <= max_num && temp >= min_num)
//		cout<<i<<" " <<temp<<" "<<is_palindrome(temp)<<endl;
	if (temp <= max_num && temp >= min_num && is_palindrome(temp))
		cnt++;
}

void gen_palindromes(int i, int j, int n) {
	if (i > j) {
		check(n);
	} else if (i == j) {
		for (int var = 0; var < 10; ++var) {
			n += var * ten[i];
			check(n);
			n -= var * ten[i];
		}
	} else
		for (int k = 0; k < 10; ++k) {
			// set digit at position i and j to k
			if (i == 0 && k == 0)
				continue;
			n += k * ten[i] + k * ten[j];
			gen_palindromes(i + 1, j - 1, n);
			n -= k * ten[i] + k * ten[j];
		}
}

int main() {
	cin>>tc;
	ten[0] = 1;
	for (int i = 1; i < 10; ++i)
		ten[i] = ten[i - 1] * 10;

	ofstream cout;
	cout.open("/home/leo/Desktop/c.out");
	int n,m;
	for (int t = 1; t <= tc; ++t) {
		cnt = 0;
		cin >> min_num >> max_num;
		n = sqrt(min_num);
		m = sqrt(max_num);
		int l1 = digit_cnt(n);
		int l2 = digit_cnt(m);

		for (int i = l1; i <= l2; ++i)
			gen_palindromes(0, i - 1, 0);

		cout << "Case #" << t << ": " << cnt << endl;

	}
	cout.close();
	return 0;
}

