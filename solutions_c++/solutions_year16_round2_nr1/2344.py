#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <algorithm>

using namespace std;

void reduce(map<char, int> &mp, const string &num)
{
	for (int i = 0; i < num.length(); i++) {
		mp[num[i]]--;
	}
}

string outString(const string & inString)
{
	//cout << inString << endl;
	map <char, int> charFreq;
	string out;
	for (int i = 0; i < inString.length(); i++) {
		charFreq[inString[i]]++;
	}
	/*
	cout << charFreq.size() << endl;
	map<char, int>::iterator itr = charFreq.begin();
	while (itr != charFreq.end()) {
		cout << itr->first << "->" << itr->second << endl;
		itr++;
	}
	*/
	while (charFreq['Z'] > 0) { //zero
		reduce(charFreq, "ZERO"); out += "0";
	}
	while (charFreq['W'] > 0) { //two
		reduce(charFreq, "TWO"); out += "2";
	}
	while (charFreq['X'] > 0) { //six
		reduce(charFreq, "SIX"); out += "6";
	}
	while (charFreq['S'] > 0) { //seven
		reduce(charFreq, "SEVEN"); out += "7";
	}
	while (charFreq['U'] > 0) { //four
		reduce(charFreq, "FOUR"); out += "4";
	}
	while (charFreq['V'] > 0) { //five
		reduce(charFreq, "FIVE"); out += "5";
	}
	while (charFreq['G'] > 0) { //eight
		reduce(charFreq, "EIGHT"); out += "8";
	}
	while (charFreq['R'] > 0) { //three
		reduce(charFreq, "THREE"); out += "3";
	}
	while (charFreq['O'] > 0) { //one
		reduce(charFreq, "ONE"); out += "1";
	}
	while (charFreq['N'] > 0) { //nine
		reduce(charFreq, "NINE"); out += "9";
	}
	std::sort(out.begin(), out.end());
	return out;
}

//int mainA()
int main()
{
	int NumTests = 0;
	std::cin >> NumTests;
	for (int i = 1; i <= NumTests; i++) {
		string str; std::cin >> str;
		std::cout << "Case #" << i << ": " << outString(str) << std::endl;
	}
	return 0;
}