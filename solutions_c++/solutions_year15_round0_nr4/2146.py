#if !ONLINE_JUDGE
#define _CRT_SECURE_NO_WARNINGS
#endif
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <stack>
using namespace std;

bool solve(int,int,int);

int main()
{
#if !ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output1.out", "w", stdout);
#endif
	
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++)
	{
		int x, r, c;
		cin >> x >> r >> c;
		cout << "Case #" << z << ": ";
		if (solve(x,r,c))
		{
			cout << "RICHARD" << endl;
		}
		else cout << "GABRIEL" << endl;

	}
	return 0;
}

bool solve(int x, int r, int c)
{
	if (x == 1) return false;
	else if (x == 2)
	{
		if ((r*c) % 2 == 0) return false;
		else return true;
	}
	else if (x == 3)
	{
		if (r == 1 || c == 1 || (r*c) % 3 != 0) return true;
		else return false;
	}
	else
	{
		if ((r*c) % 4 != 0 || r <= 2 || c <= 2) return true;
		else return false;
	}
}