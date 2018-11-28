#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
#define mp make_pair

const int N = 27;
int n;
char s[N];
int a[N][2];
int b[N][2];
int m;
int ans;
int addToAns;

int sqr(int x)
{
	return x * x;
}
int sgn(int x)
{
	if (x > 0) return 1;
	if (x == 0) return 0;
	return -1;
}

struct State
{
	int A, B;
	vector<pii> w;

	State() : A(), B(), w() {}

	bool operator < (const State &S) const
	{
		if (A != S.A) return A < S.A;
		if (B != S.B) return B < S.B;
		return w < S.w;
	}

	int getMinScore()
	{
		int res = max(A, B);
		for (pii t : w)
			res += sqr(min(t.first, t.second));
		return res;
	}
};

set<State> used;

void brute(State S, int curAns)
{
	if (curAns + S.getMinScore() >= ans) return;
	if (used.count(S) > 0) return;
	used.insert(S);
	if (S.w.empty())
	{
		ans = curAns + S.getMinScore();
		return;
	}
	pii t = S.w.back();
	State nS = S;
	nS.w.pop_back();
	if (t.first < t.second && S.A >= t.second - t.first)
	{
		nS.A -= t.second - t.first;
		brute(nS, curAns + sqr(t.second));
		nS.A += t.second - t.first;
	}
	if (t.second < t.first && S.B >= t.first - t.second)
	{
		nS.B += t.second - t.first;
		brute(nS, curAns + sqr(t.first));
		nS.B -= t.second - t.first;
	}
	for (int i = 0; i < (int)S.w.size() - 1; i++)
	{
		if (sgn(t.first - t.second) == sgn(S.w[i].first - S.w[i].second)) continue;
		pii nt = mp(t.first + S.w[i].first, t.second + S.w[i].second);
		nS.w.clear();
		for (int j = 0; j < (int)S.w.size() - 1; j++)
			if (j != i)
				nS.w.push_back(S.w[i]);
		if (nt.first == nt.second)
		{
			brute(nS, curAns + sqr(nt.first));
		}
		else
		{
			nS.w.push_back(nt);
			brute(nS, curAns);
		}
	}
	return;
}

int solve()
{
	scanf("%d", &n);
	addToAns = 0;
	ans = n * n;
	m = 0;
	for (int i = 0; i < n; i++)
	{
		scanf(" %s ", s);
		int mask = 0;
		for (int j = 0; j < n; j++)
			if (s[j] == '1')
			{
				mask |= 1 << j;
				addToAns--;
			}
		int sz = 0;
		int cnt = 1;
		for (int j = 0; j < m; j++)
		{
			if ((mask & a[j][0]) == 0)
			{
				b[sz][0] = a[j][0];
				b[sz][1] = a[j][1];
				sz++;
				continue;
			}
			cnt += a[j][1];
			mask |= a[j][0];
		}
		b[sz][0] = mask;
		b[sz][1] = cnt;
		sz++;
		m = sz;
		for (int j = 0; j < m; j++)
			for (int k = 0; k < 2; k++)
				a[j][k] = b[j][k];
	}

	int allMask = 0;
	for (int i = 0; i < m; i++)
		allMask |= a[i][0];
	State S = State();
	int curAns = 0;
	for (int i = 0; i < m; i++)
	{
		if (a[i][0] == 0)
			S.A++;
		else
		{
			int pc = 0;
			for (int j = 0; j < n; j++)
				if ((a[i][0] >> j) & 1)
					pc++;
			if (a[i][1] != pc)
				S.w.push_back(mp(a[i][1], pc));
			else
				curAns += sqr(pc);
		}
	}
	for (int i = 0; i < n; i++)
		if (((allMask >> i) & 1) == 0)
			S.B++;
	sort(S.w.begin(), S.w.end());

	used.clear();
	brute(S, curAns);
	return ans + addToAns;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
		printf("Case #%d: %d\n", i, solve());

	return 0;
}