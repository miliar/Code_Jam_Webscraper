#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

//try to remove b from a
//b == "ONE" or "TWO", etc...
bool tryToRemove(string& a, string b) {
	for(int currChar = 0; currChar < b.size(); ++currChar) {
		bool foundChar = false;
		for(int i = 0; i < a.size(); ++i) {
			if(a[i] == b[currChar]) {
				a.erase(a.begin()+i);
				foundChar = true;
				break;
			}
		}
		if(!foundChar) return false;
	}
	return true;
}

void recurBuildOutput(	string alphadigits,
						int startNum,
						string tempSolution,
						string& endSolution) {
	if(alphadigits.size() == 0)
		endSolution = tempSolution;
	else if(alphadigits.size() < 3)
		return;
	string cpy;
//	cpy = alphadigits;
//	if(startNum <= 0 && tryToRemove(cpy, "ZERO"))
//		recurBuildOutput(cpy, 0, tempSolution+"0", endSolution);
	cpy = alphadigits;
	if(startNum <= 1 && tryToRemove(cpy, "ONE"))
		recurBuildOutput(cpy, 1, tempSolution+"1", endSolution);
//	cpy = alphadigits;
//	if(startNum <= 2 && tryToRemove(cpy, "TWO"))
//		recurBuildOutput(cpy, 2, tempSolution+"2", endSolution);
	cpy = alphadigits;
	if(startNum <= 3 && tryToRemove(cpy, "THREE"))
		recurBuildOutput(cpy, 3, tempSolution+"3", endSolution);
//	cpy = alphadigits;
//	if(startNum <= 4 && tryToRemove(cpy, "FOUR"))
//		recurBuildOutput(cpy, 4, tempSolution+"4", endSolution);
	cpy = alphadigits;
	if(startNum <= 5 && tryToRemove(cpy, "FIVE"))
		recurBuildOutput(cpy, 5, tempSolution+"5", endSolution);
//	cpy = alphadigits;
//	if(startNum <= 6 && tryToRemove(cpy, "SIX"))
//		recurBuildOutput(cpy, 6, tempSolution+"6", endSolution);
	cpy = alphadigits;
	if(startNum <= 7 && tryToRemove(cpy, "SEVEN"))
		recurBuildOutput(cpy, 7, tempSolution+"7", endSolution);
//	cpy = alphadigits;
//	if(startNum <= 8 && tryToRemove(cpy, "EIGHT"))
//		recurBuildOutput(cpy, 8, tempSolution+"8", endSolution);
	cpy = alphadigits;
	if(startNum <= 9 && tryToRemove(cpy, "NINE"))
		recurBuildOutput(cpy, 9, tempSolution+"9", endSolution);
}

//this is an optimization...
//since 0,2,4,6,8 all contain unique characters
//we know that if we find those characters, we can remove
//that number, then we don't have to worry about them later
string removeUniques(string& s) {
	string partialSolution = "";
	while(s.find('Z') != string::npos) {
		tryToRemove(s, "ZERO");
		partialSolution += "0";
	}
	while(s.find('W') != string::npos) {
		tryToRemove(s, "TWO");
		partialSolution += "2";
	}
	while(s.find('U') != string::npos) {
		tryToRemove(s, "FOUR");
		partialSolution += "4";
	}
	while(s.find('X') != string::npos) {
		tryToRemove(s, "SIX");
		partialSolution += "6";
	}
	while(s.find('G') != string::npos) {
		tryToRemove(s, "EIGHT");
		partialSolution += "8";
	}
	return partialSolution;
}

int main(int argc, char* argv[]) {
	if(argc != 2) {
		cout << "Usage: use this program correctly" << endl;
		return 0;
	}
	ofstream os("out.txt");
	ifstream is(argv[1]);
	int numTestCases;
	is >> numTestCases;
	is.get(); //burn newline
	for(int i = 1; i <= numTestCases; ++i) {
		os << "Case #" << i << ": ";
		char alphadigits[256];
		is.getline(alphadigits, sizeof(alphadigits));

		string testCase(alphadigits);
		string solutionPartA = removeUniques(testCase);
		string solutionPartB = "";
		recurBuildOutput(testCase, 0, "", solutionPartB);
		string solution = solutionPartA + solutionPartB;
		sort(solution.begin(), solution.end());
		os << solution << endl;
	}
		
}