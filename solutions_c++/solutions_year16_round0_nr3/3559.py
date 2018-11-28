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

#define CURRENT C
#define  A 0 //countin sheep
#define  B 1 //revenge of the pancakes
#define  C 2 //jamcoin
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

int len;
int J;
//int a[16];
uint64_t num10;
uint64_t num2;
uint64_t divs[9];



uint64_t isPrime(uint64_t a)
{
	if (a<=3)
		return -1;
	
	if ((a & 1) == 0)
		return 2;
	
	uint64_t sq = (uint64_t)sqrt(a);

	for (uint64_t i = 3; i <= sq; i++)
	{
		if (a%i == 0)
			return i;
	}
	return -1;
}

uint64_t getByBase(uint64_t b)
{
	if (b == 2)
		return num2;

	uint64_t res = 0;
	uint64_t tmp = num2;
	uint64_t base = 1;
	while (tmp)
	{
		res += (tmp % 2)*base;
		base *= b;
		tmp = tmp >>1;
	}
	return res;
	/*
	switch (b)
	{
	case 2:
		while (b)
		{

		}
		break;
	case 3:
		break;
	case 4:
		break;
	case 5:
		break;
	case 6:
		break;
	case 7:
		break;
	case 8:
		break;
	case 9:
		break;
	default:
		break;
	}*/
}

void solve()
{
	//num2-=2;
	while (1)
	{
		num2+=2;
		int numOfNonPrime = 0;
		for (uint64_t base = 2; base <= 10; base++)
		{
			uint64_t tmp = isPrime(getByBase(base));
			if (tmp == -1)
				break;
			else
			{
				numOfNonPrime++;
				divs[base - 2] = tmp;
			}
				
		}

		if (numOfNonPrime == 9)
			return;
	}
}

int main(void)
{
	freopen("1.txt", "r", stdin);
	freopen("Cs.out", "w", stdout);
	int nTest;

	//scanf("%d", &nTest);
	cin >> nTest;
	for (int i = 0; i < nTest; i++)
	{
		cin >> len >> J;

		num2 = 0x8001;
		num2 -= 2;

		cout << "Case #" << i + 1 << ":"<<endl;
		for (int i = J - 1; i >= 0; i--)
		{
			solve();


			for (int i = len-1; i >= 0; i--)
				cout << ((num2 >> i) & 1);


			for (int j = 0; j < 9; j++)
			{
				cout << " " << divs[j];
			}
			cout << endl;
			fflush(stdout);
		}

	}

	return 0;
}


#endif

#if ( CURRENT ==D )


#endif