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

static int A[2000];
static int B[2000];
static bool gt[2000][2000];
char *doC(char **&toks)
{
	int N = atoi(*toks++);
	for (int i=0; i<N; i++) {
		A[i] = atoi(*toks++);
	}
	for (int i=0; i<N; i++) {
		B[i] = atoi(*toks++);
	}
	doneParsingArgs(toks);

	memset(gt, 0, sizeof(gt));
	bool saw[2000];
	for (int i=0; i<N; i++) {
		memset(saw, 0, N);
		for (int j=i-1; j>=0; j--) {
			if (A[j] < A[i] && !saw[A[j]]) {
				saw[A[j]] = true;
				gt[i][j] = true;
			}
		}
		for (int j=i+1; j<N; j++) {
			if (A[j] <= A[i]) {
				gt[i][j] = true;
			}
		}
	}
	if (0) {
		printf("-----\n");
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				printf("%c ", gt[i][j] ? 'X' : ' ');
			}
			printf("\n");
		}
	}
	for (int i=0; i<N; i++) {
		memset(saw, 0, N);
		for (int j=i+1; j<N; j++) {
			if (B[j] < B[i] && !saw[B[j]]) {
				saw[B[j]] = true;
				gt[i][j] = true;
			}
		}
		for (int j=i-1; j>=0; j--) {
			if (B[j] <= B[i]) {
				gt[i][j] = true;
			}
		}
	}
	if (0) {
		printf("-----\n");
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				printf("%c ", gt[i][j] ? 'X' : ' ');
			}
			printf("\n");
		}
	}
	int ret[2000];
	memset(saw, 0, N);
	for (int i=0; i<N; i++) {
		bool good = false;
		for (int j=0; j<N; j++) {
			if (saw[j]) continue;
			good = true;
			for (int k=0; k<N; k++) {
				if (saw[k]) continue;
				if (gt[j][k]) {
					good = false;
					break;
				}
			}
			if (good) {
				ret[i] = j;
				saw[j] = true;
				break;
			}
		}
		assert(good);
	}

	int ret2[2000];
	for (int i=0; i<N; i++) {
		ret2[ret[i]] = i;
	}
	static char buf[16384];
	static char rets[16384];
	rets[0] = 0;
	for (int i=0; i<N; i++) {
		sprintf(buf, "%d%s", ret2[i]+1, (i == N-1) ? "" : " ");
		strcat(rets, buf);
	}
	return rets;
}

