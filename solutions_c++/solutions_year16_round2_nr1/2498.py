#include <iostream>
#include <unordered_map>
#include <vector>
#include <utility>
#include <fstream>
#include <algorithm>
using namespace std;

int main() {
	ifstream testCase ("./A-large.in");
	ofstream testCaseAns ("./output.txt");

	int T = 0;
	testCase >> T;
	for (int i = 0; i < T; i++) {
		string str;
    testCase >> str;
    int count[26] = {0};
    for (int j = 0; j < str.length(); j++) {
      count[str[j] - 'A']++;
    }
    vector<int> digits;
    // 0 ZERO
    for (int j = 0; j < count['Z' - 'A']; j++) {
      digits.push_back(0);
      count['E' - 'A']--;
      count['R' - 'A']--;
      count['O' - 'A']--;
    }
    count['Z' - 'A'] = 0;
    // 2 TWO
    for (int j = 0; j < count['W' - 'A']; j++) {
      digits.push_back(2);
      count['T' - 'A']--;
      count['O' - 'A']--;
    }
    count['W' - 'A'] = 0;
    // 6 SIX
    for (int j = 0; j < count['X' - 'A']; j++) {
      digits.push_back(6);
      count['S' - 'A']--;
      count['I' - 'A']--;
    }
    count['X' - 'A'] = 0;
    // 7 SEVEN
    for (int j = 0; j < count['S' - 'A']; j++) {
      digits.push_back(7);
      count['E' - 'A'] -= 2;
      count['V' - 'A']--;
      count['N' - 'A']--;
    }
    count['S' - 'A'] = 0;
    // 5 FIVE
    for (int j = 0; j < count['V' - 'A']; j++) {
      digits.push_back(5);
      count['F' - 'A']--;
      count['I' - 'A']--;
      count['E' - 'A']--;
    }
    count['V' - 'A'] = 0;
    // 4 FOUR
    for (int j = 0; j < count['F' - 'A']; j++) {
      digits.push_back(4);
      count['O' - 'A']--;
      count['U' - 'A']--;
      count['R' - 'A']--;
    }
    count['F' - 'A'] = 0;
    // 1 ONE
    for (int j = 0; j < count['O' - 'A']; j++) {
      digits.push_back(1);
      count['N' - 'A']--;
      count['E' - 'A']--;
    }
    count['O' - 'A'] = 0;
    // 3 THREE
    for (int j = 0; j < count['R' - 'A']; j++) {
      digits.push_back(3);
      count['T' - 'A']--;
      count['H' - 'A']--;
      count['E' - 'A'] -= 2;
    }
    count['R' - 'A'] = 0;
    // 8 EIGHT
    for (int j = 0; j < count['H' - 'A']; j++) {
      digits.push_back(8);
      count['E' - 'A']--;
      count['I' - 'A']--;
      count['G' - 'A']--;
      count['T' - 'A']--;
    }
    count['H' - 'A'] = 0;
    // 9 NINE
    for (int j = 0; j < count['I' - 'A']; j++) {
      digits.push_back(9);
    }
    sort(digits.begin(), digits.end());
		testCaseAns << "Case #" << i + 1 << ": ";
      for (vector<int>::iterator it=digits.begin(); it!=digits.end(); ++it)
        testCaseAns << *it;
    testCaseAns << "\n";
	}
	testCase.close();
	testCaseAns.close();
	return 0;
}
