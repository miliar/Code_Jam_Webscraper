// sheep.cpp : Defines the entry point for the console application.
//

/************************************************************************/
/* Microsoft Visual Studio Community 2013, Win32                        */
/************************************************************************/

#include <iostream>
#include <set>
#include <math.h>

using namespace std;

typedef unsigned long long SIZE;

int main(int argc, char* argv[])
{
	SIZE cases;
	cin >> cases;
	for (SIZE i = 1; i <= cases; ++i)
	{
		SIZE n, k;
		cin >> n;

		if (n == 0)
		{
			printf("Case #%llu: INSOMNIA\n",i);
			continue;
		}
		string characters(2000000, '\0');
		set<char> digits;
		set<char> needed_digits{ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
		for (k = 1; digits != needed_digits; ++k)
		{
			sprintf_s(&characters[0], characters.size(), "%llu", k*n);
			digits.insert(characters.begin(), characters.begin()+strlen(&characters[0]));
		}
		printf("Case #%llu: %llu\n",i, n*(k-1));
	}

	return 0;
}

