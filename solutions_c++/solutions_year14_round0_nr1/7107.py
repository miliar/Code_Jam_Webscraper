#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <deque>
#include <string>

using namespace std;

typedef vector<vector<int> > matrix;
int t;

void solve(int number, int a, int b, matrix x, matrix y)
{
	vector<int> inter;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
			if (x[a - 1][i] == y[b - 1][j])
			{
				inter.push_back(x[a - 1][i]);
				break;
			}
	}

	printf("Case #%d: ", number + 1);
	if (inter.size() == 0)
		printf("Volunteer cheated!\n");
	else if (inter.size() == 1)
		printf("%d\n", inter[0]);
	else
		printf("Bad magician!\n");
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
	{
		int a, b;
		vector< vector<int> > x;
		vector< vector<int> > y;

		x.resize(4, vector<int>());
		y.resize(4, vector<int>());

		scanf("%d", &a);
		for (int j = 0; j < 4; ++j)
		for (int k = 0; k < 4; ++k)
		{
			int t; scanf("%d", &t);
			x[j].push_back(t);
		}
		scanf("%d", &b);
		for (int j = 0; j < 4; ++j)
		for (int k = 0; k < 4; ++k)
		{
			int t; scanf("%d", &t);
			y[j].push_back(t);
		}

		solve(i, a, b, x, y);
	}

	return 0;
}