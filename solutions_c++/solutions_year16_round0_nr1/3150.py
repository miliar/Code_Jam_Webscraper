//
//  main.cpp
//  CodeJam_1
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

int T;
unsigned long long N;
int seen, A[10], C;

int main(int argc, const char * argv[]) {
	int tmp = 1;
	for (int i = 0; i < 10; ++i) {
		C |= tmp;
		A[i] = tmp;
		tmp = tmp << 1;
	}
	
	ifstream readFile;
	ofstream writeFile;
	readFile.open("A-large.in");
	writeFile.open("output.txt");
	
	if (readFile.is_open()) {
		readFile >> T;
		for (int i = 1; i <= T; i++) {
			seen = 0;
			readFile >> N;
			if (N == 0) {
				printf("Case #%d: INSOMNIA\n", i);
				writeFile << "Case #" << i << ": INSOMNIA\n";
				continue;
			}

			unsigned long long num = N;
			unsigned long long inc;
			for(;;) {
				inc = num;
				while (inc > 0) {
					int r = inc % 10;
					seen |= A[r];
					inc /= 10;
				}
				if (seen == C) {
					break;
				}
				num += N;
			}
			
			printf("Case #%d: %llu\n", i, num);
			writeFile << "Case #" << i << ": " << num << "\n";
		}
	}
	
	readFile.close();
	writeFile.close();
	return 0;
}
