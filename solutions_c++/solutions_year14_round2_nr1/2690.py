#include <iostream>
#include <vector>
#include <algorithm>
#include <assert.h>
#include <map>
using namespace std;


int findOptimalNumber( vector<int>& numbers )
{
	assert(numbers.size() > 0);
	std::sort(numbers.begin(), numbers.end());
	// incompatible strings
	if (numbers[0] == 0) {
		return -1;
	}
	int currIndex = 0;
	int currNumOfOperations = 0;

	// operations for one letter
	for (int j = 0; j < numbers.size(); j++) {
		currNumOfOperations += abs(numbers[j]-1);
	}
	int minimum = currNumOfOperations;
	for (int x = 2; x <= numbers[numbers.size() - 1]; x++) {
		while (currIndex < numbers.size() && numbers[currIndex] < x) {
			currIndex++;
		}
		currNumOfOperations += currIndex;
		currNumOfOperations -= numbers.size() - currIndex;
		if (currNumOfOperations < minimum) {
			minimum = currNumOfOperations;
		}
	}
	return minimum;
}


int findNumberOfOperations()
{
	const int maxStrLength = 100;
	char buf[maxStrLength + 1];
	vector<char> letters;
	vector<vector<int>> lettersCount;

	int nLines = 0;
	cin >> nLines;
	for (int line = 0; line < nLines; line++) {
		cin >> buf;
		lettersCount.push_back(vector<int>());
		vector<int>& lineLettersCount = lettersCount.at(lettersCount.size() - 1);
		if (line == 0){ // fill the letters
			for (char* c = buf; *c != 0; c++) {
				if ( !letters.empty() && letters.back() == *c) { // adding count of existing letter
					lineLettersCount.back() += 1;
				} else { // adding new letter
					letters.push_back(*c);
					lineLettersCount.push_back(1);
				}
			}
		} else { 
			int i = 0;
			for (int j = 0; j < letters.size(); j++) {
				lineLettersCount.push_back(0);
			}
			for (char* c = buf; *c != 0; c++) {
				if (i >= letters.size()) {
					return -1;
				}
				if (letters[i] == *c) {
					lineLettersCount[i]++;
				}
				else if (i + 1 < letters.size() && letters[i + 1] == *c) {
					i++;
					lineLettersCount[i]++;
				}
				else {
					return -1;
				}
			}
		}
	}
	int result = 0;
	for (int letter = 0; letter < letters.size(); letter++) {
		vector<int> counts; // for current letter
		for (int line = 0; line < lettersCount.size(); line++) {
			counts.push_back(lettersCount[line][letter]);
		}
		int curr = findOptimalNumber(counts);
		if (curr == -1) {
			return -1;
		}
		else { 
			result += curr; 
		}
	}
	return result;
}

int main()
{
	
	int nCases = 0;
	cin >> nCases;
	for (int n = 0; n < nCases; n++) {
		
		int numberOfOperations = findNumberOfOperations();

		// output result
		cout << "Case #" << n + 1 << ": ";
		if (numberOfOperations < 0) {
			cout << "Fegla Won" << endl;
		}
		else {
			cout << numberOfOperations << endl;
		}
	}
}

