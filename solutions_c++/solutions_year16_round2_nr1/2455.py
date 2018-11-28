#include "stdafx.h"

#include <direct.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <stdint.h>
#include <assert.h>
#include <unordered_map>
#include <map>

using namespace std;

//string prepath = "..\\2016-C\\";
string prepath = "";
//string testin = "test";
//string testin = "A-small-attempt1";
string testin = "A-large";


int work();
int test();
int doexit() {
	printf("exiting\n");
	char c;
	scanf("%c", &c);
	exit(0);
}

int main()
{
	test();
	work();
	return 0;
}

struct Digit {
	char digit;
	string word;
	char uniqueChar;

	Digit(char digit_, const char* word_, char uniqueChar_) {
		digit = digit_;
		word = word_;
		uniqueChar = uniqueChar_;
	}

};

int test() {
	printf("tests done\n");
	return 0;
}

int solve(FILE *fin, FILE *fout) {
	char buf[2005] = {};

	fgets(buf, 2005, fin);
	printf(">%s< \n", buf);

	unordered_map<char, int> chars;
	int i = 0;
	for (; i < 2005; ++i) {
		const char &c = buf[i];
		if (c == 0 || c == '\n') break;

		if (!chars.count(c)) {
			chars[c] = 1;
		}
		else {
			chars[c]++;
		}
	}
	printf("%d\n", i);

	vector<Digit> uniqueChars;
	uniqueChars.push_back(Digit('0', "ZERO", 'Z'));
	uniqueChars.push_back(Digit('6', "SIX", 'X'));
	uniqueChars.push_back(Digit('2', "TWO", 'W'));
	uniqueChars.push_back(Digit('8', "EIGHT", 'G'));
	uniqueChars.push_back(Digit('3', "THREE", 'T'));
	uniqueChars.push_back(Digit('4', "FOUR", 'R'));
	uniqueChars.push_back(Digit('1', "ONE", 'O'));
	uniqueChars.push_back(Digit('5', "FIVE", 'F'));
	uniqueChars.push_back(Digit('7', "SEVEN", 'S'));
	uniqueChars.push_back(Digit('9', "NINE", 'E'));

	map<char, int> digits;
	for each (const Digit &digit in uniqueChars)
	{
		int count = chars.count(digit.uniqueChar);
		if (count <= 0) continue;
		count = chars[digit.uniqueChar];

		for each (const char &c in digit.word)
		{
			chars[c] -= count;
		}
		digits[digit.digit] = count;
	}

	string output = " ";
	for each (auto iter in digits) {
		const char &c = iter.first;
		size_t count = iter.second;

		output.append(count, c);
	}
	output += "\n";
	fprintf(fout, "%s", output.c_str());

	return 0;
}

int work() {
	string path = prepath + testin + ".in";
	FILE *fin = fopen(path.c_str(), "r");
	if (fin == NULL) {
		printf("can not open in %s\n", path.c_str());
		char *cwd = _getcwd(NULL, 0);
		printf("cwd %s\n", cwd);
		doexit();
	}

	path = prepath + testin + "_out.in";
	FILE *fout = fopen(path.c_str(), "w");
	if (fout == NULL) {
		printf("can not open out %s\n", path.c_str());
		doexit();
	}
	fflush(fout);

	int problemc;
	int ret = fscanf(fin, "%d\n", &problemc);
	if (ret != 1) {
		printf("problemc\n");
		doexit();
	}
	printf("problemc %d\n", problemc);

	for (int n = 0; n < problemc; ++n) {
		fprintf(fout, "Case #%d:", n + 1);
		printf("Case #%d:", n + 1);

		solve(fin, fout);
	}

	fclose(fout);

	doexit();
	return 0;
}

