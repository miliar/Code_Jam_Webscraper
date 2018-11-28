//============================================================================
// Name        : gcj-1a.cpp
// Author      : QvZcJsj7oJWtu2A
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
using namespace std;

int main() {
	int caseNum;
	cin >> caseNum;
	caseNum = 0;
	string word;
	while(cin >> word){
		string endWord;
		for(const char& c : word){
			if(endWord.empty() || c < endWord[0])
				endWord.insert(endWord.end(), c);
			else
				endWord.insert(endWord.begin(), c);
		}
		cout << "Case #" << ++caseNum << ": " << endWord << "\n";
	}
	return 0;
}
