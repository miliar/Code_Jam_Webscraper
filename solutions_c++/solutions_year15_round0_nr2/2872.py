#include <iostream>
#include <algorithm>

using namespace std;

const int MAX = 1000 + 10;	

int a[MAX];

int main()
{
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int test = 0; test < T; test++)
	{
		int n;
		cin >> n;
		for(int i=0; i<n; i++)
			cin >> a[i];
		int ans = 10000;
		int ma = *max_element(a, a+n);
		for(int m = ma; m > 0; m--)
		{
			int cur = m;
			for (int i=0; i<n; i++)
				cur += (a[i] + m - 1) / m - 1;
			ans = min(ans, cur);
		}
		cout << "Case #" << test + 1 << ": " << ans << endl;
	}
}
