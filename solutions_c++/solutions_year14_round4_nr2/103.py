#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <map>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

int a[1001], origin[1001], n, bestK;

int solveA(void)
{
	scanf("%d", &n);
	FOR(i, n) scanf("%d", a + i);
	memcpy(origin, a, sizeof(origin));
	int best = 999666111;
	// [0..k) + [k..n)
	for (int k = 0; k <= n; k++) {
		int left = 0, right = 0;
		for (int i = 0; i < k; i++)
			for (int j = i + 1; j < k; j++) if (a[i] > a[j]) left++;
		
		for (int i = k; i < n; i++)
			for (int j = i; j < n; j++)
				if (a[i] < a[j]) right++;
		int temp = left + right;
		if (temp < best) {
			best = temp;
			bestK = k;
		}
	}
	return best;
}

int minSteps;
int bestL, bestR;
vector<int> bestV;

void bt(vector<int> v, int L, int R, int steps)
{
	int idx = L + R;
	if (idx == n) {
		//minSteps = min(minSteps, steps);
		if (steps < minSteps) {
			bestL = L;
			bestR = R;
			bestV = v;
			minSteps = steps;
		}
		return;
	}
	int next = a[idx];
	int inext;
	for (int i = L; i < n - R; i++) if (v[i] == next) { inext = i; break; }
	// try left:
	vector<int> temp = v;
	int lSteps = 0;
	int i = inext;
	while (i > L) {
		swap(v[i], v[i - 1]);
		i--;
		lSteps++;
	}
	bt(v, L + 1, R, steps + lSteps);
	
	// try right:
	v = temp;
	int rSteps = 0;
	i = inext;
	while (i < n - R - 1) {
		swap(v[i], v[i + 1]);
		i++;
		rSteps++;
	}
	bt(v, L, R + 1, steps + rSteps);
}

int solveB()
{
//	scanf("%d", &n);
//	FOR(i, n) scanf("%d", a + i);
	vector<int> v;
	FOR(i, n ) v.push_back(a[i]);
	sort(a, a + n);
	minSteps = 999666111;
	bt(v, 0, 0, 0);
	return minSteps;
}

vector<pair<int, int> > tags;
int dp[1001][1001];
int NSMAP[1001][3];

int numSwaps(int value, int from, int dir)
{
	int& comp = NSMAP[from][dir + 1];
	if (comp != -1) return comp;
	int c = 0;
	for (int i = from + dir; i >= 0 && i < n; i += dir) {
		if (a[i] > value) c++;
	}
	comp = c;
	return c;
}

int f(int L, int R)
{
	if (L + R == n) return 0;
	int& d = dp[L][R];
	if (d != -1) return d;
	// try left:
	int idx = L + R;
	int pos = tags[idx].second;
	d = numSwaps(a[pos], pos, -1) + f(L + 1, R);
	// try right:
	d = min(d, numSwaps(a[pos], pos, +1) + f(L, R + 1));
	return d;
}

int solveC(void)
{
	memset(NSMAP, 0xff, sizeof(NSMAP));
	memcpy(a, origin, sizeof(a));
	tags.clear();
	FOR(i, n) tags.push_back(make_pair(a[i], i));
	sort(tags.begin(), tags.end());
	memset(dp, 0xff, sizeof(dp));
	return f(0, 0);
}

int solve(void)
{
/*
	int a = solveA();
	int b = solveB();
	int c = solveC();
	if (b != c) {
		printf("Mismatch. AlgoB said %d, C said %d\n", b, c);
	//	printf("Algo A: k = %d\n", bestK);
		printf("Algo B: L = %d, R = %d, v = { ", bestL, bestR);
		REP(i, bestV) {
			if (i) printf(", ");
			printf("%d", bestV[i]);
		}
		printf("}\n");
	}
	
	return b;
	*/
	scanf("%d", &n);
	FOR(i, n) scanf("%d", &a[i]);
	memcpy(origin, a, sizeof(origin));
	return solveC();
}

int main(void)
{
//	freopen("/home/vesko/gcj/b.in", "rt", stdin);
	int nTests;
	scanf("%d", &nTests);
	FOR(tc, nTests) {
		printf("Case #%d: %d\n", tc + 1, solve());
	}
	return 0;
}

