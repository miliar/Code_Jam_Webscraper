/*
 * A.cpp
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
//	print(1000001);
//	return 0;

	int t;
	cin >> t;
	for (int tt =1  ; tt <= t ; tt++){
		cout << "Case #" << tt << ": ";
		int n;
		cin >> n;
		if (!n) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		int m = n;
		set<char> st;
		while (true) {
			stringstream ss;
			ss << n;
			string str;
			ss >> str;

			for(int i=0 ; i < str.size() ; i++) {
				st.insert(str[i]);
			}

			if (st.size() == 10) {
				cout << n << endl;
				break;
			}
			n += m;
		}
	}
}
