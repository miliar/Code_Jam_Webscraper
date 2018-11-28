#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

const int Maxn = 4;
const int Inf = 1000000000;

int t;
int n;
char B[Maxn][Maxn];
int res;
vector <int> seq;
bool tk[Maxn];

bool Check2(int lvl)
{
	if (lvl >= n) return true;
	int got = 0;
	for (int i = 0; i < n; i++)
		if (B[seq[lvl]][i] == '1' && !tk[i]) {
			got++;
			tk[i] = true;
			if (!Check2(lvl + 1)) return false;
			tk[i] = false;
		}
	return got > 0;
}

bool Check()
{
	seq.clear();
	for (int i = 0; i < n; i++)
		seq.push_back(i);
	do {
		fill(tk, tk + n, false);
		if (!Check2(0)) return false;
	} while (next_permutation(seq.begin(), seq.end()));
	return true;
}

void Gen(int r, int c, int cost)
{
	if (r >= n) {
		if (Check()) res = min(res, cost);
	} else if (c >= n) Gen(r + 1, 0, cost);
	else {
		Gen(r, c + 1, cost);
		if (B[r][c] == '0') {
			B[r][c] = '1';
			Gen(r, c + 1, cost + 1);
			B[r][c] = '0';
		}
	}
}

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				scanf(" %c", &B[i][j]);
		res = Inf;
		Gen(0, 0, 0);
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}