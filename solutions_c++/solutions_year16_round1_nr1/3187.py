//
//  main.cpp
//  Round1-1
//
//  Created by 김 균태 on 2016. 4. 16..
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
string S;

string solve() {
	string ret;
	ret = S[0];
	
	for (int i = 1; i < S.length(); ++i) {
		if (S[i] >= ret[0]) {
			ret = S[i] + ret;
		} else {
			ret = ret + S[i];
		}
	}
	
	return ret;
}

int main(int argc, const char * argv[]) {
	ifstream readFile;
	ofstream writeFile;
	readFile.open("A-large.in");
	writeFile.open("output.txt");
	
	if (readFile.is_open()) {
		readFile >> T;
		for (int i = 1; i <= T; i++) {
			readFile >> S;
			
			string ans = solve();
			
			printf("Case #%d: %s\n", i, ans.c_str());
			writeFile << "Case #" << i << ": " << ans << "\n";
		}
	}
	
	readFile.close();
	writeFile.close();
	return 0;
}

