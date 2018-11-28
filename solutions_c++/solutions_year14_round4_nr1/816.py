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
#include <fstream>

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

const int maxn = 100000;
int a[maxn];

int main(int argc, char *argv[])
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int t;
	cin >> t;
	
	for (int tt = 1; tt <= t; tt++)
	{
		int n, x;
		cin >> n >> x;
		
		for (int i = 0; i < n; i++)
			scanf("%d", a + i);
			
		sort(a, a + n);
		
		int ans = 0;
		
		int l = 0, r = n - 1;
		
		while (l <= r)
		{
			if (l == r)
			{
				ans++;
				break;
			}
			
			if (a[l] + a[r] <= x)
			{
				ans++;
				l++;
				r--;
			}
			else
			{
				ans++;
				r--;
			}
		}
		
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}











