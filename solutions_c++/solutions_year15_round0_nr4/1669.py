#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define USEFILE

int main(void)
{
#ifdef USEFILE
	FILE* inf = freopen("D.in", "r", stdin);
	FILE* outf = freopen("D_out.txt.", "w", stdout);
#endif

	int tc;
	cin >> tc;

	for(int testNum = 1; testNum <= tc; testNum++)
	{
		int x, r, c;
		cin >> x >> r >> c;

		if((x == 1) || (x == 2 && ((r*c) % 2 == 0)))
		{
			printf("Case #%d: GABRIEL\n", testNum);
			continue;
		}

		if((r*c) % x != 0)
		{
			printf("Case #%d: RICHARD\n", testNum);
			continue;
		}

		if(x == 3)
		{
			if(r * c == 3)
				printf("Case #%d: RICHARD\n", testNum);
			else
				printf("Case #%d: GABRIEL\n", testNum);

			continue;
		}

		// x == 4
		int p = r * c;
		if(p <= 8)
			printf("Case #%d: RICHARD\n", testNum);
		else
			printf("Case #%d: GABRIEL\n", testNum);

	}


#ifdef USEFILE
	fclose(inf);
	fclose(outf);
#endif

	return 0;
}