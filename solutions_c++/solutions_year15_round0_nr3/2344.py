#include <iostream>
#include <fstream>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <queue>
#include <deque>
#include <list>

using namespace std;

#define pb push_back
#define fs first
#define sc second
#define sz(a) (int)a.size()
#define szs(s) (int)s.length() 
#define elif else if
#define mp make_pair

typedef long long ll;
typedef long double ld;

const int INF = 1000000009;
const ll INFL = 1759849216489136867ll;
const double eps = 1e-9;

#define NAME ""

void solve();

int main()
{
	clock_t t_start, t_end;
	
	#ifdef _GEANY
	assert(freopen("input.txt", "r", stdin));
	t_start = clock();
	#endif
	
	int t(0);
	cin >> t;
	
	for (int i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	
	#ifdef _GEANY
	t_end = clock();
	cerr.precision(3);
	cerr << fixed << (double)(t_end - t_start) / CLOCKS_PER_SEC << '\n';
	#endif
	
	return 0;
}

struct Quaternion
{
	int num;
	
	Quaternion ()
	: num(0)
	{
	}
	
	Quaternion(const int &num)
	: num(num)
	{
	} 
	
	Quaternion operator * (const Quaternion &q)
	{
		//~ cerr << num << '*' << q.num << '\n';
		assert(num);
		
		int c = 1, cq = 1;
		
		if (num < 0)
			c = -1;
		if (q.num < 0)
			cq = -1;
		
		switch (q.num * cq)
		{
			case 1:
				return Quaternion(num * cq);
				break;
			case 2:
				if (num * c == 1)
					return Quaternion(cq * 2 * c);
				if (num * c == 2)
					return Quaternion(cq * -1 * c);
				if (num * c == 3)
					return Quaternion(cq * -4 * c);
				if (num * c == 4)
					return Quaternion(cq * 3 * c);
				break;
			case 3:
				if (num * c == 1)
					return Quaternion(cq * 3 * c);
				if (num * c == 2)
					return Quaternion(cq * 4 * c);
				if (num * c == 3)
					return Quaternion(cq * -1 * c);
				if (num * c == 4)
					return Quaternion(cq * -2 * c);
				break;
			case 4:
				if (num * c == 1)
					return Quaternion(cq * 4 * c);
				if (num * c == 2)
					return Quaternion(cq * -3 * c);
				if (num * c == 3)
					return Quaternion(cq * 2 * c);
				if (num * c == 4)
					return Quaternion(cq * -1 * c);
				break;
		}
		
		//~ cerr << num << '*' << q.num << '\n';
		
		assert(0);
		return Quaternion(0);
	}
	
	bool operator == (const Quaternion &q)
	{
		return num == q.num;
	}
};

Quaternion a[10001];
Quaternion mul[100010];

void solve()
{
	ll l, x;
	cin >> l >> x;
	
	Quaternion all(1);
	
	string s;
	cin >> s;
	
	for (int i = 0; i < l; ++i)
	{
		char c(s[i]);
		
		switch (c)
		{
			case 'i':
				a[i] = Quaternion(2);
				break;
			case 'j':
				a[i] = Quaternion(3);
				break;
			case 'k':
				a[i] = Quaternion(4);
				break;
			default:
				cerr << l << x << i << ' ' << c << '\n';
				assert(0);
				break;
		}
		
		all = all * a[i];
		//~ cerr << a[i].num << ' ';
	}
	
	//~ cerr << '\n';
	
	Quaternion pows[4];
	pows[0] = Quaternion(1);
	
	for (int i = 1; i < 4; ++i)
		pows[i] = pows[i - 1] * all;
	
	if (!(pows[x & 3] == Quaternion(-1)))
	{
		cout << "NO\n";
		return;
	}
	
	if (x > 8)
		x = 8;
	
	mul[0] = a[0];
	
	for (int i = 0; i < x; ++i)
	{
		for (int j = 0; j < l; ++j)
		{
			if (i == 0 && j == 0)
				continue;
			mul[i * l + j] = mul[i * l + j - 1] * a[j];
		}
	}
	
	bool is_i(0);
	
	for (int i = 0; i < l * x; ++i)
	{
		//~ cerr << mul[i].num << ' ';
		if (is_i && mul[i] == Quaternion(4))
		{
			cout << "YES\n";
			return;
		}
			
		if (mul[i] == Quaternion(2))
			is_i = 1;
	}
	
	//~ cerr << '\n';
	
	cout << "NO\n";
}
