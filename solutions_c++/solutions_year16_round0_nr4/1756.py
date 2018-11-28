/************************************************************************/
/* Microsoft Visual Studio Community 2013, Win32                        */
/************************************************************************/

#include <iostream>
#include <set>
#include <vector>
#include <queue>
#include <math.h>

using namespace std;

typedef unsigned long long SIZE;

int main(int argc, char* argv[])
{
	SIZE cases;
	cin >> cases;
	for (SIZE i = 1; i <= cases; ++i)
	{
		printf("Case #%llu:",i);
		SIZE k, c, s;
		cin >> k >> c >> s;
		if (s < k)
			printf(" IMPOSSIBLE");
		else
			for (SIZE j = 1; j <= k; ++j)
				printf(" %llu", j);

		printf("\n");
	}
	return 0;
}
