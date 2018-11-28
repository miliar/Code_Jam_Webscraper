#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int gx, gr, gc, gn;

bool canFillBoard()
{
	if(gx == 1)
	{
		// always possible.
		return true;
	}
	if(gn % gx)
	{
		// always impossible.
		return false;
	}

	// 2-omino
	if(gx == 2)
	{
		return true;
	}

	// 3-omino
	if(gx == 3)
	{
		if(gn < 6)
		{
			return false;
		}
		return true;
	}

	// 4-omino
	if(gn >= 12)
	{
		return true;
	}
	return false;
}

void solve(int nCase)
{
	cin >> gx >> gr >> gc;

	gn = (gr * gc);
	if(canFillBoard())
		printf("Case #%d: GABRIEL\n", nCase);
	else
		printf("Case #%d: RICHARD\n", nCase);
}


int main(int argc, char cargv[])
{
	int n, i;
	// freopen("02.in", "r", stdin);
	
	scanf("%d", &n);
	for(i=0; i<n; i++)
	{
		solve(i+1);
	}
	return 0;
}
