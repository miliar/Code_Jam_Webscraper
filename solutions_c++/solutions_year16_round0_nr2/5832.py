/*
 * p2.cpp
 *
 *  Created on: 9 Apr 2016
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

char GetFlippedValue(char ch) {

	if (ch == '-')
		return '+';

	return '-';
}

void Flip(string& S, int number) {

	for (int i=0;i<=number/2;++i) {
		char temp = S[i];
		S[i] = GetFlippedValue(S[number - i]);
		S[number - i] = GetFlippedValue(temp);
	}
}

int GetMinNumberOfFlips(string& S) {

	int flips = 0;

	if (S.size() == 1) {
		if (S[0] == '+')
			return 0;
		else
			return 1;
	}

	for (int i=S.size()-1;i>=0;--i) {
		if (S[i] == '+') {
			continue;
		}else {
			if (S[0] == '+') {
				int j = 0;
				while (S[j] == '+') {
					++j;
				}

				Flip(S, j);
				++flips;
			}

			Flip(S, i);
			++flips;
		}
	}

	return flips;
}

int main() {

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	string S;

	for (int i = 1; i <= T; ++i) {
		cin>>S;
		cout<<"Case #"<<i<<": "<<GetMinNumberOfFlips(S)<<endl;
	}



	return 0;
}


