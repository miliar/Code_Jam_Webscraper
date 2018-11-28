#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <complex>
#include <cstdio>
#include <vector>
#include <cctype>
#include <string>
#include <ctime>
#include <cmath>
#include <set>
#include <map>

typedef long double LD;
typedef long long LL;

using namespace std;

#define sz(A) (int)(A).size()
#define mp make_pair
#define pb push_back

const int N = int(1e4 + 5);

int used[N];

int main() {
	int t;
	cin >> t;
	for (int q = 0; q < t; q++) {
		memset(used, 0, sizeof(used));
		int n, x, cnt = 0;
		cin >> n >> x;
		for (int j = 0; j < n; j++) {
			int sz;
			cin >> sz;
			used[sz] += 1;
		}
		int i = x / 2;
		for (int j = (x + 1) / 2; j <= x; j++) {
			while (used[j] > 0) {
				used[j]--;
				n--;
				int rest = x - j;
				if (i > rest) 
					i = rest;
				while (i && !used[i]) i--;
				if (used[i])
					used[i]--, n--;
				cnt++;
			}			
		}
		cnt += (n + 1) / 2;
		printf("Case #%d: %d\n", q + 1, cnt);
	}
	return 0;
}
