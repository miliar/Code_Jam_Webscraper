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
long long table[51];

/******************************************************************************
 * Global & Static Function Prototypes
 *****************************************************************************/

/******************************************************************************
 * Function Implementations
 *****************************************************************************/
long long getSure(int n, long long p)
{
	long long expn = table[n];
	p = expn - p;
	if (p == 0) {
		return expn - 1;
	}

	for (int i = 1; i <= n; i++) {
		long long tmpn = table[i];
		if (p < tmpn) {
			return table[n - i + 1] - 2;
		}
	}

	return 0;
}

long long getCould(int n, long long p)
{
	long long expn = table[n];
	if (p == expn) {
		return expn - 1;
	}
	return expn - getSure(n, expn - p) - 2;
}

void runCase()
{
	int N;
	long long P;
	scanf("%d %lld", &N, &P);

	printf("%lld %lld\n", getSure(N, P), getCould(N, P));

}

int main(int argc, char *argv[])
{
	table[0] = 1;
	for (int i = 0; i < 50; i++) {
		table[i + 1] = table[i] * 2;
	}
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		runCase();
	}
	return 0;
}
