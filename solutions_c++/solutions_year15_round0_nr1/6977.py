//
//  main.cpp
//  Ovation
//
//  Created by Harshal Sheth on 4/10/15.
//  Copyright (c) 2015 Harshal Sheth. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
	int TESTs;
	cin >> TESTs;
	for (int q = 0; q < TESTs; q++) {
		int N;
		cin >> N;
		//cout << N << "\n";
		
		int standing = 0;
		int needed = 0;
		for (int x = 0; x <= N; x++) {
			char c;
			cin >> c;
			int num = c - '0';
			//cout << num << ' ';
			
			if (x <= standing) {
				// enough already
				standing += num;
				//cout << standing << '\n';
			} else {
				// add more
				int add = x - standing;
				//cout << standing << ' ' << x << '\n';
				needed += add;
				standing += add + num;
			}
		}
		
		cout << "Case #" << q+1 << ": " << needed << "\n";
	}
	
	return 0;
}
