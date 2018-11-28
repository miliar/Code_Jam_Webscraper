/*
 * p1.cpp
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

void UpdateDigits (vector<bool>& dig, long long N) {

	while (N > 0) {

		int d = N % 10;
		N = N / 10;
		dig[d] = true;
	}
}


bool CheckDigits(const vector<bool>& dig) {

	for (int i=0;i<dig.size();++i) {
		if (dig[i] == false)
			return false;
	}
	return true;
}


long long LastNumber (int N) {

	vector<bool> dig(10, false);

	UpdateDigits(dig, N);
	long long last = N;

	while (!CheckDigits(dig)) {

		last += N;
		UpdateDigits(dig, last);
	}

	return last;

	//return -1;
}

int main() {

	freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

	int T, N;
	cin >> T;
	//cout<<T<<endl;

	for (int i=1; i<=T; ++i) {
		cin >> N;
		//cout<<N<<endl;

		if (N == 0) {
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}

		long long res = LastNumber(N);

		cout<<"Case #"<<i<<": ";
		if (res == -1)
			cout<<"INSOMNIA"<<endl;
		else
			cout<<res<<endl;
	}


	return 0;
}


