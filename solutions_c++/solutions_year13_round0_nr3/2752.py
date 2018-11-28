#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <iostream>
#include <climits>
using namespace std;

typedef long long ll;
typedef long double ld;

int t;
ll a, b, ans;

bool pali(ll num)
{
	int array[20];
	int c = 0;
	while (num)
	{
		array[c++] = num%10;
		num /= 10;
	}
	for (int i = 0; i < c/2; i++)
		if (array[i] != array[c-i-1])
			return false;
	return true;
}

int main()
{
	int i;
	ll l, r, j;
//	freopen("C-small-attempt0.in", "r", stdin);
//	freopen("out", "w", stdout);
	cin >> t;
	for (i = 0; i < t; i++)
	{
		ans = 0;
		cin >> a >> b;
		l = sqrt(a);
		r = sqrt(b);
		if (l*l < a)
			l++;
		for (j = l; j <= r; j++)
		{
			if (pali(j) && pali(j*j))
				ans++;
		}
		cout << "Case #" << i+1<< ": " << ans << endl;
	}
	return 0;
}
