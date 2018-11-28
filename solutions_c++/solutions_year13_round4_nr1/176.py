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

static int s[1000];
static int e[1000];
static U64 p[1000];
static int evt[2000];
static S64 evp[2000];

static U64 mod = 1000002013;
static U64 N;

U64 cost(U64 len) {
	return (len * N - (len)*(len-1)/2) % mod;
}

int cmpIndir(const void *a, const void *b) {
	int ia = *(const int*)a;
	int ib = *(const int*)b;
	int d = evt[ia] - evt[ib];
	if (d == 0) {
		if (evp[ia] > 0) {
			return -1;
		} else {
			return 1;
		}
	}
	return d;
}

char *doA(char **&toks)
{
	N = atoi(*toks++);
	int M = atoi(*toks++);
	for (int i=0; i<M; i++) {
		s[i] = atoi(*toks++);
		e[i] = atoi(*toks++);
		p[i] = atoi(*toks++);
		evt[i*2] = s[i];
		evp[i*2] = p[i];
		evt[i*2+1] = e[i];
		evp[i*2+1] = -p[i];
	}
	doneParsingArgs(toks);
	U64 orig_cost=0;
	for (int i=0; i<M; i++) {
		orig_cost += (cost(e[i] - s[i]) * p[i]) % mod;
		orig_cost %= mod;
	}

	int indir[2000];
	for (int i=0; i<M*2; i++) {
		indir[i] = i;
	}
	qsort(indir, M*2, sizeof(int), cmpIndir);

	U64 res = 0;
	int idx=0;
	U64 starts[2000];
	U64 counts[2000];
	for (int k=0; k<M*2; k++) {
		int i = indir[k];
		if (evp[i] > 0) {
			starts[idx] = evt[i];
			counts[idx] = evp[i];
			idx++;
		} else {
			U64 ppl = -evp[i];
			while (ppl) {
				if (counts[idx-1] > ppl) {
					counts[idx-1] -= ppl;
					U64 len = evt[i] - starts[idx-1];
					res += (cost(len) * ppl) % mod;
					res %= mod;
					ppl = 0;
				} else {
					ppl -= counts[idx-1];
					U64 len = evt[i] - starts[idx-1];
					res += (cost(len) * counts[idx-1]) % mod;
					res %= mod;
					counts[idx-1] = 0;
					idx--;
				}
			}
		}
	}

	S64 rr = orig_cost;
	rr -= res;
	if (rr < 0) {
		rr += mod;
	}
	static char buf[16384];
	sprintf(buf, "%d", (U32)rr);
	return buf;
}

