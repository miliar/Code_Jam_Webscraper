#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

typedef long long ll;
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ZERO(x) memset((x), 0, sizeof(x))
#define MAXN 2*10000500

using namespace std;

int main()
{
#ifdef DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T = 0;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int x, r, c;
		cin >> x >> r >> c;

		int cm = max(r, c);
		int rm = min(r, c);
		printf("Case #%d: ", i + 1);
		switch (x)
		{
		case 1:
			printf("GABRIEL\n");
			break;
		case 2:
			if ((rm == 1 && cm == 1) || (cm == 3 && rm == 1) || (cm == 3 && rm == 3))
			{
				printf("RICHARD\n");
			}
			else
			{
				printf("GABRIEL\n");
			}
			break;
		case 3:
			if ((rm == 2 && cm == 3) || (cm == 4 && rm == 3) || (cm == 3 && rm == 3))
			{
				printf("GABRIEL\n");
			}
			else
			{
				printf("RICHARD\n");
			}
			break;
		case 4:
			if ((rm == 3 && cm == 4) || (cm == 4 && rm == 4))
			{
				printf("GABRIEL\n");
			}
			else
			{
				printf("RICHARD\n");
			}
			break;
		}
	}

	return 0;
}