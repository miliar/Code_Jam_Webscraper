
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{
	int cases;
	int current_case = 0;
	cin >> cases;
	while (cases)
	{
		current_case++;
		cases--;
		int x, r, c;
		cin >> x >> r >> c;

		bool gabriel = true;

		if (x > 7)
		{
			gabriel = false;
		}
		else if (x > r && x > c)
		{
			gabriel = false;
		}
		else if (r*c %x != 0)
		{
			gabriel = false;
		}
		else if ((x + 1) / 2 > min(r, c))
		{
			gabriel = false;
		}
		else if (x == 1 || x == 2 || x == 3)
		{
			gabriel = true;
		}
		else if (x == 4)
		{
			gabriel = min(r, c) > 2;
		}
		else if (x == 5)
		{
			gabriel = !(min(r, c) == 3 && max(r, c) == 5);
		}
		else if (x == 6)
		{
			gabriel = min(r, c) > 3;
		}
		if (gabriel)
		{
			printf("Case #%d: GABRIEL\n",current_case);
		}
		else
		{
			printf("Case #%d: RICHARD\n",current_case);
		}
	}
}
