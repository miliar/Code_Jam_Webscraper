// ConsoleApplication30.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <list>
#include <queue>
using namespace std;
int senatorCount[26];
vector<string> result;
bool IsSolved() {
	for (int i = 0; i < 26; ++i)
		if (senatorCount[i] != 0)
			return false;

	return true;
}

int maxIndex() {
	int max = 0;
	int ret = -1;
	for (int i = 0; i < 26; ++i) {
		if (max <= senatorCount[i])
		{
			max = senatorCount[i];
			ret = i;
		}
	}
	return ret;
}

bool IsOk() {
	int max = 0;
	int ret = -1;
	int sum = 0;
	for (int i = 0; i < 26; ++i) {
		if (max <= senatorCount[i]) {
			ret = i;
			max = senatorCount[i];
		}
		sum += senatorCount[i];
	}
	if (sum < (max * 2))
		return false;
	else
		return true;
}

void solve() {

	int index = maxIndex();
	if(senatorCount[index] == 0)
		return;
	senatorCount[index]--;
	string r = "";
	char temp ='A' + index;
	r = temp;
	
	
	
	index = maxIndex();
	if (senatorCount[index] == 0)
		return;
	senatorCount[index]--;
	if (IsOk()) {
		r += 'A' + index;
	}else{
		senatorCount[index]++;
	}

	result.push_back(r);
}

int main()
{
	ifstream fin("input.in");
	ofstream fout("output.out");

	//-- check if the files were opened successfully 
	if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
	if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
	int numCase;
	fin >> numCase;

	for (int i = 0; i < numCase; i++)
	{
		int n;
		fin >> n;
		vector<int> input;
		vector<int> senator;
		result.clear();
		for (int i = 0; i < n; ++i) {
			int temp;
			fin >> temp;
			input.push_back(temp);
		}
		for (int i = 0; i < 26; ++i) {
			senatorCount[i] = 0;
		}

		for (int i = 0; i < input.size(); ++i) {
			senatorCount[i] = input[i];
			for(int j=0; j < input.size(); ++j)
				senator.push_back(i);
		}
		
		while (!IsSolved()) {
			solve();
		}
		
		fout << "Case #" << (i + 1) << ": ";
		for (int i = 0; i < result.size(); ++i) {
			fout << result[i].c_str();
			fout << " ";
		}
		fout << endl;
	}
	fin.close();
	fout.close();
    return 0;
}

