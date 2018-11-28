#include <stdio.h>
#include <stdlib.h>
#include <share.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;
using namespace std::tr1;

const unsigned int MAX_LINE = 1050000;

int la = 0;
int lb = 1;
int lc = 2;
int ld = 3;
int le = 4;
int lf = 5;
int lg = 6;
int lh = 7;
int li = 8;
int lj = 9;
int lk = 10;
int ll = 11;
int lm = 12;
int ln = 13;
int lo = 14;
int lp = 15;
int lq = 16;
int lr = 17;
int ls = 18;
int lt = 19;
int lu = 20;
int lv = 21;
int lw = 22;
int lx = 23;
int ly = 24;
int lz = 25;

vector<vector<int> > calclc;

vector<int> numbers;
vector<int> gleft(26);
int countLeft;

bool Solve(int tryThis)
{
	if (countLeft == 0)
		return true;
	if (tryThis >= 10)
		return false;
	
	vector<int> calc = calclc[tryThis];
	int numTries = calc.size();
	if (countLeft < numTries)
		return Solve(tryThis + 1);

	for (int i = 0; i < numTries; i++)
	{
		int ind = calc[i];
		if (gleft[ind])
			gleft[ind]--;
		else
		{
			for (int j = i - 1; j >= 0; j--)
				gleft[calc[j]]++;

			return Solve(tryThis + 1);
		}
	}
	countLeft -= numTries;
	numbers.push_back(tryThis);

	bool solveNext = false;
	for (int i = 0; i < 10; i++)
	{
		if (Solve(i))
		{
			solveNext = true;
			break;
		}
	}
	if (!solveNext)
	{
		for (int i = 0; i < numTries; i++)
			gleft[calc[i]]++;
		countLeft += numTries;
		numbers.pop_back();
	}
	return solveNext;
}

#define REG(ind, letter) calclc[ind].push_back(l##letter);

void main(int argc, char *argv[])
{
	char* fileName = "input\\A-small-attempt1.in";
	char* fileOutName = "output\\A-small-attempt1.out";
	//char* fileName = "input\\B-large.in";
	//char* fileOutName = "output\\B-large.out";
	FILE* filePtr = _fsopen(fileName, "r", _SH_DENYNO);
	FILE* fileOutPtr = _fsopen(fileOutName, "w", _SH_DENYNO);
	if (!filePtr || !fileOutPtr)
	{
		printf("File not found\n");
		return;
	}

	calclc.resize(10);
	REG(0, z) REG(0, e) REG(0, r) REG(0, o)
	REG(1, o) REG(1, n) REG(1, e)
	REG(2, t) REG(2, w) REG(2, o)
	REG(3, t) REG(3, h) REG(3, r) REG(3, e) REG(3, e)
	REG(4, f) REG(4, o) REG(4, u) REG(4, r)
	REG(5, f) REG(5, i) REG(5, v) REG(5, e)
	REG(6, s) REG(6, i) REG(6, x)
	REG(7, s) REG(7, e) REG(7, v) REG(7, e) REG(7, n)
	REG(8, e) REG(8, i) REG(8, g) REG(8, h) REG(8, t)
	REG(9, n) REG(9, i) REG(9, n) REG(9, e)

	char* currStr = (char*)malloc(MAX_LINE);
	fgets(currStr, MAX_LINE, filePtr);
	int numCases = atoi(currStr);
	for (int tt = 0; tt < numCases; tt++)
	{
		fgets(currStr, MAX_LINE, filePtr);
		currStr[strcspn(currStr, "\r\n")] = 0;

		int found[26] = {0};
		int totalLetters = strlen(currStr);
		for (int i = 0; i < totalLetters; i++)
			found[currStr[i] - 'A']++;

		for (int i = 0; i < 26; i++)
			gleft[i] = found[i];
		numbers.clear();
		countLeft = totalLetters;
		for (int i = 0; i < 10; i++)
			Solve(i);

		std::sort(numbers.begin(), numbers.end());
		fprintf(fileOutPtr, "Case #%d: ", tt + 1);
		for (int i = 0; i < numbers.size(); i++)
			fprintf(fileOutPtr, "%d", numbers[i]);
		fprintf(fileOutPtr, "\n");
	}
	fflush(fileOutPtr);
	fclose(fileOutPtr);
	fclose(filePtr);
}