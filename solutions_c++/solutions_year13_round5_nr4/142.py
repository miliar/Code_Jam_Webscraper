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

int N;
int final;
bool isset(int b, int idx) {
	return !!(b & (1 << idx));
}
double cache[2097152];
bool bcache[2097152];
double doit(int b) {
	if (bcache[b]) {
		return cache[b];
	}
	if (b == final) {
		return 0;
	}
	double r = 0;
	for (int i=0; i<N; i++) {
		int w = 0;
		for (; isset(b, (i + w) % N); w++);
		int idx = (i + w) % N;
		r += (N - w) + doit(b | (1 << idx));
	}
	r = r / N;
	bcache[b] = true;
	cache[b] = r;
	return r;
}

char *doD(char **&toks)
{
	char *s = *toks++;
	N = strlen(s);
	int b = 0;
	final = (1 << N) - 1;
	for (int i=0; i<N; i++) {
		if (s[i] == 'X') {
			b |= (1 << i);
		}
	}
	doneParsingArgs(toks);

	memset(bcache, 0, 1 << N);
	double v = doit(b);

	static char buf[16384];
	sprintf(buf, "%0.10f", v);
	return buf;
}

