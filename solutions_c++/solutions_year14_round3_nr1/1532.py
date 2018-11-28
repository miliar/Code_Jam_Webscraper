#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cmath>
#include <fstream>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <cstring>
#include <queue>
#include <deque>
#include <stack>
#include <climits>
using namespace std;

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)
#define REP1(i, n) for (int (i) = 1; (i) <= (n); (i) ++)
#define FOR(i,a,b) for (int (i) = (a); (i) < (b); ++(i)) 
#define wait system("pause")


const int NMAX = 40;
ll plog[NMAX + 1];
void pre()
{
	plog[0] = 1; 
	FOR(i, 1, NMAX + 1) 
		plog[i] = plog[i - 1] * 2;
}

int blog(ll inn)
{
	ll n = 0, N = inn;
	while (N / 2 > 0)
	{
		N /= 2; ++n;
	}
	return n;
	
}

int solve()
{
	ll P, Q;
	char c;
	cin >> P >>c>> Q;

	ll p = P, q = Q, d = 1;
	while (!(q % 2)) q /= 2;
	d = q, q = Q;
	if (p%d)
		return -1;
	else
		p /= d, q /= d;
	return blog(q) - blog(p);

}

int main()
{
	//ifstream in("A-small-attempt3.in");
	//ofstream out("A.out");
	freopen("A-large(1).in", "r", stdin);
	freopen("a.out", "w", stdout);
	pre();
	int II;
	int T;
	cin >> T;
	REP1(II, T)
	{
		cout << "Case #" << II << ": ";
		int ans = solve();
		if (ans == -1)
			printf("impossible\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}