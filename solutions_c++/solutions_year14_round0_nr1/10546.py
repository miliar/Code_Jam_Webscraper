#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <algorithm>

const int nRowCount = 4;
const char* sBad = "Bad magician!";
const char* sCheated = "Volunteer cheated!";

void solution(int test)
{
	int nFirstRow = 0, nSecondRow = 0;
	scanf("%d", &nFirstRow);
	
	std::vector<int> vCardRowFirst[nRowCount];
	
	for (int i = 0; i < nRowCount; ++i) {
		int c1, c2, c3, c4;
		scanf("%d%d%d%d", &c1, &c2, &c3, &c4);
		vCardRowFirst[i].push_back(c1);
		vCardRowFirst[i].push_back(c2);
		vCardRowFirst[i].push_back(c3);
		vCardRowFirst[i].push_back(c4);
	}

	scanf("%d", &nSecondRow);

	std::vector<int> vCardRowSecond[nRowCount];
	for (int i = 0; i < nRowCount; ++i) {
		int c1, c2, c3, c4;
		scanf("%d%d%d%d", &c1, &c2, &c3, &c4);
		vCardRowSecond[i].push_back(c1);
		vCardRowSecond[i].push_back(c2);
		vCardRowSecond[i].push_back(c3);
		vCardRowSecond[i].push_back(c4);
	}

	int nMatchCount = 0;
	int nAnswer = 0;
	for (int i = 0; i < vCardRowFirst[nFirstRow-1].size(); ++i) {
		for (int j = 0; j < vCardRowSecond[nSecondRow-1].size(); ++j) {
			if (vCardRowFirst[nFirstRow-1][i] == vCardRowSecond[nSecondRow-1][j]) {
				++nMatchCount;
				nAnswer = vCardRowFirst[nFirstRow-1][i];
			}
		}
	}

	if (nMatchCount == 0)
	{
		printf("Case #%d: %s\n", test + 1, sCheated);
	}
	else if (nMatchCount == 1)
	{
		printf("Case #%d: %d\n", test + 1, nAnswer);
	}
	else
	{
		printf("Case #%d: %s\n", test + 1, sBad);
	}
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("a.out", "w", stdout);

	char buf[256];
	gets(buf); // read first line from input
	int T = 0;
	sscanf(buf, "%d", &T);
	for (int test = 0; test < T; ++test) {
		solution(test);
	}


	return 0;
}