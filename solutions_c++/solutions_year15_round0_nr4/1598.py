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
/*  //A Standing Ovation
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
*/


int Cal(int x, int r, int c)
{
	if ((r*c)%x)
		return 1;

	if ((r < x) && (c < x))
		return 1;

	if( x < 3)
		return 0;

	if (x == 3)
	{		
		if ((r == 1) || (c==1))
		{
			return 1;
		}
		return 0;
	}

	if (x==4)
	{
		if ((r + c) >= 7)
			return 0;
		return 1;
	}

}

//D Ominous Omino
int main(void)
{
	//freopen("D-large.in", "r", stdin);
	freopen("D-small-attempt0.in", "r", stdin);
	//freopen("1.txt", "r", stdin);
	freopen("D.out", "w", stdout);
	int nTest, x,r,c;
	char result[2][8] = { "GABRIEL", "RICHARD" };

	scanf("%d", &nTest);

	for (int i = 0; i < nTest; i++)
	{
		scanf("%d %d %d", &x, &r, &c);
		cout << "Case #" << i + 1 << ": " << result[Cal(x, r, c)] << endl;
	}

	return 0;
}