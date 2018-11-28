#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 1010;

int n, a[MAXN];


int Work()
{
	cin >> n;
	for (int i = 0; i < n; i ++)
		cin >> a[i];
	int ret = 0, ll = 0, rr = n - 1;
	
	while (ll < rr)
	{
		int mn = ll;
		for (int i = ll; i <= rr; i ++)
			if (a[i] < a[mn])  mn = i;
		if (abs(mn - ll) < abs(mn - rr))
		{
			ret += abs(mn - ll);
			while (mn > ll)
			{
				swap(a[mn], a[mn-1]);
				mn --;
			}
			ll ++;
		} else 
		{
			ret += abs(mn - rr);
			while (mn < rr)
			{
				swap(a[mn], a[mn+1]);
				mn ++;
			}
			rr --;
		}
	}

	return ret;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin.sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt ++)
		cout << "Case #" << tt << ": " << Work() << endl;
	return 0;
}