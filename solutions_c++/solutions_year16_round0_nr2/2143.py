//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Jing Shan on 4/8/16.
//  Copyright © 2016 Jing Shan. All rights reserved.
//

#include <iostream>
#include <stdlib.h>
#include <vector>
#include <string>

using namespace std;

class Solution {
private:
	
public:
	int flipPancakes (string &s) {
		int len = (int)s.size();
		int flips[len+1];
		memset(flips, 0, sizeof(flips));
		for (int i = 0; i < len; ++i) {
			char prev = (i == 0 ? '+' : s[i-1]);
			if (s[i] == prev || s[i] == '+') {
				flips[i+1] = flips[i];
			}
			else {
				if (i == 0) flips[i+1] = 1;
				else flips[i+1] = flips[i] + 2;
			}
		}
		return flips[len];
	}
};


int main(int argc, const char * argv[]) {
	Solution sol;
	int T;
	cin >> T;
	int i = 0;
	vector<string> testCase(T, "");
	string line;
	while (i < T) {
		cin >> line;
		testCase[i++] = line;
	}
	
	for (int j = 0; j < T; ++j) {
		int res = sol.flipPancakes(testCase[j]);
		cout << "Case #" << j+1 << ": " << res << endl;
	}
}
