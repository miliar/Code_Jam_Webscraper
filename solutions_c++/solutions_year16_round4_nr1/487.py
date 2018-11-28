// Using libUtil from libGlov (Game Library of Victory) available at http://bigscreensmallgames.com/libGlov
// Some solutions may use BigInteger from http://mattmccutchen.net/bigint/
#include "bigint/BigIntegerAlgorithms.hh"
#include "bigint/BigIntegerUtils.hh"
#include "utilUtils.h"
#include "utilFile.h"
#include "utilString.h"
#include "assert.h"
#include "utilArray.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "utilRand.h"
#include "utilHashTable2.h"
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;
#pragma warning(disable:4018)
extern void doneParsingArgs(char **&toks);

static int N;
static vector<int> perm;
int winner2(int v0, int v1) {
	if (v0 > v1) {
		int t = v0;
		v0 = v1;
		v1 = t;
	}
	if (v0 == v1) {
		return -1;
	} else if (v0 == 0 && v1 == 2) {
		return 2;
	} else if (v0 == 0 && v1 == 1) {
		return 0;
	} else {
		return 1;
	}
}
int winner(int level, int offset) {
	if (level == N - 1) {
		return winner2(perm[offset], perm[offset + 1]);
	}
	int v0 = winner(level + 1, offset * 2);
	if (v0 == -1) {
		return -1;
	}
	int v1 = winner(level + 1, offset * 2 + 2);
	if (v1 == -1) {
		return -1;
	}
	return winner2(v0, v1);
}

char *doA(char **&toks)
{
	N = atoi(*toks++);
	int R = atoi(*toks++);
	int P = atoi(*toks++);
	int S = atoi(*toks++);
	doneParsingArgs(toks);
	
	perm.clear();
	for (int i = 0; i < P; i++)
	{
		perm.push_back(0);
	}
	for (int i = 0; i < R; i++)
	{
		perm.push_back(1);
	}
	for (int i = 0; i < S; i++)
	{
		perm.push_back(2);
	}
	do
	{
		bool b = false;
		for (int ii = 0; ii < perm.size(); ii+=2)
		{
			if (perm[ii] == perm[ii + 1]) {
				b = true;
				break;
			}
		}
		if (b) {
			continue;
		}
		if (winner(0, 0) != -1) {
			static char ret[5000];
			for (unsigned int ii = 0; ii < perm.size(); ii++)
			{
				ret[ii] = "PRS"[perm[ii]];
			}
			ret[perm.size()] = '\0';
			return ret;
		}
	} while (next_permutation(perm.begin(), perm.end()));
	return "IMPOSSIBLE";
}