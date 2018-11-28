/*
 * A.StandingOvation.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: Yasser
 */

#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main() {
	freopen("test.in","rt",stdin);
	freopen("results.txt","wt",stdout);

	int T,n;
	string s;
	cin >> T;
	for(int tt=0;tt<T;tt++) {
		cin >> n >> s;
		int tot = 0;
		int sol = 0;
		for(int i=0;i<s.size();i++) {
			if(tot + sol < i){
				sol += i - ( tot+sol);
			}

			tot += (s[i] - '0');
		}

		printf ("Case #%d: %d\n", tt+1, sol);
	}
	return 0;
}
