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

using namespace std;

class Solution {
private:
	void countDigit (int N, vector<int> &countArray, int &digitCount) {
		while (N > 0) {
			int digit = N % 10;
			if (countArray[digit] == 0) {
				++digitCount;
			}
			countArray[digit]++;
			N /= 10;
		}
	}
public:
	int countSheep(int N) {
		if (N == 0) {
			return 0;
		}
		int curNum = N;
		vector<int> count(10, 0);
		int digitCount = 0;
		while (true) {
			countDigit(curNum, count, digitCount);
			if (digitCount == 10) break;
			curNum += N;
		}
		return curNum;
	}
};


int main(int argc, const char * argv[]) {
	Solution sol;
	int T;
	cin >> T;
	int i = 0, N;
	vector<int> testCase(T, 0);
	while (i < T) {
		cin >> N;
		testCase[i] = N;
		++i;
	}
	
	for (int i = 0; i < T; ++i) {
		int res = sol.countSheep(testCase[i]);
		if (res == 0) {
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
		}
		else {
			cout << "Case #" << i+1 << ": " << res << endl;
		}
	}
}
