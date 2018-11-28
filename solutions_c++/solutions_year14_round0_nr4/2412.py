#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <ctype.h>
#include <cassert>
#include <stack>

using namespace std;


#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left

template < typename T > T abs(T x)
{
	return x > 0 ? x : -x;
}

const int maxn = 10005;

ll a[maxn], b[maxn];
set < ll > bs;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int tt;
	cin >> tt;
	for (int t = 0; t < tt; t++)
	{
		int n;
		cin >> n;
		
		for (int i = 0; i < n; i++)
		{
			ld x;
			cin >> x;
			a[i] = x * 10000000;
		}
		
		for (int i = 0; i < n; i++)
		{
			ld x;
			cin >> x;
			b[i] = x * 10000000;
			bs.insert(b[i]);
		}
		
		sort(a, a + n);
		sort(b, b + n);
		
		int warS = 0;
		
		for (int i = 0; i < n; i++)
		{
			if (bs.upper_bound(a[i]) == bs.end())
			{
				warS++;
				bs.erase(bs.begin());
			}
			else
			{
				bs.erase(bs.upper_bound(a[i]));
			}
		}
		
		int dWarS = 0;
		
		int p = 0;
		for (int i = 0; i < n; i++)
		{
			if (a[i] > b[p])
			{
				dWarS++;
				p++;
			}
		}
		
		cout << "Case #" << t + 1 << ": ";
		cout << dWarS << " " << warS << endl;
	}
	
	return 0;
}







