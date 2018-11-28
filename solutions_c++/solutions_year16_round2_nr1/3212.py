#include <stdio.h>
#include <string>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

int N;
string S;
int MEMO[26];
string nums[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

inline void init()
{
	cin >> S;
	memset(MEMO, 0, sizeof(MEMO));
}

inline void solve()
{
	int i, j, c;

	for (i = 0; i < S.length(); i++)
		MEMO[S[i] - 'A'] ++;

	vector<int> V;

	if (MEMO['Z' - 'A'] != 0)
	{
		c = MEMO['Z' - 'A'];

		for (i = 0; i < c; i++)
			V.push_back(0);

		for (i = 0; i < nums[0].size(); i++)
			MEMO[nums[0][i] - 'A'] -= c;
	}

	if (MEMO['U' - 'A'] != 0)
	{
		c = MEMO['U' - 'A'];
		for (i = 0; i < c; i++)
			V.push_back(4);

		for (i = 0; i < nums[4].size(); i++)
			MEMO[nums[4][i] - 'A'] -= c;
	}

	if (MEMO['F' - 'A'] != 0)
	{
		c = MEMO['F' - 'A'];

		for (i = 0; i < c; i++)
			V.push_back(5);

		for (i = 0; i < nums[5].size(); i++)
			MEMO[nums[5][i] - 'A'] -= c;
	}

	if (MEMO['V' - 'A'] != 0)
	{
		c = MEMO['V' - 'A'];

		for (i = 0; i < c; i++)
			V.push_back(7);

		for (i = 0; i < nums[7].size(); i++)
			MEMO[nums[7][i] - 'A'] -= c;
	}

	if (MEMO['W' - 'A'] != 0)
	{
		c = MEMO['W' - 'A'];

		for (i = 0; i < c; i++)
			V.push_back(2);

		for (i = 0; i < nums[2].size(); i++)
			MEMO[nums[2][i] - 'A'] -= c;
	}

	if (MEMO['O' - 'A'] != 0)
	{
		c = MEMO['O' - 'A'];

		for (i = 0; i < c; i++)
			V.push_back(1);

		for (i = 0; i < nums[1].size(); i++)
			MEMO[nums[1][i] - 'A'] -= c;
	}

	if (MEMO['S' - 'A'] != 0)
	{
		c = MEMO['S' - 'A'];

		for (i = 0; i < c; i++)
			V.push_back(6);

		for (i = 0; i < nums[6].size(); i++)
			MEMO[nums[6][i] - 'A'] -= c;
	}

	if (MEMO['G' - 'A'] != 0)
	{
		c = MEMO['G' - 'A'];

		for (i = 0; i < c; i++)
			V.push_back(8);

		for (i = 0; i < nums[8].size(); i++)
			MEMO[nums[8][i] - 'A'] -= c;
	}

	if (MEMO['T' - 'A'] != 0)
	{
		c = MEMO['T' - 'A'];

		for (i = 0; i < c; i++)
			V.push_back(3);

		for (i = 0; i < nums[3].size(); i++)
			MEMO[nums[3][i] - 'A'] -= c;
	}

	if (MEMO['I' - 'A'] != 0)
	{
		c = MEMO['I' - 'A'];

		for (i = 0; i < c; i++)
			V.push_back(9);

		for (i = 0; i < nums[9].size(); i++)
			MEMO[nums[9][i] - 'A'] -= c;
	}

	sort(V.begin(), V.end());
	for (i = 0; i < V.size(); i++)
		printf("%d", V[i]);

	putchar('\n');
}

int main()
{
	int T, i;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);

	for (i = 1; i <= T; i++)
	{
		init();
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}