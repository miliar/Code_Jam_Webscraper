#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

int a[2000], b[2000];
int n;

int calc(int l, int r, int sign)
{
	if (l > r)
		return 0;
	int res = 0;
	for (int i = l; i <= r; i++)
		for (int j = l; j < r; j++)
			if ((b[j] - b[j + 1]) * sign > 0)
			{
		res++;
		swap(b[j], b[j + 1]);
			}
	return res;
}

int move(int l, int r)
{
	if (l < r)
	{
		for (int i = l; i < r; i++)
			swap(b[i], b[i + 1]);
	}
	else
	{
		for (int i = l; i > r; i--)
			swap(b[i], b[i - 1]);
	}

	return a - b;
}

int solve1()
{
	int mid = 0;
	for (int i = 0; i < n; i++)
	{
		if (a[i] > a[mid])
			mid = i;
	}

	int ans = 1e9;
	for (int gr = 0; gr < n; gr++)
	{
		for (int i = 0; i < n; i++)
			b[i] = a[i];
		int loc = 0;
		loc += abs(mid - gr);

		move(mid, gr);
		//swap(b[mid], b[gr]);

		loc += calc(0, gr - 1, 1);
		loc += calc(gr + 1, n - 1, -1);
		ans = min(ans, loc);
	}
	return ans;
}


int ind[2000];
bool used[2000];

bool good()
{
	int i = 0;
	while (i + 1 < n && a[ind[i]] < a[ind[i + 1]])
		i++;
	while (i + 1 < n && a[ind[i]] > a[ind[i + 1]])
		i++;
	return i == n - 1;
}

int solve2()
{
	for (int i = 0; i < n; i++)
		ind[i] = i;

	int res = 1e9;
	do
	{
		if (!good())
			continue;

		//int ind[] = { 2, 0, 9, 8, 1, 7, 6, 3, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, };


		for (int i = 0; i < n; i++)
		{
			b[i] = a[i];
			used[i] = 0;
		}

		int loc = 0;
		for (int i = 0; i < n; i++)
		{
			int val = a[ind[i]];
			int pos = 0;
			while (b[pos] != val)
				pos++;
			for (int j = pos; j > i; j--)
			{
				swap(b[j], b[j - 1]);
				loc++;
			}
		}

		if (res > loc)
			res = min(res, loc);
	} while (next_permutation(ind, ind + n));

	return res;
}

void Solution()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}
	
	//printf("%d ", solve1());
	printf("%d", solve2());
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		Solution();
		printf("\n");
	}
}