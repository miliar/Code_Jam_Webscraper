//
//  main.cpp
//  jamcoin
//
//  Created by Harshal Sheth on 4/9/16.
//  Copyright © 2016 Harshal Sheth. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>       /* sqrt */
using namespace std;

typedef long long ll;

string to_base(ll num, ll base) {
	string ans = "";
	
	while (num > 0) {
		ll rem = num % base;
		num = num / base;
		ans = to_string(rem) + ans;
	}
	
	return ans;
}

ll from_base(string num, ll base) {
	ll ans = 0;
	
	for (int i = 0; i < num.length(); i++) {
		ans *= base;
		ans += num[i] - '0';
	}
	
	return ans;
}

ll get_divisor(ll num) {
	for (ll d = 2; d <= sqrt(num); d++)
		if (num % d == 0)
			return d;
	
	return 0;
}

bool check(ll test) {
	string str = to_base(test, 2);
	
	string ans = "";
	ans += str;
	
//	cerr << test << '\n';
	for (int i = 2; i <= 10; i++) {
		ll interp = from_base(str, (ll)i);
//		cerr << interp << '\n';
		ll div = get_divisor(interp);
		if (div == 0)
			return false;
		ans += " " + to_string(div);
	}
	
	cout << ans << '\n';
	return true;
}

void run(ll N, ll J) {
	int found = 0;
	
	for (ll test = (1 << (N-1)) + 1; found < J; test += 2) {
//		cerr << test << ' ' << from_base(to_base(test, 2), 2) << '\n';
		if (check(test))
			found++;
	}
}

int main() {
	ifstream fin("jamcoin.in"); assert(fin);
	
	int T;
	fin >> T;
	
	for (int i = 0; i < T; i++) {
		cout << "Case #" << i+1 << ":\n";
		ll N, J;
		fin >> N >> J;
		run(N, J);
	}
	
	return 0;
}