#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <algorithm>
#include <cstdio>
#include <ctime>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <cassert>
#include <iostream>
#include <cmath>
#include <sstream>
#include <complex>
#include <memory.h>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

typedef long long int64;
typedef unsigned long long uint64;

#define y1 _dsfkjdsfksdj
#define y0 _sfsdkfdop

typedef unsigned uint;
typedef vector<int64> vi64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef pair<int,string> pis;
typedef pair<int64,int64> pii64;
typedef pair<pii,int> piii;
typedef pair<pii,pii> piiii;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<double,int> pdi;
typedef pair<double,double> pdd;

int nt;
int n;
int64 B;
int64 a[40];

inline void init()
{
	cin >> B >> n;
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	while (n < 37) a[n++] = 0;
	sort(a, a + n);
}

/*
inline double slow_solve()
{
	double res = 0.0;
	for (int val = 1; val <= 1001; ++val)
	{
		int need = 0;
		int cnt = 0;
		int own = 0;
		vi b;
		b.clear();
		for (int i = 0; i < n; ++i)
		{
			if (a[i] > val) break;
			need += (val - a[i]);
			b.push_back(val - a[i]);
			++cnt;
			if (a[i] < val) ++own;
		}
		if (need > B) continue;
		if (!cnt) continue;
		if (!own) continue;
		sort(b.begin(), b.end());
		reverse(b.begin(), b.end());
		int add = 0;
		int tneed = need;
		for (int t = 0; t < cnt; ++t)
		{
			int town = own;
			if (t + own > cnt) town -= (t + own - cnt);
			int tcnt = cnt - t;
			double extra = B - tneed - add;
			double cur = extra + ((double)town / (double)tcnt) * 36.0 * ((double)need / (double)town) - B;
			if (val == 53) cout << cur << endl;			
			//cerr << val << " " << t << " " << tcnt << " " << town << " " << cur << endl;			
			if (res < cur)
			{
				res = cur;
				bval = val;
			}
			++add;
			need -= b.back();
			b.pop_back();
			if (tneed + add > B) break;
		}
	}
	return res;
}
*/

double F(int64 val)
{
	double res = 0.0;
	int64 need = 0;
	int cnt = 0;
	int own = 0;
	vector <int64> b;
	b.clear();
	for (int i = 0; i < n; ++i)
	{
		if (a[i] > val) break;
		need += (val - a[i]);
		b.push_back(val - a[i]);
		++cnt;
		if (a[i] < val) ++own;
	}
	if (need > B) return -1.0;
	if (!cnt) return -1.0;
	if (!own) return -1.0;
	sort(b.begin(), b.end());
	reverse(b.begin(), b.end());
	int64 add = 0;
	int64 tneed = need;
	for (int t = 0; t < cnt; ++t)
	{
		int town = own;
		if (t + own > cnt) town -= (t + own - cnt);
		int tcnt = cnt - t;
		double extra = (double)(B - tneed - add);
		double cur = extra + ((double)town / (double)tcnt) * 36.0 * ((double)need / (double)town) - B;		
		//cerr << val << " " << t << " " << tcnt << " " << town << " " << cur << endl;			
		if (res < cur)
		{
			res = cur;
		}
		++add;
		need -= b.back();
		b.pop_back();
		if (tneed + add > B) break;
	}
	return res;
}

inline double fast_solve()
{
	int64 l = max(a[0], 1LL), r = 1000000000001LL;
	while (l + 10 < r)
	{
		int64 m1 = l + (r - l) / 3;
		int64 m2 = l + 2 * (r - l) / 3;
		//cout << l << " " << r << " " << m1 << " " << m2 << endl;
		double f1 = F(m1);
		double f2 = F(m2);
		//cout << f1 << " " << f2 << endl;		
		if (f1 < -0.5 && f2 < -0.5)
		{
			r = m2;
			continue;
		}
		if (f1 > f2)
		{
			r = m2;
		} else {
			l = m1;
		}
	}
	double res = max(0.0, F(l));
	for (int64 i = l + 1; i <= r; ++i)
		res = max(res, F(i));
	return res;
}

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	cin >> nt;
	for (int tn = 1; tn <= nt; ++tn)
	{
		cerr << tn << endl;
		init();
		double res = fast_solve();
		cout.precision(15);
		cout << "Case #" << tn << ": "; 
		cout << fixed << res << endl;
		if (0)
		{
			for (int i = n - 1; i >= 0; --i)
				cout << a[i] << " ";
			cout << endl;
		}
		//cout << fixed << slow_solve() << endl;
	}

    return 0;
}