#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;

int Cal(int Smax, char* aud)
{
	if (Smax == 0)
		return 0;
	int totalStand = 0;
	int friend2Invite = 0;
	int first = aud[0] - '0';
	if (first == 0)
	{
		totalStand = friend2Invite = 1;
	}
	else
	{
		totalStand = first;
	}

	for (int i = 1; i <= Smax ; i++)
	{
		int p = aud[i] - '0';
		if (totalStand < i)
		{
			friend2Invite += (i - totalStand);
			totalStand = i;
			totalStand += p;
		}
		else
		{
			totalStand += p;
		}
	}
	return friend2Invite;
}

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int nTest;

	scanf("%d", &nTest);
	int Smax;
	char aud[1024];
	for (int i = 0; i < nTest; i++)
	{
		scanf("%d %1020s", &Smax, aud);
		cout << "Case #" << i + 1 << ": "<<Cal(Smax, aud)<<endl;
	}

	return 0;
}