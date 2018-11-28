//be naame khodaa

#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cassert>
#include <iomanip>
#include <cstring>
typedef long long ll;

using namespace std;
typedef pair <int, int> pii;

double p[20];

int main()
{
	ios_base::sync_with_stdio(false);
	cout << fixed << setprecision(10);
	int t;
	cin >> t;
	for (int it = 1; it <= t; it++){
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			cin >> p[i];
		double ans = 0;
		for (int i = 0; i < (1 << n); i++){
			if (__builtin_popcount(i) != k) continue;
			double prob = 0;
			for (int j = 0; j < i; j++){
				if ((i|j) != i || __builtin_popcount(j) != k/2) continue;
				double thisprob = 1;
				for (int ii = 0; ii < n; ii++)
					if ((i >> ii)&1)
						thisprob *= ( ((j >> ii)&1) ? p[ii] : (1-p[ii]));
				prob += thisprob;
			}
			ans = max(ans, prob);
		}
		cout << "Case #" << it << ": " << ans << '\n';
	}
	return 0;
}
