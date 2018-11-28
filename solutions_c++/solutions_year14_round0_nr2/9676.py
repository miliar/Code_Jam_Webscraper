#pragma once

#include <fstream>
#include <vector>
using namespace std;

class Solution
{
public:

	ifstream inputFile;
	ofstream outputFile;

	Solution(void);
	~Solution(void);

	void solve();
};

