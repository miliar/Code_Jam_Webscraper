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
#include <math.h>
using namespace std;
//A Standing Ovation
/*  
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

//D Ominous Omino
/*

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

int m = min(r, c);
if (x&1)
{
if (m>= ((x+1)/2))
{
return 0;
}
return 1;
}
else
{
if (m >= (x/2 -1))
{
return 0;
}
return 1;
}

}


int main(void)
{
freopen("D-large.in", "r", stdin);
//freopen("D-small-attempt0.in", "r", stdin);
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
*/


//C Dijkstra
/*
#define i (2)
#define j (3)
#define k (4)

int matrix[5][5] = {
	{ 0, 1, i, j, k },
	{ 1, 1, i, j, k },
	{ i, i, -1, k, -j },
	{ j, j, -k, -1, i },
	{ k, k, j, -i, -1 }
};

int gsin = 1;

int Get(int a, int b)
{

}


int main(void)
	{
		//freopen("C-large.in", "r", stdin);
		//freopen("C-small-attempt0.in", "r", stdin);
		freopen("1.txt", "r", stdin);
		freopen("D.out", "w", stdout);
		int nTest, l,x;


		scanf("%d", &nTest);

		for (int i = 0; i < nTest; i++)
		{
			scanf("%d %d ", &l,&x);

			cout << "Case #" << i + 1 << ": " << result[Cal(x, r, c)] << endl;
		}

		return 0;
	}

	*/

//B Inifinite House of Pancakes
/**/
int p[1005];
int maxValue;
int Cal(int d)
{
	int minimum = 0x7FFFffff;
	int  maxChunk = maxValue;// (maxValue + 1) / 2;
	int totalMinutes = 0;
	for (int chunk = 1; chunk <= maxChunk ; chunk++)
	{
		//try all the diners
		totalMinutes = chunk;
		for (int i = 0; i < d ; i++)
		{
			if (p[i]<=chunk)
				continue;
			if (p[i] % chunk)
				totalMinutes += (p[i] / chunk);
			else
				totalMinutes += (p[i] / chunk-1);
		}
		minimum = min(totalMinutes, minimum);
	}
	return minimum;
}

int main(void)
{
	freopen("B-large.in", "r", stdin);
	//freopen("B-small-attempt1.in", "r", stdin);
	//freopen("1.txt", "r", stdin);
	freopen("B_Large.out", "w", stdout);
	int nTest, d;


	scanf("%d", &nTest);

	for (int i = 0; i < nTest; i++)
	{
		maxValue = 0;
		scanf("%d", &d);
		for (int j = 0; j < d; j++)
		{
			scanf("%d", p + j);
			maxValue = max(maxValue, p[j]);
		}
		cout << "Case #" << i + 1 << ": " << Cal(d) << endl;
	}

	return 0;
}



