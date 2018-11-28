//
//  main.cpp
//  codejam2
//
//  Created by 김 균태 on 2016. 4. 9..
//  Copyright © 2016년 ethan. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <vector>
#include <deque>
#include <queue>
#include <unordered_map>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <string>

using namespace std;

int T;
string stack;

int solve() {
	int ret = 0;
	int N = (int)stack.length();
	int cur = 0;
	char now = stack[0];
	while (cur+1 < N) {
		++cur;
		if (stack[cur] != now) {
			now = stack[cur];
			ret++;
		}
		now = stack[cur];
	}
	if (now == '-') {
		ret++;
	}
	
	return ret;
}

int main(int argc, const char * argv[]) {
	ifstream readFile;
	ofstream writeFile;
	readFile.open("B-large.in");
	writeFile.open("output.txt");
	
	if (readFile.is_open()) {
		readFile >> T;
		for (int i = 1; i <= T; i++) {
			readFile >> stack;
			int ans = solve();
			printf("Case #%d: %d\n", i, ans);
			writeFile << "Case #" << i << ": " << ans << "\n";
		}
	}
	
	readFile.close();
	writeFile.close();
	return 0;
}
