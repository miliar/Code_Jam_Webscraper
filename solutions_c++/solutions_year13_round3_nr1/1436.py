/*
 * codejam_R1C_A.cpp
 *
 *  Created on: May 12, 2013
 *      Author: leo
 */

#include <iostream>
#include <set>
using namespace std;
set<char> vouls;

int main() {
	vouls.insert('a');
	vouls.insert('e');
	vouls.insert('i');
	vouls.insert('o');
	vouls.insert('u');

	int tc, cnt, ccnt, a;
	string s;
	cin >> tc;

	for (int t = 1; t <= tc; ++t) {
		cin >> s >> a;
		cnt = 0;
		for (unsigned int i = 0; i < s.length() - a+1; ++i) {
			ccnt = 0;
			for (unsigned int j = i; j < s.length(); ++j) {
				ccnt++;
				if (vouls.find(s[j]) != vouls.end())
					ccnt = 0;
				if (ccnt == a) {
					cnt += s.length()-j;
					break;
				}

			}
		}
		cout << "Case #" << t << ": " << cnt << endl;
	}

	return 0;
}

