#define _CRT_SECURE_NO_DEPRECATE
#include <fstream>
#include <cstdlib>
#include <iostream>
#include <math.h>
#include <sstream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <string>
#include <map>

using namespace std;

struct Nodes{
	vector<int> adjNodes;
};
int main() {
	freopen("InputR1-B.txt","r",stdin);
	freopen("OutputR1-B.txt","w",stdout);
	string str;
	cin >> str;
	int numOfTestCases = atoi(str.c_str());	
	int caseNmuber = 0;
	while (true)
	{
		caseNmuber++;
		cin >> str;
		int numOfStrings = atoi(str.c_str());
		string baseString = "";
		vector<string> AllStrings;
		bool possible = true;
		for(int i = 0; i < numOfStrings; i++)
		{
			cin >> str;
			AllStrings.push_back(str);
		}
		// Create the base string
		string firstString = AllStrings[0];
		char curChar = ' ';
		for(int i = 0; i < firstString.size(); i++)
		{
			if(firstString[i] != curChar)
			{
				curChar = firstString[i];
				baseString.push_back(curChar);
			}
		}
		vector<vector<int>> freqOfChars;
		// Create freq of chars in strings
		//iterate through all strings
		for(int s = 0; s < AllStrings.size() && possible ;s++)
		{
			vector<int> freqOfCurString(baseString.size(),0);
			int baseIndex = 0;
			for(int curChar = 0; curChar < AllStrings[s].size(); curChar++)
			{
				if(baseString[baseIndex] == AllStrings[s][curChar])
					freqOfCurString[baseIndex]++;
				else
				{
					baseIndex++;
					if(baseIndex < baseString.size() && baseString[baseIndex] == AllStrings[s][curChar])
						freqOfCurString[baseIndex]++;
					else
					{
						possible = false;
						break;
					}
				}
			}
			freqOfChars.push_back(freqOfCurString);
		}

		vector<int> numOfActions(baseString.size(),0);
		for(int curFreq = 0; curFreq < baseString.size(); curFreq++)
		{
			int min = 1000;
			int max = -1;
			for(int curStr = 0; curStr < freqOfChars.size(); curStr++)
			{
				//min = min(1,2);
				//min(
				if(freqOfChars[curStr][curFreq] == 0)
					possible = false;
				min = std::min(freqOfChars[curStr][curFreq],min);
				max = std::max(freqOfChars[curStr][curFreq],max);
			}
			//if(min == 0)
			//	possible = false;
			numOfActions[curFreq] = max - min;
		}

		int totalActions = 0;

		for(int i = 0; i < numOfActions.size(); i++)
			totalActions += numOfActions[i];

		if(possible)
			cout << "Case #"<<caseNmuber<<": "<<totalActions << endl;
		else 
			cout << "Case #"<<caseNmuber<<": Fegla Won" << endl;
		//cout << str;
		if(caseNmuber == numOfTestCases)
			break;

	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}

