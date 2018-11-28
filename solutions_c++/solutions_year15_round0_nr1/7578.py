/*
 * StandingOvation.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: saha
 */

#include <bits/stdc++.h>

using namespace std;

typedef vector<int> VI;
typedef long long LL;

int main () {
	int T, Smax;
	string s;
	cin >> T;
	int cs = 1;
	while(T--) {
		cin >> Smax;
		cin >> s;
		VI N;
		for(int i=0; i<=Smax ; i++)
			N.push_back(s[i]-'0');
		LL count = 0;
		int Ni = N[0];
		for(int j=1; j<=Smax ; j++) {
			if(j-Ni > 0) {
				count += (j-Ni);
				Ni = j;
			}
			Ni += N[j];
		}

		cout << "Case #" << cs << ": " << count << endl;
		cs++;
	}
}


