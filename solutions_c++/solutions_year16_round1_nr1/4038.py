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
#include <deque>

using namespace std;

//string prepath = "..\\2016-C\\";
string prepath = "";
//string testin = "test";
//string testin = "A-small-attempt0";
//string testin = "C-small-attempt1";
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

int test() {

	printf("tests done\n");
	return 0;
}

int solve(FILE *fin, FILE *fout) {
	char buf[1024];
	fscanf(fin, "%s\n", buf);
	printf(">%s< \n", buf);
	string input = buf;
	printf(">%s< \n", input.c_str());
		
	deque<char> queue;

	queue.push_back(input[0]);

	for (unsigned i = 1; i < input.size(); ++i) {
		const char &c = input[i];
		if (c < queue.front()) {
			queue.push_back(c);
		} else {
			queue.push_front(c);
		}
	}

	string output = "";

	while (queue.size()) {
		output += queue.front();
		queue.pop_front();
	}

	fprintf(fout, " %s\n", output.c_str());
	printf(" %s\n", output.c_str());

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

