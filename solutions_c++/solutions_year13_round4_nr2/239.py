#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
using namespace std;

long long alwaysWin(int n, long long p)
{
	long long total = 1LL << n;
	int lose = 0;
	while (total > 1)
	{
		if (p <= total / 2) break;
		lose++;
		total /= 2;
		p -= total;
	}
	return min((1LL << (lose + 1)) - 2, (1LL << n) - 1);
}

long long mayWin(int n, long long p)
{
	long long total = 1 << n;
	int best[2000];
	vector <int> a;
	for (int i = 0; i < 1 << n; i++) a.push_back(i), best[i] = (1 << n);
	for (int i = 0; i < n; i++)
	{
		vector <int> b;
		for (int i = 0; i < int(a.size()); i += 2) b.push_back(a[i]);
		total /= 2;
		a = b;
		best[b.back()] = a.size();
	}
	
	for (int i = (1 << n) - 1; i >= 0; i--)
		if (best[i] <= p) return i;
}

long long mayWin2(int n, long long p)
{
	long long total = 1LL << n, last = total - 1, step = 1;
	if (p == total) return total - 1;
	for (int i = 0; i < n; i++)
	{
		last -= step;
		total /= 2;
		step *= 2;
		if (total <= p) return last;
	}
	return 0;
}

int main()
{
	freopen("blarge.in", "r", stdin); 
	freopen("blarge.out", "w", stdout);
	int test, n;
	long long p;
	cin >> test;
	for (int itest = 1; itest <= test; itest++)
	{
		cin >> n >> p;
		printf("Case #%d: ", itest);
		cout << alwaysWin(n, p) << ' ' << mayWin2(n, p) << endl;
	}
}
