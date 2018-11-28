// Test.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

bool check(long l)
{
	char s[100];
	sprintf(s, "%ld", l);
	int n = strlen(s);
	int i = 0, j = n-1;
	for (; i < j && s[i] == s[j]; ++i, --j);
	return i >= j;
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int c = 0; c < numCases; ++c) 
	{
		long a, b;
		cin >> a >> b;

		int i = 0;
		for (long l = a; l <= b; ++l)
		{
			long r = (long) sqrt((double)l);
			if (r * r == l)
			{
				if (check(l) && check(r))
					++i;
			}
		}

		cout << "Case #" << c+1 << ": " << i << endl;
	}

	return 0;
}

