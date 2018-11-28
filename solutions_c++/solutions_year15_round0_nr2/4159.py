#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <iostream>
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
int res;
void foo(int cnt, int plates[1000], int nPlates)
{
	int maxInd = 0;
	for (int plate = 0; plate < nPlates; plate++)
		if (plates[maxInd] < plates[plate])
			maxInd = plate;
	if (cnt + plates[maxInd] < res)
		res = cnt + plates[maxInd];
	if (plates[maxInd] == 1)
	{
		return;
	}
	nPlates++;
	plates[nPlates - 1] = 0;
	for (int i = 2; i <= (int) ceil(1.0 * plates[maxInd] / 2); i++)
	{
		plates[maxInd] -= i;
		plates[nPlates - 1] = i;
		foo(cnt + 1, plates, nPlates);
		plates[maxInd] += i;
		plates[nPlates - 1] = 0;
	}
}

int main()
{
	///*
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout); /**/
	int nTests;
	scanf("%d", &nTests);
	for (int test = 1; test <= nTests; test++)
	{
		int nPlates;
		res = 0;
		scanf("%d", &nPlates);
		int plates[1000];
		for (int plate = 0; plate < nPlates; plate++)
			scanf("%d", &plates[plate]);
		int maxInd = 0;
		for (int plate = 0; plate < nPlates; plate++)
			if (plates[maxInd] < plates[plate])
				maxInd = plate;
		res = plates[maxInd];
		foo(0, plates, nPlates);
		printf("Case #%d: %d\n", test, res);
	}

	return 0;
}
