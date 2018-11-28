/*
 * B.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: nmarwan
 */

#include <iostream>
#include <sstream>
#include <set>
#include <algorithm>

using namespace std;

void print (int n) {
	freopen ("a.in", "wt", stdout);
	cout << n << endl;
	for (int i=0 ; i < n ; i++) {
		cout << i << endl;
	}

}
int main () {
	freopen ("a.in", "rt", stdin);
	freopen ("a.out", "wt", stdout);

	int t;
	cin >> t;
	for (int tt =1  ; tt <= t ; tt++){
		cout << "Case #" << tt << ": ";
		string s;
		cin >> s;

		int ans = 0;
		string ss = "-+";
		for (int i=s.size()-1 ; i >= 0 ; --i) {
			if (s[i] == ss[ans%2]) {
				ans ++;
			}
		}
		cout << ans << endl;
	}
}
