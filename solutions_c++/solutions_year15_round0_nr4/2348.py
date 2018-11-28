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


int main()
{
	///*
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout); /**/
	int nTests;
	scanf("%d", &nTests);
	for (int test = 1; test <= nTests; test++)
	{
		printf("Case #%d: ", test);
		int x, r, c;
		scanf("%d %d %d", &x, &r, &c);
		if (r > c) swap(r, c);
		if (x == 1) puts("GABRIEL");
		else if (x == 2)
			if (r%2 == 0 || c%2 == 0)
				puts("GABRIEL");
			else
				puts("RICHARD");
		else if (x == 3)
			if ((r == 3 || c == 3) && r != 1)
				puts("GABRIEL");
			else
				puts("RICHARD");
		else if (x == 4)
			if (c < 4 || r == 1 || r == 2)
				puts("RICHARD");
			else
				puts("GABRIEL");
	}

	return 0;
}
