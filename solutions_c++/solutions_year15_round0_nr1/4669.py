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
		int sMax;
		string s;
		scanf("%d", &sMax);
		cin >> s;
		int curCntPeoples = 0;
		int myFriends = 0;
		for (size_t curSh = 0; curSh < sMax + 1; curSh++)
		{
			if (curCntPeoples < curSh)
			{
				myFriends += curSh - curCntPeoples;
				curCntPeoples += curSh - curCntPeoples;
			}
			curCntPeoples += s[curSh] - '0';
		}
		printf("Case #%d: %d\n", test, myFriends);
	}

	return 0;
}
