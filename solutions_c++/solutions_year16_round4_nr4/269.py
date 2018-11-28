#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <iostream>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000ll;
const double eps = 1e-8;

const int NN = 10;

int n;
bool can[NN][NN];
bool can2[NN][NN];
int sel[NN];

char s[NN];

int order[NN];
bool used[NN];

bool checkWithOrder()
{
	for (int i = 0; i < n; i++)
		used[i] = false;

	for (int i = 0; i < n; i++)
	{
		int cc = 0;
		int id = order[i];
		for (int j = 0; j < n; j++)
			if (can[id][j] && !used[j])
				sel[cc++] = j;

		if (cc == 0)
			return false;

		int num = rand() % cc;
		used[sel[num]] = true;
	}

	return true;
}

bool check()
{
	for (int i = 0; i < n; i++)
		order[i] = i;

	do
	{
		for (int i = 0; i < 1500; i++)
			if (!checkWithOrder())
				return false;
	} while (next_permutation(order, order + n));

	return true;
}

void solve()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", s);
		for (int j = 0; j < n; j++)
			can[i][j] = s[j] == '1';
	}

	vector<pair<int, int>> pos;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (can[i][j] == 0)
			{
				pos.pb(mp(i, j));
			}

	memcpy(can2, can, sizeof(can));

	int maskMax = 1 << pos.size();
	int ans = INF;
	for (int i = 0; i < maskMax; i++)	
	{
		memcpy(can, can2, sizeof(can));

		int x = i;
		int j = 0;
		int cost = 0;
		while (x)
		{
			if (x & 1)
			{
				can[pos[j].first][pos[j].second] = true;
				cost++;
			}

			j++;
			x >>= 1;
		}

		if (check())
		{
			ans = min(ans, cost);
		}
	}

	printf("%d", ans);

	printf("\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tn;
	scanf("%d", &tn);
	for (int i = 0; i < tn; i++)
	{
		cerr << "test #" << i + 1 << endl;
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
