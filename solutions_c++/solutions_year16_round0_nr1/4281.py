/*
 * =====================================================================================
 *
 *       Filename:  A.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/ 9/2016 12:40:41 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */

#include <iostream>
using namespace std;

int cnt[10];

int clear() {
	for (int i=0; i<10; i++) cnt[i]=0;
}

// no zero?
bool check() {
	bool r = true;
	for (int i=0; i<10 && r; i++) r=(cnt[i]>0);
	return r;
}

int iter(int n) {
	if (n <= 0) return -1;
	int r = 0;
	int m = 0;
	while (!check()) {
		m += n;
		for (int i=m;i>0;i/=10) {
			cnt[i%10]++;
		}
		r++;
	}
	return m;
}

int main() {
	int n;
	cin >> n;
	for (int i=0; i<n; i++) {
		int m;
		cin >> m;
		clear();
		int r = iter(m);
		if (r < 0) {
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		} else {
			cout << "Case #" << i+1 << ": " << r << endl;
		}
	}

	return 0;
}

