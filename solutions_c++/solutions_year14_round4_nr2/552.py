#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <stack>
#include <cmath>
#include <queue>
using namespace std;

int N, a[10000];
int leftBorder, rightBorder;

int getSmallest()
{
	int idx = leftBorder;
	for (int i = leftBorder; i <= rightBorder; ++i)
	{
		if (a[i] < a[idx]) 
		{
			idx = i;
		}
	}
	return idx;
}

void evaluate()
{
	int out = 0, k = N - 1;

	while (k--)
	{
	int idx = getSmallest();

	int l = idx - leftBorder;
	int r = rightBorder - idx;

	if (l < r) 
	{
		while (idx != leftBorder)
		{
			swap(a[idx], a[idx - 1]);
			--idx;
		}
		leftBorder++;
		out += l;
	}
	else
	{
		while (idx != rightBorder)
		{
			swap(a[idx], a[idx + 1]);
			++idx;
		}
		rightBorder--;
		out += r;
	}
	}
	printf("%d\n", out);

}

void input()
{
	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &a[i]);
	}
	leftBorder = 0;
	rightBorder = N - 1;

	evaluate();
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int T;
	scanf("%d", &T);

	for (int test = 1; test <= T; ++test)
	{
		printf("Case #%d: ", test);
		input();
	}

	return 0;
}