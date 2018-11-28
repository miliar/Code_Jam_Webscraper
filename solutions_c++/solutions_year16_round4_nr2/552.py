#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <memory.h>
#include <ctime>

using namespace std;

#pragma comment(linker, "/STACK:128000000")

typedef pair<int, int> pii;
typedef long long int64;
typedef pair<int64, int64> pii64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<int,pii> piii;
typedef pair<int64,pii> piii64;
typedef pair<pii,pii> piiii;

#define y1 dsjfksdj_fks
#define y2 alksaad_sa
#define y0 _sdkfsjfs__

#define tm _dskfjskdfjksdf

int nt;
int n, k;
vector<double> p;

inline void init()
{
	p.clear();
	cin >> n >> k;
	p.resize(n);
	for (int i = 0; i < n; ++i)
		cin >> p[i];
	sort(p.begin(), p.end());
}

inline int bitcount(int x)
{
	int res = 0;
	while (x)
	{
		x &= (x - 1);
		++res;
	}
	return res;
}

inline double triv_prob(int mask)
{
	vector<double> tp(k + 1, 0.0);
	tp[0] = 1.0;
	for (int i = 0; i < n; ++i)
	{
		if (!(mask & (1 << i))) continue;
		vector<double> ntp(k + 1, 0.0);
		for (int j = k - 1; j >= 0; --j)
		{
			ntp[j + 1] += tp[j] * p[i];
			ntp[j] += tp[j] * (1.0 - p[i]);
		}
		tp = ntp;
	}
	return tp[k >> 1];
}

inline double trivial_sol()
{
	int bmask = 0;
	double res = -1.0;
	for (int mask = 0; mask < (1 << n); ++mask)
	{
		if (bitcount(mask) != k) continue;
		double cur = triv_prob(mask);
		if (cur > res)
		{
			res = cur;
			bmask = mask;
		}
	}
	/*
	cout.precision(2);
	for (int i = 0; i < n; ++i)
	{
		if (!(bmask & (1 << i))) continue;
		cout << p[i] << " ";
	}
	cout << endl;
	*/
	return res;
}

inline double fast_sol(vector<int> &ind)
{
	vector<double> tp(k + 1, 0.0);
	tp[0] = 1.0;
	for (int t = 0; t < k; ++t)
	{
		int i = ind[t];
		vector<double> ntp(k + 1, 0.0);
		for (int j = k - 1; j >= 0; --j)
		{
			ntp[j + 1] += tp[j] * p[i];
			ntp[j] += tp[j] * (1.0 - p[i]);
		}
		tp = ntp;
	}
	return tp[k >> 1];
}

inline double fast_sol2()
{
	double res = 0.0;
	vector<int> ind;
	for (int i = 0; i < n; ++i)
	{
		ind.clear();
		for (int j = 0; j < k; ++j)
		{
			ind.push_back((i + j) % n);
		}
		res = max(res, fast_sol(ind));
	}
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	cout.precision(15);
	cin >> nt;
	for (int tn = 1; tn <= nt; ++tn)
	{
		cerr << tn << endl;
		init();
		//double res = trivial_sol();
		double res2 = fast_sol2();
		cout << fixed << "Case #" << tn << ": " << res2 << endl;
	}

    return 0;
}