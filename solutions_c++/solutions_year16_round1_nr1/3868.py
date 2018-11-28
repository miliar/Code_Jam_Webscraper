/*
 * p1.cpp
 *
 *  Created on: 16 Apr 2016
 *      Author: Clem
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <set>
#include <queue>
#include <climits>
#include <list>
#include <utility>
#include <cstdio>

using namespace std;

int main() {

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin>>T;
	string S;

	for (int i=1;i<=T;++i) {
		cin>>S;
		string sol = "";
		char ch = S[0];
		sol += ch;

		for (int j=1;j<S.size();++j) {
			if (S[j] >= ch) {
				ch = S[j];
				sol = ch + sol;
			}else {
				sol = sol + S[j];
			}
		}
		cout<<"Case #"<<i<<": "<<sol<<endl;
	}

	return 0;
}


