/******************************************************************************
 * Directives
 *****************************************************************************/
#ifdef WIN32
#define _CRT_SECURE_NO_WARNINGS
#endif

/******************************************************************************
 * Header Files
 *****************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/******************************************************************************
 * Constants, Macros, Typedefs, Enums & Structures
 *****************************************************************************/

/******************************************************************************
 * Global & Static Variables
 *****************************************************************************/
int N, M;
int O[100];
int E[100];
int P[100];
long long CNT[100];

long long max_loss = 0;

/******************************************************************************
 * Global & Static Function Prototypes
 *****************************************************************************/

/******************************************************************************
 * Function Implementations
 *****************************************************************************/
long long getOrg()
{
	long long sum = 0;
	for (int i = 0 ; i < M; i++) {
		long long len = E[i] - O[i];
		sum += len * len * P[i];
	}
	return sum;
}

void cntPeople()
{
	for (int i = 1; i < N; i++) {
		CNT[i] = 0;
	}
	for (int i = 0; i < M; i++) {
		int ob = O[i];
		int ex = E[i];
		int people = P[i];
		for (int j = ob; j < ex; j++) {
			CNT[j] += people;
		}
	}
}

long long getMax(long long level, int start, int end)
{
	if (start == end) {
		return 0;
	}
	long long min = CNT[start];
	for (int i = start + 1; i < end; i++) {
		long long cnt = CNT[i];
		if (cnt < min) {
			min = cnt;
		}
	}
	long long dist = (end - start);
	long long val = dist * dist * (min - level);
	level = min;

	int nstart = -1;
	for (int i = start; i < end; i++) {
		long long cnt = CNT[i];
		if (nstart < 0) {
			if (cnt > level) {
				nstart = i;
			}
		} else {
			// nstart > 0
			if (cnt == level) {
				val += getMax(level, nstart, i);
				nstart = -1;
			}
		}
		if (nstart > 0 && i == end - 1) {
			val += getMax(level, nstart, end);
		}
	}

	return val;
}

void runCase()
{
	scanf("%d %d", &N, &M);
	for (int i = 0; i < M; i++) {
		scanf("%d %d %d", &O[i], &E[i], &P[i]);
	}

	long long org = getOrg();
	cntPeople();

	long long max = getMax(0, 1, N);

	printf("%lld\n", (max - org) / 2);
}

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		runCase();
	}
	return 0;
}
