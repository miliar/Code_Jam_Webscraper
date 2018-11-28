#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int f(int p, int r, int s)
{
	int n = p + r + s;
	if (n == 1)
	{
		if (p == 1)
			return 1;
		if (r == 1)
			return 2;
		if (s == 1)
			return 3;
	}
	if (p * 2 > n)
		return -1;
	if (r * 2 > n)
		return -1;
	if (s * 2 > n)
		return -1;
	return f((p + r - s) / 2, (r + s - p) / 2, (s + p - r) / 2);
}

string print(int x, int n, int N)
{
	if (n == N)
	{
		if (x == 1)
			return "P";
		if (x == 2)
			return "R";
		if (x == 3)
			return "S";
	}
	else
	{
		if (x == 1)
		{
			string s1 = print(1, n + 1, N);
			string s2 = print(2, n + 1, N);
			return s1 < s2 ? s1 + s2 : s2 + s1;
		}
		if (x == 2)
		{
			string s1 = print(2, n + 1, N);
			string s2 = print(3, n + 1, N);
			return s1 < s2 ? s1 + s2 : s2 + s1;
		}
		if (x == 3)
		{
			string s1 = print(3, n + 1, N);
			string s2 = print(1, n + 1, N);
			return s1 < s2 ? s1 + s2 : s2 + s1;
		}
	}
}

void process(int t)
{
	int N, R, P, S;
	cin >> N >> R >> P >> S;
	int r = f(P, R, S);
	cout << "Case #" << t << ": ";
	if (r == -1)
	{
		cout << "IMPOSSIBLE";
	}
	else
	{
		string s = print(r, 0, N);
		cout << s;
	}
	cout << "\n";
}

int main()
{
	freopen("c:\\Projects\\CodeJam2016R2\\A\\A.in", "r", stdin);
	freopen("c:\\Projects\\CodeJam2016R2\\A\\A.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
		process(t+1);



	fclose(stdin);
	fclose(stdout);
	return 0;
}