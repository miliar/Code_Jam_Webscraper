// _template.cpp : Defines the entry point for the console application.
//

#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>

typedef long long ll;
#define PI 3.1415926535897932384626433832795

using namespace std;
#define INF 1000000000
int start, n;
int best;
ll  a[2000000];

int main()
{
	int tc = 0;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> tc;
	for(int tt=1; tt<=tc; ++tt) {
		cin >> start >> n;
		for(int i=0; i<n; ++i) cin >> a[i];

		sort(a, a + n);

		if (start == 1) 
			best = n;
		else{
			best = INF;
			for(int j=0; j<=n; ++j) {
				ll x = start;
				int tmp = n - j;
				for(int i=0; i<j; ++i) {
					while (x<=a[i]) {
						tmp++;
						x += x - 1;
					}
					x += a[i];
				}
				if (tmp < best) {
					best = tmp;
				}
			}
		}
		cout << "Case #" << tt << ": " << best << endl;
	}
	return 0;
}

