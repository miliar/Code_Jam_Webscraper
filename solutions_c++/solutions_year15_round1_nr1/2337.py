#include <iostream>
#include <vector>
#include <string>
#include <memory.h>
#include <set>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <queue>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int maxn = 1000 + 100;

int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	
	int t;
	cin >> t;

	for (int i = 1; i <= t; i++) {
		int n;
		int a[maxn];

		cin >> n;
		for (int j = 0; j < n; j++) cin >> a[j];
		
		int ans1 = 0;
		int cur = a[0];
		for (int j = 1; j < n; j++) {
			if (a[j] < cur) {
				ans1 += cur - a[j];
			}
			cur = a[j];
		}

		int bestm = 0;
		for (int j = 0; j < n - 1; j++) {
			if (a[j] > a[j + 1]) {
				bestm = max(bestm, a[j] - a[j + 1]);
			}
		}
		
		int ans2 = 0;
		for (int j = 0; j < n - 1; j++) {
			if (a[j] > bestm) {
				ans2 += bestm;
			} else {
				ans2 += a[j];
			}
		}

		cout << "Case #" << i << ": " << ans1 << " " << ans2 << endl;
	}

	return 0;
}

