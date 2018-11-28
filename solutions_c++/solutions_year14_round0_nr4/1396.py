#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int main()
{
	freopen("D-large.in.txt","r",stdin);
	freopen("D-large.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1 ; tt <= T ; tt++)
	{
		int n, ans1 = 0, ans2 = 0;
		cin >> n;
		double a1[1000], a2[1000];
		for (int i = 0 ; i < n ; i++)
			cin >> a1[i];
		for (int i = 0 ; i < n ; i++)
			cin >> a2[i];
		sort(a1, a1 + n);
		sort(a2, a2 + n);
		// cheat
		int l1 = 0, r1 = n-1, l2 = 0, r2 = n-1;
		while (l1 <= r1)
		{
			if (a1[r1] > a2[r2])
			{
				r1 --;
				r2 --;
				ans1 ++;
			}
			else
			{
				l1 ++;
				r2 --;
			}
		}

		// not cheat
		l1 = l2 = 0;
		while (l1 < n && l2 < n)
		{
			if (a1[l1] < a2[l2])
			{
				l1 ++;
				l2 ++;
				ans2 ++;
			}
			else
			{
				while (l2 < n && a2[l2] < a1[l1]) l2 ++;
				if (l2 == n) break;
				ans2 ++;
				l1 ++;
				l2 ++;
			}
		}
		ans2 = n - ans2;
		cout << "Case #" << tt << ": " << ans1 << " " << ans2 << endl;
	}
}