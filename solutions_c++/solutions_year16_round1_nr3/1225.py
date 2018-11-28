#pragma comment(linker, "/STACK:268435456")
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <fstream>
#include <functional>
#include <stdio.h>
#include <sstream>
#include <bitset>
#include <limits.h>
#include <stack>
using namespace std;

#define sqr(a) ((a)*(a))
typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;

const ld EPS = 1e-16;

i64 t, tt, n, m = 0;
vector <i64> a;
vector <vector <i64> > b;
vector <int> state;
stack <i64> s;

void dfs(i64 v, i64 start, i64 depth)
{
	s.push(v);

	if (state[v] == 1)
		for (int i = 0; i < n; ++i)
			if (!state[i])
			{
				if (a[i] == v)
					state[i] = 1;
				else
					state[i] = 2;
				dfs(i, start, depth + 1);
			}

	
	if (!state[a[v]])
	{
		if (a[a[v]] ==  v)
			state[a[v]] = 1;
		else
			state[a[v]] = 2;
		dfs(a[v], start, depth + 1);
	}
		

	if (a[v] == start || state[v] == 1)
		m = max(m, depth);

	s.pop();
	state[v] = 0;
}


int main()
{
	cout.precision(50);
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		cin >> n;

		m = 0;
		a.clear();
		a.resize(n);
		b.clear();
		b.resize(n);
		state.clear();
		state.resize(n);

		for (int j = 0; j < n; ++j)
		{
			cin >> tt;
			a[j] = tt - 1;
			b[tt - 1].push_back(j);
		}

		for (int j = 0; j < n; ++j)
		{
			state[j] = 2;
			dfs(j, j, 1);
			for (int k = 0; k < n; ++k)
				state[k] = 0;
		}

		cout << "Case #" << i + 1 << ": " << m << endl;
	}


	return 0;
}
