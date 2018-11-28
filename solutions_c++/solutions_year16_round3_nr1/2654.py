#include "stdafx.h"

#include <direct.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <stdint.h>
#include <assert.h>
#include <unordered_set>
#include <deque>
#include <boost/graph/graph_traits.hpp>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/topological_sort.hpp>
#include <boost/graph/max_cardinality_matching.hpp>

using namespace std;

//string prepath = "..\\2016-C\\";
string prepath = "";
//string testin = "test";
//string testin = "A-small-attempt0";
string testin = "A-large";

string readString(FILE *f, int limit);
int work();
int test();
int doexit() {
	printf("exiting\n");
	fflush(NULL);
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

char takeLargetsParty(multimap<int, char> &senatorsInRoom) {
	auto iter = senatorsInRoom.end();
	--iter;
	pair<int, char> selectedParty = *iter;
	senatorsInRoom.erase(iter);

	selectedParty.first--;
	if (selectedParty.first > 0) {
		senatorsInRoom.insert(selectedParty);
	}
	return selectedParty.second;
}

int solve(FILE *fin, FILE *fout) {
	int parties;

	fscanf(fin, "%d\n", &parties);
	printf(">%d< \n", parties);

	vector<int> partySizes(parties);
	multimap<int, char> senatorsInRoom;
	char currentParty = 'A';
	int total = 0;
	for (int i = 0; i < partySizes.size(); ++i) {
		fscanf(fin, "%d\n", &partySizes[i]);
		total += partySizes[i];
		senatorsInRoom.insert(std::make_pair(partySizes[i], currentParty));
		currentParty++;
	}

	for (int i = 0; i < partySizes.size(); ++i) {
		printf(" %d", partySizes[i]);
	}
	printf(" \n");
	
	string plan = "";

	while (total > 0) {
		plan += " ";

		total--;
		char s = takeLargetsParty(senatorsInRoom);
		plan += s;
		
		if (total % 2 == 0) continue;

		total--;
		s = takeLargetsParty(senatorsInRoom);
		plan += s;
	}

	fprintf(fout, "%s\n", plan.c_str());
	printf("%s\n", plan.c_str());

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


string readString(FILE *f, int limit) {
	string buf;
	buf.resize(limit);

	fscanf(f, "%s", (char *)buf.data());

	size_t pos = buf.find('\0');
	buf.resize(pos);
	return buf;
}

