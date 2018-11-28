//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Jing Shan on 4/15/16.
//  Copyright © 2016 Jing Shan. All rights reserved.
//

#include <iostream>
#include <stdlib.h>
#include <vector>
#include <string>
#include <math.h>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
	string number(string &s) {
		string ans;
		if (s.empty()) return ans;
		vector<int> letters(26, 0);
		for (const char &c : s) {
			letters[c - 'A']++;
		}
		
		vector<int> count(10, 0);
		
		vector<string> word = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
		
		vector<char> remove = {'Z', 'W', 'U', 'X', 'G', 'O', 'H', 'F', 'S','I'};
		vector<int> index = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};
		for (int i = 0; i < 10; ++i) {
			int num = index[i];
			int uniqueCount = letters[remove[i] - 'A'];
			count[num] = uniqueCount;
			string w = word[num];
			for (const char &c : w) {
				letters[c-'A'] -= uniqueCount;
			}
		}
		
		for (int i = 0; i < 10; ++i) {
			if (count[i] > 0) {
				for (int j = 0; j < count[i]; ++j) {
					ans += ('0' + i);
				}
			}
		}
		return ans;
	}
};


int main(int argc, const char * argv[]) {
	Solution sol;
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		string s;
		cin >> s;
		string number = sol.number(s);
		cout << "Case #" << i + 1 <<": " << number << endl;
	}
}

