//
//  main.cpp
//  counting-sheep
//
//  Created by Harshal Sheth on 4/8/16.
//  Copyright © 2016 Harshal Sheth. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

typedef long long ll;

bool addDigit(int d, vector<bool>& digits) {
	if (digits[d] == false) {
		digits[d] = true;
		return true;
	}
	else return false;
}

void run(ll n) {
	if (n == 0) {
		cout << "INSOMNIA";
		return;
	}
	
	vector<bool> digits(10, false);
	short seen = 0;
	
	for (ll m = 1; true; m++) {
		ll counted = m * n;
		string num = to_string(counted);
		
		for (int i = 0; i < num.size(); i++) {
			char c = num[i];
			if (addDigit(c - '0', digits))
				seen++;
		}
		
		if (seen == 10) {
			cout << counted;
			return;
		}
	}
}

int main() {
	ifstream fin("sheep.in"); assert(fin);
	
	ll N;
	fin >> N;
	for (ll i = 0; i < N; i++) {
		ll n;
		fin >> n;
		cout << "Case #" << i+1 << ": ";
		run(n);
		cout << '\n';
	}
	
	return 0;
}
