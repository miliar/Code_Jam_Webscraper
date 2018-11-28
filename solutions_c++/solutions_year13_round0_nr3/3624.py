// CodeJam 2013
// Autor: Benjamín de la Fuente Ranea

#include <stdarg.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>

#define FILE_INPUT	"C-small-attempt0"

using namespace std;

char numStr[10000];
bool isPalindromo(int i)
{
	_itoa(i, numStr, 10);
	int length = strlen(numStr);
	for (int i = 0; i < length/2; ++i)
	{
		if (numStr[i] != numStr[length-i-1])
			return false;
	}

	return true;
}

void main()
{
	freopen(FILE_INPUT".in", "r", stdin);
	freopen(FILE_INPUT".out", "w", stdout);

	int numCases;
	scanf("%d\n", &numCases);

	for (int i = 1; i <= numCases; ++i)
	{
		int low, high;
		scanf("%d %d\n", &low, &high);

		int lowSR = sqrt(low);
		if (lowSR * lowSR < low)
			++lowSR;

		int highSR = sqrt(high);
		int count = 0;
		for (int n = lowSR; n <= highSR; ++n)
		{
			if (isPalindromo(n) && isPalindromo(n*n))
				++count;
		}

		printf("Case #%d: %d\n", i, count);
	}
}
