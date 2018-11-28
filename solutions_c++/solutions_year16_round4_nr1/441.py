#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define in_str(b) scanf("%s",(b))
#define in_int1(a) scanf("%d",&(a))
#define in_int2(a,b) scanf("%d%d",&(a),&(b))
#define in_int3(a,b,c) scanf("%d%d%d",&(a),&(b),&(c))
#define in_int4(a,b,c,d) scanf("%d%d%d%d",&(a),&(b),&(c),&(d))
#define so(a) sort((a).begin(), (a).end())
#define rso(a) sort((a).rbegin(), (a).rend())
#define mp(a,b) make_pair(a,b)
#define mset(a,n) memset(a,n,sizeof(a))
#define readints(mas,n) for (int _i=0;_i<(n);_i++) in_int1((mas)[_i])
#define readdoubles(mas,n) for (int _i=0;_i<(n);_i++) scanf("%lf", &(mas)[_i])
#define unq(src) src.erase(unique((src).begin(), (src).end()), (src).end())
#define MOD 1000000007
typedef pair<int, int> pii;
typedef long long ll;
typedef pair<ll, ll> pll;

int r, p, s;

int test1(int R, int P, int S, int n)
{
	if (n == 0) return R == r && P == p && S == s;
	return test1(P + R, P + S, R + S, n - 1);
}

string build(int R, int P, int S, int n)
{
	string ans = R == 1 ? "R" : (P == 1 ? "P" : "S");
	int i;
	for (i = 0; i < n; i++)
	{
		string t;
		for (int j = 0; j < ans.size(); j++)
		{
			if (ans[j] == 'P') t += "PR";
			else if (ans[j] == 'R') t += "RS";
			else t += "PS";
		}
		ans = t;
	}

	vector<string> o;
	for (i = 0; i < ans.size(); i++)
	{
		o.push_back(string(1,ans[i]));
	}

	while (o.size() != 1)
	{
		vector<string> t;
		for (i = 0; i < o.size(); i += 2)
		{
			if (o[i] > o[i + 1]) t.push_back(o[i + 1] + o[i]);
			else t.push_back(o[i] + o[i + 1]);
		}
		o = t;
	}

	return o[0];
}

void Solve()
{
	int i, j, k, n, m;

	int tests;
	in_int1(tests);
	for (int test = 1; test <= tests;test++)
	{
		in_int4(n, r, p, s);
		string ans = "IMPOSSIBLE";
		if (test1(1, 0, 0, n)) ans = build(1, 0, 0, n);
		else if (test1(0, 1, 0, n)) ans = build(0, 1, 0, n);
		else if (test1(0, 0, 1, n)) ans = build(0, 0, 1, n);
		printf("Case #%d: %s", test, ans.c_str());
		printf("\n");
	}
}

int main()
{
#ifdef __LOCAL_RUN__
	FILE *res_output = freopen("output.txt", "wt", stdout);
	FILE *res_input = freopen("input.txt", "rt", stdin);
	Solve();
#else
	Solve();
#endif
	return 0;
}