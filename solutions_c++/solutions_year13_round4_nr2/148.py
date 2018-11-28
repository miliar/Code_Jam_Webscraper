#include <cassert>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>

using namespace std;

long long bestPlace1(int step, long long stronger)
{
	if(stronger == 0)
		return 0;

	long long weaker = (1LL << (step + 1)) - stronger - 1;
	return (1LL << step) + bestPlace1(step - 1, max(0LL, stronger - 1) / 2);
}

bool test1(int n, long long p, long long s)
{
	long long bp = 1 + bestPlace1(n - 1, s);
	return bp <= p;
}

long long firstTask(int n, long long p)
{
	const long long size = 1LL << n;

	if(test1(n, p, size - 1))
		return size - 1;

	long long l = 0, r = size - 1;

	while(r - l > 1)
	{
		long long m = (r + l) / 2;
		if(test1(n, p, m))
			l = m;
		else
			r = m;
	}

	return l;
/*
	long long r = 0;
	for(long long i = 0; i < size; i++)
	{
		long long bp = 1 + bestPlace1(n - 1, i);
		if(bp > p)
			break;
		else
			r = max(r, i);
	}

	return r;*/
}


long long bestPlace2(int step, long long stronger)
{
	long long weaker = (1LL << (step + 1)) - stronger - 1;

	if(weaker == 0)
		return (1LL << (step + 1)) - 1;

	return bestPlace2(step - 1, (stronger + 1) / 2);
}

bool test2(int n, long long p, long long s)
{
	long long bp = 1 + bestPlace2(n - 1, s);
	return bp <= p;
}

long long secondTask(int n, long long p)
{
	const long long size = 1LL << n;

	if(test2(n, p, size - 1))
		return size - 1;

	long long l = 0, r = size - 1;

	while(r - l > 1)
	{
		long long m = (r + l) / 2;
		if(test2(n, p, m))
			l = m;
		else
			r = m;
	}

	return l;

/*	long long r = 0;
	for(long long i = 0; i < size; i++)
	{
		long long bp = 1 + bestPlace2(n - 1, i);
		if(bp > p)
			break;
		else
			r = max(r, i);
	}

	return r;*/
}

void solve()
{
	int n;
	long long p;
	cin >> n >> p;

	cout << firstTask(n, p) << " " << secondTask(n, p);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%i\n", &t);

	for(int ti = 1; ti <= t; ti++)
	{
		cout << "Case #" << ti << ": ";
		solve();
		cout << "\n";
	}

	return 0;
}
