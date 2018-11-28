#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <sstream>
#include <functional>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>

using namespace std;

vector<int> bigMult(const vector<int> &a, const vector<int> &b)
{
	vector<int> res(a.size() + b.size(), 0);		
	for(int i = 0; i < a.size(); i++)
	{
		int c = 0;
		for(int j = 0; j < b.size(); j++)
		{
			c += res[i + j] + a[i] * b[j];
			res[i + j] = c % 10;
			c /= 10;
		}
		res[i + b.size()] = c;
	}

	while(!res.back()) res.pop_back();

	return res;
}

bool palin(const vector<int> &a)
{
	for(int i = 0; i < a.size(); i++) if (a[i] != a[a.size() - i - 1]) return false;
	return true;
}

vector<int> toBig(int x)
{
	vector<int> res;
	while(x)
	{
		res.push_back(x % 10);
		x /= 10;
	}
	return res;
}

vector<int> toBig(char *x)
{
	int n = strlen(x);
	vector<int> res(n, 0);
	for(int i = 0; i < n; i++) res[i] = x[n - i - 1] - '0';
	while(!res.back()) res.pop_back();
	return res;
}

bool bigLess(const vector<int> &a, const vector<int> &b)
{
	if (a.size() != b.size()) return a.size() < b.size();
	int n = a.size();
	for(int i = 0; i < n; i++)
		if (a[n - i - 1] != b[n - i - 1])
			return a[n - i - 1] < b[n - i - 1];
	return false;
}

int nt;

int n;
vector<int> a[100000];

vector<int> x;

void test()
{
	vector<int> sq = bigMult(x, x);
	if (palin(sq))
	{
		a[n++] = sq;
		//printf("a[%d] = ", n - 1);
		//for(int i = sq.size(); i--;) printf("%d", sq[i]);
		//puts("");
	}
}

void go(int len, int index, int used)
{
	int index_r = len - index - 1;
	if (index == index_r)
	{
		// odd case
		for(int d = 0; d <= 3; d++)
		if (used + d * d < 10)
		{
			x[index] = d;
			if (used + d * d) test();
		}
		return;
	}

	if (index > index_r)
	{
		if (used) test();
		return;
	}

	for(int d = 0; d < 3; d++)
	if (used + d * d * 2 < 10)
	{
		x[index] = x[index_r] = d;
		go(len, index + 1, used + d * d * 2);
	}
}

char sA[1000], sB[1000];
vector<int> A, B;

int main()
{
	for(int len = 1; len <= 50; len++)
	{
		x.assign(len, 0);
		fprintf(stderr, "len = %d\n", len);
		go(len, 0, 0);
	}

	int nt;
	scanf("%d", &nt);
	for(int tt = 1; tt <= nt; tt++)
	{
		fprintf(stderr, "test = %d\n", tt);
		printf("Case #%d: ", tt);
		
		scanf("%s %s", sA, sB);
		A = toBig(sA);
		B = toBig(sB);

		if (bigLess(B, A)) swap(A, B);

		int res = upper_bound(a, a + n, B, bigLess) - lower_bound(a, a + n, A, bigLess);

		printf("%d\n", res);
	}
	return 0;
}