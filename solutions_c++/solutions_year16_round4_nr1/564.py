// 2011_2.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <functional>
#include <vector>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <bitset>
#include <list>
#include <iomanip>      // std::setprecision

using namespace std;

FILE * in, *out;

#define fo(a,b,c) for(int a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

#define LL long long

int ri() { int a; fscanf(in, "%d", &a); return a; }
double rf() { double a; fscanf(in, "%lf", &a); return a; }
char sbuf[100005];
string rstr()
{
	//fscanf(in, "%lf", sbuf); 
	char c;
	char * b = sbuf;
	while (c = fgetc(in))
	{
		if (c == '\n' || c == 255) break;
		*b++ = c;
	}
	*b = 0;
	return sbuf;
}


int nod(int a, int b)
{
	if (a == 1 || b == 1) return 1;
	if (a == 0) return b;
	if (b == 0) return a;

	return nod(b%a, a);
}

vector<int> primes;
void calculatePrimes()
{
	primes.push_back(2);
	for (int i = 3; i < 500; i += 2)
	{
		bool bFound = false;
		int m = (int)sqrt((float)i);
		for (int j = 1; j < primes.size() && !bFound && primes[j] <= m; j++)
			bFound = ((i%primes[j]) == 0);
		if (!bFound)
			primes.push_back(i);
	}
}

struct Counts
{
	int p, r, s;
	Counts() { p = r = s = 0;  }
	bool operator == (Counts & r1) { return r1.p == p && r1.r == r && r1.s == s; }
};

Counts pre[3][14];
string str[3][14];


void mySort(string & in)
{
	for (int i = 2; i < in.size(); i *= 2)
	{
		for (int j = 0; j*i < in.size(); j += 2)
		{
			bool bCoorect = true;
			for (int k = 0; k < i && bCoorect; k++)
				bCoorect = (in[i*j+k] <= in[i*(j + 1) + k]);
			if(!bCoorect)
			{
				for (int k = 0; k < i; k++)
					swap(in[i*j + k],in[i*(j + 1) + k]);
			}

		}
	}
}

void fill()
{
	pre[0][0].p = 1;
	pre[1][0].r = 1;
	pre[2][0].s = 1;
	str[0][0] = "P";
	str[1][0] = "R";
	str[2][0] = "S";


	for (int i = 1; i < 14; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			pre[j][i].p = pre[j][i - 1].p + pre[j][i - 1].s;
			pre[j][i].s = pre[j][i - 1].s + pre[j][i - 1].r;
			pre[j][i].r = pre[j][i - 1].r + pre[j][i - 1].p;

			for (int k = 0; k < str[j][i - 1].size(); k++)
			{
				if (str[j][i - 1][k] == 'P')
					str[j][i] += "PR";
				else if (str[j][i - 1][k] == 'S')
					str[j][i] += "PS";
				else if (str[j][i - 1][k] == 'R')
					str[j][i] += "RS";
			}
			mySort(str[j][i]);
		}

	}
}


int main()
{
	int T;
	cin >> T;
	fill();

	string test = "PRRSPSPR";
	mySort(test);


	for (int t = 1; t <= T; t++)
	{
		int n;
		Counts cn;
		cin >> n >> cn.r >> cn.p >> cn.s;

		cout << "Case #" << t << ": ";
		if (cn == pre[0][n])
			cout << str[0][n];
		else if (cn == pre[1][n])
			cout << str[1][n];
		else if (cn == pre[2][n])
			cout << str[2][n];
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}


	return 0;
}