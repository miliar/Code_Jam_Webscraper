#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <list>
#include <deque>
#include <algorithm>

using namespace std;

const int MAXN = 12;
string Ss[MAXN + 1], Rs[MAXN + 1], Ps[MAXN + 1];

int N, P, R, S;
string result;

string GenP(int n);
string GenR(int n);
string GenS(int n);

string GenP(int n)
{
	if (Ps[n].length() == 0) {
		if (GenP(n - 1) < GenR(n - 1))
			Ps[n] = GenP(n - 1) + GenR(n - 1);
		else
			Ps[n] = GenR(n - 1) + GenP(n - 1);
	}
	return Ps[n];
}

string GenR(int n)
{
	if (Rs[n].length() == 0) 
	{
		if (GenR(n - 1) < GenS(n - 1))
			Rs[n] = GenR(n - 1) + GenS(n - 1);
		else
			Rs[n] = GenS(n - 1) + GenR(n - 1);
	}
	return Rs[n];
}

string GenS(int n)
{
	if (Ss[n].length() == 0)
	{
		if (GenP(n - 1) < GenS(n - 1))
			Ss[n] = GenP(n - 1) + GenS(n - 1);
		else
			Ss[n] = GenS(n - 1) + GenP(n - 1);
	}
	return Ss[n];
}

static void Init()
{
	Ss[0] = "S";
	Rs[0] = "R";
	Ps[0] = "P";
	GenP(MAXN);
	GenR(MAXN);
	GenS(MAXN);
}

bool Count(const string &str, int p, int r, int s)
{
	for (int i = 0; i < (int)str.length(); ++i)
	{
		if (str[i] == 'P')
			--p;
		else if (str[i] == 'R')
			--r;
		else if (str[i] == 'S')
			--s;
	}
	return p == 0 && r == 0 && s == 0;
}

void Work()
{
	result = "IMPOSSIBLE";
	if (Count(Ps[N], P, R, S))
		result = Ps[N];
	else if (Count(Rs[N], P, R, S))
		result = Rs[N];
	else if (Count(Ss[N], P, R, S))
		result = Ss[N];
}

void Read()
{
	scanf("%d%d%d%d", &N, &R, &P, &S);
}

void Write(int t)
{
	printf("Case #%d: %s\n", t, result.c_str());
}

int main()
{
	int i, t;
	scanf("%d", &t);
	Init();
	for (i = 0; i < t; ++i)
	{
		Read();
		Work();
		Write(i + 1);
	}
	return 0;
}
