#include <stdio.h>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cfloat>

using namespace std;

typedef long long ll;

ofstream fout("ijkout.txt");
ifstream fin("ijkin.txt");

const int O	= 0;
const int I = 1;
const int J = 2;
const int K = 3;
const int MO = 4;
const int MI = 5;
const int MJ = 6;
const int MK = 7;
							
const int table[8][8] = {
	{ O,	I,	J,	K,	MO,	MI,	MJ,	MK	},
	{ I,	MO,	K,	MJ,	MI,	O,	MK,	J	},
	{ J,	MK,	MO,	I,	MJ,	K,	O,	MI	},
	{ K,	J,	MI,	MO,	MK,	MJ,	I,	O	},
	{ MO,	MI, MJ,	MK,	O,	I,	J,	K	},
	{ MI,	O,	MK,	J,	I,	MO,	K,	MJ	},
	{ MJ,	K,	O,	MI,	J,	MK,	MO,	I	},
	{ MK,	MJ,	I,	O,	K,	J,	MI,	MO	}
};

int l;
int s[10000];

int getBegin()
{
	int at = 1;
	int cur = s[0];
	while (at < l && cur != I)
	{
		cur = table[cur][s[at++]];
	}
	return at;
}

int getEnd()
{
	int at = l - 2;
	int cur = s[l - 1];
	while (at >= 0 && cur != K)
	{
		cur = table[s[at--]][cur];
	}
	return at;
}

bool solve()
{
	int begin = getBegin();
	int end = getEnd();
	
	int cur = O;
	for (int i = begin; i <= end; i++)
	{
		cur = table[cur][s[i]];
	}
	return cur == J;
}

int main()
{
	int numTests;
	fin >> numTests;
	for (int testIndex = 1; testIndex <= numTests; testIndex++)
	{
		int inl, inx;
		fin >> inl >> inx;
		l = inl * inx;
		for (int i = 0; i < inl; i++)
		{
			char c;
			fin >> c;
			int in = (c == 'i' ? I : (c == 'j' ? J : K));
			for (int x = 0; x < inx; x++)
			{
				s[i + x * inl] = in;
			}
		}
		fout << "Case #" << testIndex << ": " << (solve() ? "YES" : "NO") << endl;
	}
	
	return 0;
}

/*



*/