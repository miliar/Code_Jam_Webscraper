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
#include <math.h>

using namespace std;

class Solution {
private:

public:
	vector<long long> cleanTiles(int K, int C, int S) {
		vector<long long> sets;
		// if first level, must clean all of them to see
		if (C == 1) {
			if (S < K) return sets; // return empty
			else {
				for (int i = 0; i < K; ++i) {
					sets.push_back(i+1);
				}
				return sets;
			}
		}
		int minWorkers = (int)ceil((double)K/(double)C);
		if (S < minWorkers) return sets;
		
		// will have total minWorkers number, each is C digits number in base of K
		// convert it in to number in base of 10
		
		for (int i = 0; i < minWorkers; ++i) {
			int start = i * C;
			long long index = 0;
			int k = 0;
			for (int j = min(C + start, K); j > start; --j) {
				index += (long long)((j-1) * (long long)pow(K, k++));
			}
			++index;
			sets.push_back(index);
		}
		return sets;
	}
};


int main(int argc, const char * argv[]) {
	Solution sol;
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int K, C, S;
		cin >> K >> C >> S;
		vector<long long> ans = sol.cleanTiles(K, C, S);
		if (ans.empty()) {
			cout << "Case #" << i+1 <<": IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << i+1 <<":";
			for (int i = 0; i < ans.size(); ++i) {
				cout << " " << ans[i];
			}
			cout << endl;
		}
	}
}
