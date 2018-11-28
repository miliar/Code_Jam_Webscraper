#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

string s = "";

vector<char> findMax(map<char, int> mymap) {
	int maxNum = -1;
	int secondMax = -1;
	int thridMax = -1;
	char maxChar = '*';
	char secondMaxChar = '*';
	for (map<char,int>::iterator it=mymap.begin(); it!=mymap.end(); ++it) {
		if (it->second > maxNum) {
			thridMax = secondMax;
			secondMax = maxNum;
			maxNum = it->second;
			secondMaxChar = maxChar;
			maxChar = it->first;
		} else if (it->second > secondMax) {
			thridMax = secondMax;
			secondMax = it->second;
			secondMaxChar = it->first;
		} else if (it->second > thridMax) {
			thridMax = it->second;
		}
	}

	vector<char> ret;

	int diff = maxNum - secondMax;

	if (maxNum == thridMax) {
		ret.push_back(maxChar);
	} else if (diff >= 2) {
		ret.push_back(maxChar);
		ret.push_back(maxChar);
	} else if (diff == 1) {
		ret.push_back(maxChar);
	} else if (diff == 0) {
		ret.push_back(maxChar);
		ret.push_back(secondMaxChar);
	} else {
		cout << "hello" << endl;
	}

	
	return ret;
}

void removeChar(map<char, int> &mymap, char c) {
	map<char,int>::iterator itt = mymap.find(c);
	if (itt == mymap.end()) {
		return;
	} else {
		if (mymap[c] == 1) {
			mymap.erase(c);
		} else {
			mymap[c] = mymap[c]-1;
		}
		s += c;
	}
		
}

int main() {
	int T; // number of tests
	scanf("%d", &T);
	// string line;
	// getline(cin, line);
	vector<string> result;

	for (int i = 0; i < T; i++) {
		s = "";
		int N;
		scanf("%d", &N);
		map<char, int> input;
		for (int j = 0; j < N; j++) {
			int temp;
			scanf("%d", &temp);
			char tempChar = 'A'+j;
			input[tempChar] = temp;
		}
		while (!input.empty()) {
			vector<char> foundMax = findMax(input);
			if (foundMax.size() == 1) {
				removeChar(input, foundMax[0]);
				s += " ";
			} else if (foundMax.size() == 2) {
				removeChar(input, foundMax[0]);
				removeChar(input, foundMax[1]);
				s += " ";
			} else {
				cout << "hi" ;
			}
		}
		result.push_back(s);

	}

	for (int i = 0; i < T; i++) {
		cout << "Case #" << i+1 << ": " << result[i] << endl;
	}

}


