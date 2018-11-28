//
//  main.cpp
//  codejam4
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

using namespace std;

int T, K, C, S;
unsigned long long L[100];

void solve() {
	for (int i = 0; i < S; ++i) {
		unsigned long long idx = 1;
		for (int c = 1; c <= C; ++c) {
			unsigned long long p = 1;
			for (int j = 1; j <= c-1; ++j) {
				p = p * (unsigned long long)K;
			}
			idx += (unsigned long long)i * p;
		}
		L[i] = idx;
	}
}

int main(int argc, const char * argv[]) {
	
	ifstream readFile;
	ofstream writeFile;
	readFile.open("D-small-attempt1.in");
	writeFile.open("output.txt");
	
	if (readFile.is_open()) {
		readFile >> T;
		for (int i = 1; i <= T; i++) {
			readFile >> K >> C >> S;
			printf("Case #%d: ", i);
			writeFile << "Case #" << i << ": ";
			solve();
			for (int i = 0; i < S; ++i) {
				printf("%llu ", L[i]);
				writeFile << L[i] << " ";
			}
			printf("\n");
			writeFile << "\n";
		}
	}
	
	readFile.close();
	writeFile.close();
	return 0;
}
