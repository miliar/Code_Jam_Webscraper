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

// ans[C-1][W-1]
const int ans[10][10] =
{
	{1},
	{2, 2},
	{3, 3, 3},
	{4, 3, 4, 4},
	{5, 4, 4, 5, 5},
	{6, 4, 4, 5, 6, 6},
	{7, 5, 5, 5, 6, 7, 7},
	{8, 5, 5, 5, 6, 7, 8, 8},
	{9, 6, 5, 6, 6, 7, 8, 9, 9},
	{10, 6, 6, 6, 6, 7, 8, 9, 10, 10},
};


int main(void)
{
#ifdef USEFILE
	FILE* inf = freopen("A.in", "r", stdin);
	FILE* outf = freopen("A_out.txt.", "w", stdout);
#endif

	int tc;
	cin >> tc;

	for(int testNum = 1; testNum <= tc; testNum++)
	{
		int r, c, w;	// r*c grid / w: width of the ship
		cin >> r >> c >> w;

		
		printf("Case #%d: %d\n", testNum, ans[c-1][w-1]);
	}


#ifdef USEFILE
	fclose(inf);
	fclose(outf);
#endif

	return 0;
}