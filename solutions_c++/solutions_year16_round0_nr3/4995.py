//
//  main.cpp
//  Google_Jam_Qualification_C
//
//  Created by Shangqi Wu on 16/4/9.
//  Copyright © 2016 Shangqi Wu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

long long findDivisor(long long num,
						 unordered_map<long long, long long>& divisors) {
	
	if (num < 4) {
		return 0;
	}
	
	if (divisors.count(num) > 0) {
		return divisors[num];
	}
	
	if (num % 2 == 0) {
		divisors[num] = 2;
		return 2;
	}
	
	long long bound = floor(sqrt(num));
	for (long long i = 3; i <= bound; i += 2) {
		
		if (num % i == 0) {
			divisors[num] = i;
			return i;
		}
		
	}
	
	divisors[num] = 0;
	return 0;
	
}

long long baseConvert(string& s, unsigned int base) {
	
	if (base < 2) {
		return 0;
	}
	
	long long result = 0;
	long long weight = 1;
	for (int i = (int)s.size() - 1; i >= 0; i--) {
		
		result += (long long)(s[i] - '0') * weight;
		weight *= (long long)base;
		
	}
	
	return result;
	
}

vector<string> findJamCoin(string &s,
						   unordered_map<long long, long long>& divisors) {
	
	vector<string> result;
	result.push_back(s);
	
	for (unsigned int base = 2; base <= 10; base++) {
		
		long long num = baseConvert(s, base);
		long long divisor = findDivisor(num, divisors);
		
		if (divisor == 0) {
			return {};
		} else {
			result.push_back(to_string(divisor));
		}
		
	}
	
	return result;
	
}

vector<vector<string>> findJamCoins(int n, int j,
								   unordered_map<long long, long long>& divisors) {
	
	unordered_set<string> visited;
	vector<vector<string>> result;
	string ori = "1";
	for (int i = 0; i < n - 2; i++) {
		ori += "0";
	}
	ori += "1";
	
	vector<string> partialResult = findJamCoin(ori, divisors);
	if (!partialResult.empty()) {
		result.push_back(partialResult);
		if (result.size() == j) {
			return result;
		}
		partialResult.clear();
	}
	
	queue<string> q;
	q.push(ori);
	visited.insert(ori);
	
	while (!q.empty()) {
		
		string cur = q.front();
		q.pop();
		
		for (int i = 0; i < cur.size(); i++) {
			
			if (cur[i] == '0') {
				cur[i] = '1';
				
				if (visited.count(cur) == 0) {
					partialResult = findJamCoin(cur, divisors);
					
					if (!partialResult.empty()) {
						result.push_back(partialResult);
						if (result.size() == j) {
							return result;
						}
						partialResult.clear();
					}
					
					visited.insert(cur);
					q.push(cur);
				}
				
				cur[i] = '0';
			}
			
		}
		
	}
	
	return result;
	
}

int main(int argc, const char * argv[]) {
	
	ifstream input("./C-small-attempt0.in");
	ofstream output("./output.txt");
	
	if (!input.is_open() || !output.is_open()) {
		return 1;
	}
	
	int numTestCase = 0;
	int n = 0;
	int j = 0;
	input >> numTestCase;
	
	unordered_map<long long, long long> divisors;
	
	for (int i = 1; i <= numTestCase; i++) {
		
		input >> n >> j;
		vector<vector<string>> result = findJamCoins(n, j, divisors);
		
		output << "Case #" << i << ":" << endl;
		for (int j = 0; j < result.size(); j++) {
			for (int k = 0; k < result[j].size(); k++) {
				output << result[j][k] << " ";
			}
			output << endl;
		}
		
	}
	
	input.close();
	output.close();
	
    return 0;
}
