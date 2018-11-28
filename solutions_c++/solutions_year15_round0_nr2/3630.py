#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

vector < int > a;
int T, n, x;

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	cin >> T;
	
	for (int t = 0; t < T; t++) {
		cin >> n;
		int max = 0;
		a.clear();
		for (int i = 0; i < n; i++) {
			cin >> x;
			a.push_back(x);
			if (x > max)
				max = x;
		}
		
		int l = 0, r = 1000;
		
		while (l + 1 < r) {
			int m = (l + r) / 2;
			int s = max;
			for (int i = 0; i < m; i++) {
				int ts = 0;
				int dec_many = m - i;
				for (int j = 0; j < n; j++) {
					ts += (a[j] - 1) / dec_many;
				}
				if (ts + dec_many < s)
					s = ts + dec_many;
			}
			if (s <= m)
				r = m;
			else
				l = m;
		}
		
		printf("Case #%d: %d\n", t + 1, r);
	}
}
