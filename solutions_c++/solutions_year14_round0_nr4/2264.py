#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <bitset>
using namespace std;

#define INF 987654321
#define LL long long
#define ULL unsigned long long
#define For(i, n) for(int i = 0; i < n; ++i)


vector<double> va;
vector<double> vb;
int n;
int process(vector<double> a, vector<double> b)
{
	vector<double> ta;
	ta.assign(a.begin(), a.end());
	sort(ta.begin(), ta.end());
	vector<double> tb;
	tb.assign(b.begin(), b.end());
	sort(tb.begin(), tb.end(), greater<double>());

	int awin = 0;
	for (int i = 0; i < n; ++i)
	{
		vector<double>::iterator it = lower_bound(ta.begin(), ta.end(), tb[i]);
		if (it != ta.end())
		{
			ta.erase(it); awin++;
		}
		else
		{
			ta.erase(ta.begin());
		}
	}
	return awin;
}

int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int k = 1; k <= t; ++k)
	{
		scanf("%d", &n);
		va.resize(n); vb.resize(n);
		for (int i = 0; i < n; ++i) scanf("%lf", &va[i]);
		for (int i = 0; i < n; ++i) scanf("%lf", &vb[i]);
		printf("Case #%d: ", k);
		int a = process(va, vb);
		int b = process(vb, va);
		printf("%d %d", a, n - b);
		printf("\n");
	}
	return 0;
} 