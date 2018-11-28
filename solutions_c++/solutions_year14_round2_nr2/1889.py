#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <string>
#include <memory.h>
#include <limits.h>
#include <queue>

using namespace std;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	if (s.size() != 0)
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
}

int main()
{
	prepare("");
	int test;
	cin >> test;
	for (size_t t = 0; t < test; t++)
	{
		int a, b, k;
		cin >> a >> b >> k;
		cout << "Case #" << t + 1 << ": ";
		int ans = 0;
		for (size_t i = 0; i < a; i++)
		{
			for (size_t j = 0; j < b; j++)
			{
				if (k > int(i&j))
				{
					ans++;
				}
			}
		}
		cout << ans << endl;
	}
	return 0;
}
