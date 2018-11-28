//
//  main.cpp
//  Google_Jam_Qualification_B
//
//  Created by Shangqi Wu on 16/4/8.
//  Copyright © 2016 Shangqi Wu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <unordered_set>
#include <algorithm>

using namespace std;

struct strInfo {
	
	string cake;
	int step;
	int unhappyfaces;
	
	strInfo(string c, int s, int h) :
		cake(c), step(s), unhappyfaces(h) {}
	
};

int numAction(string& s) {
	
	int numUnhappyfaces = 0;
	
	for (const char& c : s) {
		
		if (c == '-') {
			numUnhappyfaces++;
		}
		
	}
	
	if (numUnhappyfaces == 0) {
		return 0;
	}
	
	queue<strInfo> q;
	q.push(strInfo(s, 0, numUnhappyfaces));
	unordered_set<string> visited;
	
	while (!q.empty()) {
		
		string cake = q.front().cake;
		int step = q.front().step;
		int numUnhappyfaces = q.front().unhappyfaces;
		q.pop();
		
		for (int i = 0; i < (int)cake.size(); i++) {
			
			string newCake = cake;
			int newUnhappyfaces = numUnhappyfaces;
			reverse(newCake.begin(), newCake.begin() + i + 1);
				
			for (int j = 0; j <= i; j++) {
					
				if (newCake[j] == '-') {
					newCake[j] = '+';
					newUnhappyfaces--;
				} else {
					newCake[j] = '-';
					newUnhappyfaces++;
				}
					
			}
			
			if (newUnhappyfaces == 0) {
				return step + 1;
			}
			
			if (visited.count(newCake) == 0) {
				q.push(strInfo(newCake, step + 1, newUnhappyfaces));
				visited.insert(newCake);
			}
			
		}
		
	}
	
	return 0;
	
}

int main(int argc, const char * argv[]) {
	
	ifstream input("./B-small-attempt0.in");
	ofstream output("./output.txt");
	
	if (!input.is_open() || !output.is_open()) {
		return 1;
	}
	
	int numCases = 0;
	string cakes;
	input >> numCases;
	
	for (int i = 1; i <= numCases; i++) {
		
		input >> cakes;
		int result = numAction(cakes);
		
		output << "Case #" << i << ": " << result << endl;
		
	}
	
	input.close();
	output.close();
	
    return 0;
}
