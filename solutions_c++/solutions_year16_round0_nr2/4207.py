#pragma warning(disable: 4996)

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
#include <unordered_set>
using namespace std;

#define CURRENT B
#define  A 0 //countin sheep
#define  B 1 //revenge of the pancakes
#define  C 2
#define  D 3

//countin sheep
#if (CURRENT == A)
#define NOT (0)
#define YES (1)
int m[10];
int nDone;

void setnum(int a)
{
	while (a)
	{
		int g = a % 10;
		if (m[g] == NOT)
		{
			m[a % 10] = YES;
			nDone++;
		}
		a = a / 10;
	}
}

int solve(int a)
{
	if (a == 0) return -1;
	
	memset(m, NOT, sizeof(m));
	nDone = 0;
	int i = 0;
	while (nDone<10)
	{
		++i;
		setnum(i*a);

	}

	return i*a;
}

int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("AL.out", "w", stdout);
	int nTest;

	//scanf("%d", &nTest);
	cin >> nTest;
	for (int i = 0; i < nTest; i++)
	{
		int input;
		cin >> input;
		int res = solve(input);
		cout << "Case #"<<i+1<<": ";
		if (res == -1)
		{
			cout << "INSOMNIA" << endl;
		}
		else
			cout << res << endl;
	}

	return 1;
}
#endif

//revenge of the pancakes
#if ( CURRENT == B )
#define NOT (0)
#define YES (1)
int m[10];
int nDone;



int solve(int a)
{
	return 1;
}

int main(void)
{
	freopen("B-large.in", "r", stdin);
	freopen("BL.out", "w", stdout);
	int nTest;

	//scanf("%d", &nTest);
	cin >> nTest;
	for (int i = 0; i < nTest; i++)
	{
		string  input;
		cin >> input;
		int res = 0;

		int len = input.length();
		if (input[len-1] == '-')
		{
			res++;
		}
		for (size_t i = 1; i < len; i++)
		{
			if (input[i] != input[i - 1])
				res++;
		}
	//	int res = solve(input);
	cout << "Case #" << i + 1 << ": ";
	/*		if (res == -1)
		{
			cout << "INSOMNIA" << endl;
		}
		else*/
			cout << res << endl;
	}

	return 1;
}

#endif

#if ( CURRENT ==C )
{

}

#endif

#if ( CURRENT ==D )
{

}

#endif