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

int N, X, a, out;
vector<int> v;

int find_greatest_but_smaller_or_equal(int x, int nIdx)
{
	int idx = -1;
	for (int i = 0; i < v.size(); ++i)
	{
		if (v[i] <= x && i != nIdx) idx = i;
	}
	return idx;
}

void evaluate()
{
	out = 0;

	for (int i = v.size() - 1; i >= 0; --i)
	{
		if (v[i] == -1u/2) continue;
		int idx = find_greatest_but_smaller_or_equal(X - v[i], i);
		v[i] = -1u/2;
		if (idx != -1) v[idx] = -1u/2;
		
		out++;

	}

	printf("%d\n", out);
}

void input()
{
	scanf("%d %d", &N, &X);
	v.clear();
	for (int i = 0; i < N; ++i)
	{
		scanf("%d", &a);
		v.push_back(a);
	}
	sort(v.begin(), v.end());
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