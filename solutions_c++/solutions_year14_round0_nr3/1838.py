#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
int A[1000][1000];
int R, C, M, f;
int d[1000];
int cur;
bool correct()
{
	int p[10];
	p[1] = 0;
	p[2] = 0;
	p[3] = 0;
	p[4] = 0;
	p[5] = 0;
	for (int i = 1; i <= 5; i++)
	{
		p[i] = d[i];
	}
	sort(p + 1, p + R + 1);
	reverse(p + 1, p + R + 1);
	for (int i = 1; i <= R; i++)
	{
		if (p[i] == 1 && R > 1 && C > 1)
		{
			return false;
		}
	}
	if (p[2] == 0 && R > 1)
	{
		return false;
	}
	if (p[1] != p[2] && R > 1 && C > 1)
	{
		return false;
	}
	cout << "Case" << " #" << cur << ":" << endl;
	cout << "c";
	for (int i = 1; i <= R; i++)
	{
		for (int j = 1; j <= C; j++)
		{
			if (i != 1 || j != 1)
			{
				if (j <= p[i])
				{
					cout << ".";
				}
				else
				{
					cout << "*";
				}
			}
		}
		cout << endl;
	}
	return true;
}
void dfs(int k, int s)
{
	if (f == 0)
	{
		if (k > R)
		{

			if (s == R * C - M)
			{
				if (correct())
				{
					f = 1;
					return;
				}
			}
		}
		else
		{
			for (int i = 0; i <= C; i++)
			{
				d[k] = i;
				dfs(k + 1, s + i);
			}
		}
	}
}
int main()
{
	int t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",  stdout);
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		cur = i;
		f = 0;
		for (int j = 1; j <= 5; j++)
		{
			d[j] = 0;
		}
		cin >> R >> C >> M;
		if (M == R * C - 1)
		{
			cout << "Case" << " #" << cur << ":" << endl;
			cout << "c";
			for (int ii = 1; ii <= R; ii++)
			{
				for (int j = 1; j <= C; j++)
				{
					if (ii != 1 || j != 1)
					{
						cout << "*";
					}
				}
				cout << endl;
			}
			continue;
		}
		dfs(1, 0);
		if (f == 0)
		{
			cout << "Case" << " #" << cur << ":" << endl;
			cout << "Impossible" << endl;
		}
	}
	return 0;
}